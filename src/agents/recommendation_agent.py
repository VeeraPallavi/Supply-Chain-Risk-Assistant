class RecommendationAgent:

    def execute(self, risks):
        recommendations = []
        for risk in risks:
            if "Delayed delivery" in risk:
                recommendations.append("Expedite shipments and notify stakeholders.")
                recommendations.append("Review warehouse operations to reduce delivery delays.")

            if "Order currently delayed" in risk:
                recommendations.append("Provide customers with delivery status updates.")

            if "Low inventory" in risk:
                recommendations.append("Trigger replenishment process.")
                recommendations.append("Increase safety stock levels.")

            if "Potential stockout" in risk:
                recommendations.append("Prioritize replenishment for critical products.")

            if "Multiple inventory shortages" in risk:
                recommendations.append("Coordinate with suppliers to avoid stockouts.")
                recommendations.append("Review inventory planning strategy.")

            if "Supply chain disruption" in risk:
                recommendations.append("Identify alternative suppliers and warehouses.")

            if "Inventory data quality issue" in risk:
                recommendations.append("Validate missing inventory values in the source data.")

            if "Repeated delayed shipment" in risk:
                recommendations.append("Investigate root cause and supplier performance.")
                recommendations.append("Perform supplier performance assessment.")

        return list(set(recommendations))