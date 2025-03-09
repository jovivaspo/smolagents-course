import re
import requests
from markdownify import markdownify
from requests.exceptions import RequestException
from smolagents import tool

from dotenv import load_dotenv
import os

load_dotenv()


@tool
def visit_webpage(url: str) -> str:
    """Visits a webpage at the given URL and returns its content as a markdown string.

    Args:
        url: The URL of the webpage to visit.

    Returns:
        The content of the webpage converted to Markdown, or an error message if the request fails.
    """
    try:
        # Send a GET request to the URL
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad status codes

        # Convert the HTML content to Markdown
        markdown_content = markdownify(response.text).strip()

        # Remove multiple line breaks
        markdown_content = re.sub(r"\n{3,}", "\n\n", markdown_content)

        return markdown_content

    except RequestException as e:
        return f"Error fetching the webpage: {str(e)}"
    except Exception as e:
        return f"An unexpected error occurred: {str(e)}"
    
from smolagents import (
    CodeAgent,
    ToolCallingAgent,
    LiteLLMModel,
    ToolCallingAgent,
    DuckDuckGoSearchTool
)

model = LiteLLMModel(
    model_id="gemini/gemini-2.0-flash",
    api_key=os.getenv("GEMINI_TOKEN"))  # Reemplaza con tu API key de OpenAI


# Create a managed agent for the web agent
web_agent = ToolCallingAgent(
    tools=[DuckDuckGoSearchTool(), visit_webpage],
    model=model,
    max_steps=10,
    name="web_search_agent",
    description="Runs web searches for you.",
)


# Create a manager agent to manage the web agent
manager_agent = CodeAgent(
    tools=[],
    model=model,
    managed_agents=[web_agent],
    additional_authorized_imports=["time", "numpy", "pandas"],
)

answer = manager_agent.run("What do you think will happen in 2025 with AI Agents?  Compare the usage in production in the past 12 months.")

print(answer)