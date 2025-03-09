from smolagents import CodeAgent, DuckDuckGoSearchTool, HfApiModel

#tomar el token quen está en el .env
from dotenv import load_dotenv
import os

load_dotenv()
TOKEN = os.getenv("TOKEN")

agent = CodeAgent(
    tools=[DuckDuckGoSearchTool()],
    model=HfApiModel(
        token=TOKEN
    )
)

agent.run("How long would it take for an elephant to cross the united states from florida to california?")