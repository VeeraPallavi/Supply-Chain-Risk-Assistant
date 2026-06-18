from src.llm.groq_client import GroqClient

class ReportingAgent:
    
    def __init__(self):
        self.llm = GroqClient()

    def execute(self, query, documents, risks, recommendations):
        context = "\n".join(documents)

        prompt = f"""
        You are a Supply Chain Investigation Analyst.
        Generate an execuive investigation report.

        User Query:
        {query}

        Retrived docs:
        {context}

        Recommendations:
        {recommendations}
        
        Generate the report in this format EXACTLY:
        Excutive Investigation Report
        Query:
        ...

        Summary:
        ...

        Risks:
        ...

        Recommendations:
        ...

        Conclusion:
        ...
        """
        return self.llm.client.chat.completions.create(
            model = "llama-3.1-8b-instant",
            messages=[{"role":"user","content":prompt}],
            temperature=0
        ).choices[0].message.content
