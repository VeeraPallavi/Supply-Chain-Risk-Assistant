from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

class GroqClient:

    def __init__(self):
        self.client = Groq(api_key=os.getenv("GROQ_API"))

    def generate(self, query, context, risks):
        prompt = f"""
        You are a Supply Chain Risk Analyst.
        
        STRICT RULES:
        1. Use ONLY the retrieved context.
        2. If retrived context does not support the user's request, explicity say so.
        3. DO NOT assume facts.
        4. DO NOT infer replenishment needs unless 
            Stock Level < Reorder Level
            
        User Query:
        {query}
        
        Retrieved Context:
        {context}
        
        Identified Risks:
        {risks}
        
        Return EXACTLY this format:
        Answer:
        ...
        
        Risks:
        ...
        
        Explanation:
        ...
        """

        response = self.client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0
        )

        return response.choices[0].message.content
    