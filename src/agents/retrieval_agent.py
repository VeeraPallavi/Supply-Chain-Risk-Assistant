import re
from src.rag.retriever import Retriever

class RetrievalAgent:

    def __init__(self):
        self.retriever = Retriever()

    def execute(self, query, top_k=5):
        docs = self.retriever.retrieve(query, top_k)
        query_lower = query.lower()
        if "order" in query_lower:
            docs = [doc for doc in docs if "Order ID" in doc]
            regions = ["east", "west", "north", "south"]
            for region in regions:
                if region in query_lower:
                    docs = [doc for doc in docs if f"Region: {region.title()}" in doc]

            warehouses = ["wh-a", "wh-b", "wh-c"]
            for warehouse in warehouses:
                if warehouse in query_lower:
                    docs = [doc for doc in docs if f"Warehouse: {warehouse.upper()}" in doc]

        elif any(word in query_lower for word in ["inventory", "stock", "replenishment", "supplier"]):
            docs = [doc for doc in docs if "Inventory ID" in doc]
            if "replenishment" in query_lower:
                filtered = []
                for doc in docs:
                    stock = re.search(r"Stock Level:\s*(\d+\.?\d*)",doc)
                    reorder = re.search(r"Reorder Level:\s*(\d+\.?\d*)",doc)
                    if stock and reorder:
                        if float(stock.group(1)) < float(reorder.group(1)):
                            filtered.append(doc)
                docs = filtered

        return docs[:5]