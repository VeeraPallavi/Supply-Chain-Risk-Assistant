import re

class RiskAgent:

    def execute(self, documents):
        risks = []
        for doc in documents:

            if "Status: Delayed" in doc:
                risks.append("Order currently delayed")

            delivery = re.search(r"Delivery Time:\s*(\d+\.?\d*)",doc)
            if delivery:
                days = float(delivery.group(1))
                if days >= 7:
                    risks.append(f"Delayed delivery risk ({int(days)} days)")

            # LOW INVENTORY
            stock = re.search(r"Stock Level:\s*(\d+\.?\d*)",doc)
            reorder = re.search(r"Reorder Level:\s*(\d+\.?\d*)",doc)
            if stock and reorder:
                stock_level = float(stock.group(1))
                reorder_level = float(reorder.group(1))

                if stock_level < reorder_level:
                    risks.append("Low inventory risk")
                    risks.append("Potential stockout risk")
                    risks.append("Supply chain disruption risk")

            if "Stock Level: nan" in doc:
                risks.append("Inventory data quality issue")

        # REPEATED DELAYS
        delayed_count = len(
            [
                d for d in documents
                if "Status: Delayed" in d
            ]
        )

        if delayed_count >= 3:
            risks.append("Repeated delayed shipment pattern detected")

        # MULTIPLE LOW STOCK ITEMS
        low_stock_count = 0
        for doc in documents:
            stock = re.search(r"Stock Level:\s*(\d+\.?\d*)",doc)
            reorder = re.search(r"Reorder Level:\s*(\d+\.?\d*)",doc)
            if stock and reorder:
                if float(stock.group(1)) < float(reorder.group(1)):
                    low_stock_count += 1
        if low_stock_count >= 3:
            risks.append("Multiple inventory shortages detected")

        return list(set(risks))