import re
from src.rag.retriever import Retriever
from src.utils.query_utils import normalize_query, get_query_intent

class RetrievalAgent:

    def __init__(self):
        self.retriever = Retriever()

    def execute(self, query, top_k=20):
        query_lower = normalize_query(query)
        intent = get_query_intent(query)
        all_docs = self.retriever.get_all_documents()

        docs = []

        delayed_keywords = [
            "delay",
            "delayed",
            "late",
            "shipment",
            "delivery"
        ]

        if any(k in query_lower for k in delayed_keywords):
            docs = [
                d for d in all_docs
                if "Order ID" in d
                and "Status: Delayed" in d
            ]

        elif "pending" in query_lower:
            docs = [
                d for d in all_docs
                if "Order ID" in d
                and "Status: Pending" in d
            ]

        elif any(
            word in query_lower
            for word in [
                "delivered",
                "completed"
            ]
        ):

            docs = [
                d for d in all_docs
                if "Order ID" in d
                and "Status: Delivered" in d
            ]

        elif any(
            word in query_lower
            for word in [
                "low stock",
                "replenishment",
                "reorder"
            ]
        ):

            for doc in all_docs:
                if "Inventory ID" not in doc:
                    continue

                stock = re.search(r"Stock Level:\s*(\d+\.?\d*)",doc)
                reorder = re.search(r"Reorder Level:\s*(\d+\.?\d*)",doc)

                if stock and reorder:
                    if float(stock.group(1)) < float(reorder.group(1)):
                        docs.append(doc)

    
        elif "supplier" in query_lower:
            docs = [
                d for d in all_docs
                if "Supplier:" in d
            ]

        elif "most delayed" in query_lower:
            delayed_docs = [
                d for d in all_docs
                if "Status: Delayed" in d
            ]

            delayed_docs.sort(
                key=lambda x: float(
                    re.search(
                        r"Delivery Time:\s*(\d+\.?\d*)",
                        x
                    ).group(1)
                ),
                reverse=True
            )

            docs = delayed_docs[:1]

        else:
            docs = self.retriever.retrieve(query_lower,top_k)
            if intent == "orders":
                docs = [d for d in docs if "Order ID" in d]
            elif intent == "inventory":
                docs = [d for d in docs if "Inventory ID" in d]

        if "east" in query_lower:
            docs = [d for d in docs if "Region: East" in d]

        elif "west" in query_lower:
            docs = [d for d in docs if "Region: West" in d]

        elif "north" in query_lower:
            docs = [d for d in docs if "Region: North" in d]

        elif "south" in query_lower:
            docs = [d for d in docs if "Region: South" in d]

        for wh in ["wh-a", "wh-b", "wh-c"]:
            if wh in query_lower:
                docs = [d for d in docs if f"Warehouse: {wh.upper()}" in d]

        for product in [
            "server",
            "router",
            "storage",
            "switch",
            "laptop"
        ]:
            if product in query_lower:
                docs = [d for d in docs if f"Product: {product.title()}" in d]

        for supplier in [
            "supplier-x",
            "supplier-y",
            "supplier-z"
        ]:

            if supplier in query_lower:
                docs =[d for d in docs if f"Supplier: {supplier.title()}" in d]

        print("Final Docs:", len(docs))

        return docs[:10]