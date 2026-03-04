# Pre-Task Engineering Check

Before starting the assignment, please answer the following questions.

This step helps us understand your engineering reasoning.

Submit your answers in the README of your solution repository.



## Question 1

What is wrong with the following code?

JavaScript

function sum(numbers) {
  let total = 0

  for (let i = 0; i <= numbers.length; i++) {
    total += numbers[i]
  }

  return total
}

Explain the issue and provide a fix.


## Question 2

Consider the following API response:

{
  "income": "80000",
  "expenses": 52000
}

If we calculate:

savings = income - expenses

What issue might occur on the frontend?

How would you fix it?



## Question 3

You have a database table with 5 million transactions.

Query:

SELECT * FROM transactions WHERE user_id = 123

Why could this query be slow?

What would you do to improve it?



## Question 4

What is one situation where AI-generated code should **not** be trusted?
