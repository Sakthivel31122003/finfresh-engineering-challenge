**Frontend Dashboard Task**
Build a simple Financial Dashboard UI for the Personal Finance Tracker.
You may use:
• React
or
• Next.js
or
Flutter

 (React or Next.JS developer can give a shot for flutter aswell and vise versa - not mandatory)
UI design quality is not important. Focus on correct functionality and clean code structure.

**Dashboard Requirements**
The dashboard should display the user's financial summary.
Show the following metrics:
Monthly Income
Monthly Expenses
Savings
Savings Rate
Financial Health Score
**Example:**
Income: ₹80,000
Expenses: ₹52,000
Savings: ₹28,000
Savings Rate: 35%
Financial Health Score: 74

**Category Breakdown**
Display category-wise spending.
Example:
Housing – ₹20,000
Food – ₹12,000
Transport – ₹6,000
Entertainment – ₹4,000

**API Integration**
The dashboard should fetch data from the backend APIs.
Example APIs:
GET /summary
GET /financial-health/:userId
GET /transactions

**Functional Requirements**
The dashboard must handle:
• API loading state
• API failure
• empty data state
• incorrect data gracefully
Example:No transactions found

**Component Structure**
Use clean component separation.
Example structure:
components/
  SummaryCard
  CategoryBreakdown
  FinancialHealth

  **Expected Features**
The dashboard should allow the user to:
• view financial summary
• see spending breakdown
• see financial health score
Optional:
• add new transaction form
• chart visualization

**Performance Consideration**
The dashboard should remain responsive even when the user has thousands of transactions.
Explain in README how you would scale this UI.

**Edge Cases**
Your frontend should handle:
• zero income
• no transactions
• API failure
• extremely large numbers

**Submission Notes**
Your submission should include:
• clean component structure
• API integration
• error handling
• readable code
Explain your frontend architecture decisions in the README.

**Optional Bonus**
You may optionally add:
• chart visualization (Chart.js / Recharts)
• responsive layout
• transaction filter by date
These are not required.

**Important**
Keep the implementation simple and maintainable.
We evaluate:
• correctness
• code structure
• reasoning
—not UI polish.

**Data Consistency Requirement**
Sometimes financial data may arrive in inconsistent formats.
For example:
Income: "80000"
Expense: 52000
Amount: "1200.50"
Amount: null
Your dashboard should handle inconsistent numeric values safely.
Ensure:
• numbers stored as strings are converted correctly
• null values do not break calculations
• invalid values do not crash the UI
For example:
Savings = Income - Expense
Should still work even if values are strings.
