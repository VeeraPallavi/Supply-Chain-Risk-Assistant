from pydantic import BaseModel
from typing import List

class ChatRequest(BaseModel):
    query: str

class ChatResponse(BaseModel):
    documents: List[str]
    risks: List[str]
    recommendations: List[str]
    report: str