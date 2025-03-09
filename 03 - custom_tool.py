from smolagents import CodeAgent, HfApiModel, tool
from huggingface_hub import list_models

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

# Create a CodeAgent
agent = CodeAgent(
    tools=[model_download_tool],
    model=HfApiModel(
        token=os.getenv("TOKEN")
    )
)

# Run the agent
agent.run("Give me the most downloaded model for text-generation on the Huggingface Hub")