from smolagents import CodeAgent, VisitWebpageTool, HfApiModel, Tool

from dotenv import load_dotenv
import os

load_dotenv()

get_travel_duration_tool = Tool.from_space(
    "m-ric/get-travel-duration-tool",
    name="get_travel_duration_tool",
    description="Get travel duration between two locations",
)

response = get_travel_duration_tool(
   "Badajoz", "Cáceres"
)

print(response)

