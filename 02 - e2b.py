from smolagents import CodeAgent, VisitWebpageTool, HfApiModel, E2BSandbox

#tomar el token quen está en el .env
from dotenv import load_dotenv
import os

load_dotenv()
TOKEN = os.getenv("TOKEN")
E2B = os.getenv("E2B")

agent = CodeAgent(
    tools=[VisitWebpageTool()],
    model=HfApiModel(
        token=TOKEN
    ),
    additional_authorized_imports=["requests", "markdownify"],
   sandbox=E2BSandbox(),
    
)

agent.run("What was Abraham Lincoln's favorite food?")