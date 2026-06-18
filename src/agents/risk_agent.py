import re

class RiskAgent:
    def execute(self, documents):
        risks = []
        delayed_count = 0
        pending_count = 0

        for doc in documents:
            # Delivery Risk
            delivery_match = re.search(r"Delivery Time:\s*(\d+\.?\d*)",doc)
            if delivery_match:
                delivery_days = float(delivery_match.group(1))
                if delivery_days >= 7:
                    delayed_count += 1
                    risks.append(f"Delayed delivery risk ({delivery_days:.0f} days)")

            # Status Risk
            status_match = re.search(r"Status:\s*([A-Za-z]+)",doc)
            if status_match:
                status = (status_match.group(1).lower())
                if status == "pending":
                    pending_count += 1
                    risks.append("Pending order risk")
                elif status == "delayed":
                    risks.append("Order currently delayed")

            # Inventory Risks
            stock_match = re.search(r"Stock Level:\s*(-?\d+\.?\d*)",doc)
            reorder_match = re.search(r"Reorder Level:\s*(\d+\.?\d*)",doc)
            if stock_match and reorder_match:
                stock = float(stock_match.group(1))
                reorder = float(reorder_match.group(1))
                if stock == -1:
                    risks.append("Inventory inconsistency detected")
                elif stock < reorder:
                    risks.append("Inventory shortage risk")

            # Transportation Risk
            transport_match = re.search(r"Transport Cost:\s*(\d+\.?\d*)",doc)
            if transport_match:
                transport_cost = float(transport_match.group(1))
                if transport_cost > 5000:
                    risks.append("Excessive transportation expense detected")

        # Operational Anomalies
        if delayed_count >= 3:
            risks.append("Repeated delayed shipment pattern detected")
        if pending_count >= 3:
            risks.append("Persistent pending order pattern detected")

        return list(set(risks))