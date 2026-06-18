from pydantic_ai import Agent
from src.orchestration.models import InvestigationResult

agent = Agent(
    "groq:llama-3.1-8b-instant",
    result_type=InvestigationResult,
    system_prompt="""
    You are a Supply Chain Risk Investigation Assistant.
    """
)