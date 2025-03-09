from smolagents import load_tool, CodeAgent, HfApiModel
from dotenv import load_dotenv
import os

load_dotenv()

image_generation_tool = load_tool(
    "m-ric/text-to-image",
    trust_remote_code=True
)

agent = CodeAgent(
    tools=[image_generation_tool],
    model=HfApiModel(
        token=os.getenv("TOKEN")
    )
)

agent.run("Generate an image of a luxurious superhero-themed party at Wayne Manor with made-up superheros.")