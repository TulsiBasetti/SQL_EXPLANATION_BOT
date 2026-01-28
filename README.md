#  SQL Explanation Bot 

An **LLM-based SQL Explanation Bot** that takes an SQL queries as input and provides step-by-step explanation of the SQl queries and stores them for future reference.

The bot uses **LangChain** with **Groq-hosted LLaMA 3.3 (70B)** .

---

##  Features

-  Explains SQL queries **step-by-step**
-  Beginner-friendly explanations
-  Does **NOT** execute SQL queries
-  Does **NOT** assume table data or schemas
-  Explains:
  - Query intent
  - Tables involved
  - SQL keywords and clauses
  - Joins, filters, aggregations, aliases, subqueries
-  Saves query + explanation history in JSON format
-  Built using **LangChain Expression Language (LCEL)**

---

##  Tech Stack

- Python
- LangChain
- Groq LLM (LLaMA 3.3 – 70B)
- dotenv
- JSON

---

##  Set up environment variables

- Create a .env file
  GROQ_API_KEY=your_groq_api_key_here

## Example 
# Input:

SELECT name, salary
FROM employee
WHERE salary > 50000;

# Output:

------------------SQL Explanation----------------
Here's the explanation of the SQL query:

1. **Query Intent**:
The intent of this query is to retrieve the names and salaries of employees who earn more than $50,000 from the employee table.

2. **Tables Involved**:
- **employee**: This table is expected to store employee-related information, including their names and salaries.

3. **Keyword / Clause Explanation**:
- **SELECT**: This keyword specifies which columns should be retrieved from the table. In this case, it's selecting two columns: **name** and **salary**.
- **name** and **salary**: These are the columns being requested; they represent the employee's name and salary, respectively.
- **employee**: This is the table that contains the requested columns.
- **WHERE**: This keyword is used to filter the data based on a condition. It only returns rows that meet the specified condition.      
- **salary > 50000**: This is the condition being applied to filter the data. It checks if the employee's salary is greater than $50,000. Only rows where this condition is true will be included in the results.

4. **Final Result Description**:
The query will return a list of employee names and their corresponding salaries, but only for those employees who earn more than $50,000. The result set will contain two columns: **name** and **salary**, with each row representing an employee who meets the specified salary condition.



