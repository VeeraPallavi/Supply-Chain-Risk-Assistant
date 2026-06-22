def normalize_query(query):
    query = query.lower().strip()
    replacements = {
    "list delayed orders": "delayed order",
    "show delayed orders": "delayed order",
    "which orders are delayed": "delayed order",
    "late shipments": "delayed order",
    "delivery issues": "delayed order",
    "pending shipments": "delayed order",

    "show stock shortages": "low stock",
    "stock shortage": "low stock",
    "stock shortages": "low stock",
    "inventory shortage": "low stock",
    "inventory shortages": "low stock",
    "replenishment needed": "low stock"
}

    for old, new in replacements.items():
        query = query.replace(old, new)

    return query

def get_query_intent(query):
    query = normalize_query(query)
    if any(
        word in query
        for word in [
            "delayed",
            "shipment",
            "order",
            "delivery"
        ]
    ):
        return "orders"
    if any(
    word in query
    for word in [
        "inventory",
        "stock",
        "low stock",
        "stock shortage",
        "inventory shortage",
        "inventory shortages",
        "replenishment",
        "supplier"
        ]
    ):
        return "inventory"

    return "general"