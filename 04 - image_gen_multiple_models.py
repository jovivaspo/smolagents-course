from smolagents import CodeAgent, HfApiModel, tool, Tool
from huggingface_hub import list_models, InferenceClient

from dotenv import load_dotenv
import os

load_dotenv()

@tool
def model_download_tool(task: str) -> str:
    """
    This is a tool that returns the most downloaded model of a fiven task on the Huggingface Hub.
    It returns the name of the checkpoint.

    Args:
        task: The task for which you want to download the model.
    """
    most_downloaded = next(iter(list_models(filter=task, sort="downloads", direction=-1)))
    return most_downloaded.id


class TextToImageTool(Tool):
    description = "This tool creates an image according to a prompt, which is a text description."

    name = "image_generator"

    inputs = {
        "prompt": {
            "type": "string",
            "description": "The image generator prompt. Don't hesitate to add details in the prompt to make the image look better."
        },
        "model": {
            "type": "string",
            "description": "The model checkpoint to use for the image generation."
        }
    }

    output_type = "image"
    current_model = "black-forest-labs/Flux.1-schnell"

    def forward(self, prompt, model):
        if model:
            if model != self.current_model:
                self.current_model = model
                self.client = InferenceClient(model)
            if not self.client:
                self.client = InferenceClient(self.current_model)
        image = self.client.text_to_image(prompt)
        image.save("image.png")

        return f"Successfully generated image for prompt: {prompt} using model {self.current_model}."

#Instantiate the tool
image_gen_tool = TextToImageTool()

# Create a CodeAgent
agent = CodeAgent(
    tools=[image_gen_tool, model_download_tool],
    model=HfApiModel(
        token=os.getenv("TOKEN")
    )
)

# Run the agent
agent.run("Improve this prompt, then generate an image of it. Prompt: A cat wearing a hazmat suit in contaminated area. Get hte latest model for text-to-image from the Huggingface Hub.")

# The image generated is really bad because the most downloaded model for text-to-image generation is very old.