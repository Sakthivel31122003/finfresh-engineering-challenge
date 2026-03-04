async def calculate_monthly_summary(user_id):

    transactions = db.transactions.find({"user_id": user_id})

    income = 0
    expense = 0
    categories = {}

    for t in transactions:

        if t["type"] == "income":
            income += t["amount"]

        if t["type"] == "expense":
            expense += t["amount"]

        if t["category"] not in categories:
            categories[t["category"]] = 0

        categories[t["category"]] += t["amount"]

    savings = income - expense

    savings_rate = savings / income * 100

    summary = {
        "user_id": user_id,
        "income": income,
        "expense": expense,
        "savings": savings,
        "savings_rate": savings_rate,
        "categories": categories
    }

    db.summary.insert(summary)

    return summary
