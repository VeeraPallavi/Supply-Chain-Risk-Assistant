from fastapi import FastAPI, HTTPException, Header
from src.models.api_models import ChatRequest,ChatResponse
from src.orchestration.pydantic_orchestrator import SupplyChainWorkflow

from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("API_KEY")

def verify_api_key(x_api_key : str):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401,detail="Invalid API Key")
    
app = FastAPI(
    title="Enterprise GenAI Supply Chain Risk Intelligence Assistant",
    description="Multi-Agent Supply Chain Investigation Platform"
)

workflow = SupplyChainWorkflow()

@app.get("/")
def home():
    return {
        "message":"Enterprise GenAI Supply Chain Risk Intelligence Assistant"
    }

@app.post("/chat",response_model=ChatResponse)
def chat(request:ChatRequest,x_api_key : str=Header(...)):
    try:
        verify_api_key(x_api_key)
        result = workflow.execute(request.query)
        return ChatResponse(
            documents=result.documents,
            risks=result.risks,
            recommendations=result.recommendations,
            report=result.report
        )
    except Exception as e:
        raise HTTPException(status_code=500,detail=str(e))
