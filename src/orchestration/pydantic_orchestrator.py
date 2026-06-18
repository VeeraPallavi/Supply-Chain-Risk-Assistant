from src.agents.retrieval_agent import RetrievalAgent
from src.agents.risk_agent import RiskAgent
from src.agents.recommendation_agent import RecommendationAgent
from src.agents.reporting_agent import ReportingAgent

from src.orchestration.models import InvestigationResult

class SupplyChainWorkflow:

    def __init__(self):
        self.retrieval = RetrievalAgent()
        self.risk = RiskAgent()
        self.recommendation = RecommendationAgent()
        self.reporting = ReportingAgent()

    def execute(self, query):
        documents = self.retrieval.execute(query)
        risks = self.risk.execute(documents)
        recommendations = (self.recommendation.execute(risks))
        report = self.reporting.execute(
            query=query,
            documents=documents,
            risks=risks,
            recommendations=recommendations
        )

        return InvestigationResult(
            documents=documents,
            risks=risks,
            recommendations=recommendations,
            report=report
        )