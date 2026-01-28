import json
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
import os

load_dotenv()


llm=ChatGroq(
    model='llama-3.3-70b-versatile',
    temperature=0.2
)


system_prompt = """
You are a senior SQL engineer and instructor.

Your task is to explain SQL queries in a clear, beginner-friendly, and educational way.
Assume the user is new to SQL and wants to understand what each part of the query does.

Rules:
- Do NOT execute the query
- Do NOT assume any table data or actual results
- Do NOT guess schemas beyond what is written
- Explain the query step-by-step
- If joins, filters, aggregations, or subqueries exist, explain them clearly
- If aliases are used, explain what they refer to
- When appropriate, explain the purpose of individual SQL keywords

Explanation Guidelines:
1. First, identify the overall intent of the query.
2. Then list the tables involved.
3. Then explain the query clause-by-clause in execution order.
4. For simple queries, explain the role of each SQL keyword (e.g., SELECT, FROM).
5. End with a clear description of what the query would return conceptually.

Output format:
1. Query Intent
2. Tables Involved
3. Keyword / Clause Explanation
4. Final Result Description

------------------------------------
Example:

SQL Query:
SELECT name FROM employee;

Explanation:

1. Query Intent:
The intent of this query is to retrieve the names of employees from the employee table.

2. Tables Involved:
- employee: This table is expected to store employee-related information.

3. Keyword / Clause Explanation:
- SELECT: This keyword specifies which columns should be retrieved from the table.
- name: This is the column being requested; it represents the employee's name.
- FROM: This keyword specifies the table from which the data should be fetched.
- employee: This is the table that contains the requested column.

4. Final Result Description:
The query will return a list of employee names from the employee table.

------------------------------------

Now, explain the user-provided SQL query following the same structure and level of detail.
"""

prompt=ChatPromptTemplate.from_messages([
    ('system',system_prompt),
    ('human',"Explain the followimg SQL Query : {sql_query} \n")
])

parser=StrOutputParser()

chain=prompt | llm | parser


JSON_FILE = "sql_explanation.json"

def save_to_json(query, explanation):
    if os.path.exists(JSON_FILE):
        with open(JSON_FILE, "r", encoding="utf-8") as f:
            try:
                data = json.load(f)
                if not isinstance(data, list):
                    data = []
            except json.JSONDecodeError:
                data = []
    else:
        data = []

    data.append({
        "sql_query": query.strip(),
        "explanation": explanation.strip()
    })

    with open(JSON_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)


def sql_explainer():
    print("Enter your SQL Query here : \n")
    query=""
    while True:
        line=input()
        query+=line+'\n'
        if ";" in line:
            break
    result= chain.invoke({
        "sql_query": query
    })

    print("------------------SQL Explanation----------------")
    print(result)

    save_to_json(query, result)

if __name__=="__main__":
    sql_explainer()