# Financial Health Score API

The system should calculate a user's **Financial Health Score (0–100)** based on financial behavior.

This score will help users understand their overall financial stability.

---

## API Endpoint

GET /financial-health/:userId

---

## Example Response

{
  "score": 74,
  "category": "Healthy",
  "suggestions": [
    "Increase emergency fund",
    "Reduce discretionary expenses"
  ]
}

---

## Score Components

The score should be calculated based on the following components.

### 1. Emergency Fund

Months of expenses covered by liquid savings.

Example:

Emergency Fund = Savings / Monthly Expenses

Suggested scoring:

0–1 months → 5 points  
1–3 months → 10 points  
3–6 months → 20 points  
>6 months → 25 points

---

### 2. Savings Rate

Savings Rate = (Savings / Income) * 100

Suggested scoring:

<10% → 5 points  
10–20% → 10 points  
20–40% → 20 points  
>40% → 25 points

---

### 3. Debt Ratio

Debt Ratio = Total EMI / Monthly Income

Suggested scoring:

>50% → 5 points  
30–50% → 10 points  
10–30% → 15 points  
<10% → 20 points

---

### 4. Investment Ratio

Investment Ratio = Investments / Income

Suggested scoring:

<5% → 5 points  
5–15% → 10 points  
15–30% → 15 points  
>30% → 20 points

---

## Final Score

Total Score = Emergency Fund + Savings Rate + Debt Ratio + Investment Ratio

Maximum Score = 100

---

## Categories

80–100 → Excellent  
60–79 → Healthy  
40–59 → Moderate  
Below 40 → At Risk

---

## Requirements

Implement:

• Score calculation logic  
• API endpoint  
• Suggestions based on score  
• Edge case handling

---

## Edge Cases

Handle:

• Zero income  
• Missing financial data  
• Negative values  
• Very large transaction volumes

---

Explain your **design decisions** in README.
