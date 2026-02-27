import streamlit as st
import sqlite3
import pandas as pd

# -----------------------
# Simple Rule-Based NL → SQL
# -----------------------
def convert_nl_to_sql(question):
    q = question.lower()

    if "count" in q or "how many" in q:
        return "SELECT COUNT(*) FROM STUDENTS;"

    elif "average" in q:
        return "SELECT AVG(MARKS) FROM STUDENTS;"

    elif "highest" in q or "top" in q or "maximum" in q:
        return "SELECT * FROM STUDENTS WHERE MARKS = (SELECT MAX(MARKS) FROM STUDENTS);"

    elif "lowest" in q or "minimum" in q:
        return "SELECT * FROM STUDENTS WHERE MARKS = (SELECT MIN(MARKS) FROM STUDENTS);"

    elif "infosys" in q:
        return 'SELECT * FROM STUDENTS WHERE COMPANY = "Infosys";'

    elif "tcs" in q:
        return 'SELECT * FROM STUDENTS WHERE COMPANY = "TCS";'

    elif "wipro" in q:
        return 'SELECT * FROM STUDENTS WHERE COMPANY = "Wipro";'

    elif "mcom" in q:
        return 'SELECT * FROM STUDENTS WHERE CLASS = "MCom";'

    elif "btech" in q:
        return 'SELECT * FROM STUDENTS WHERE CLASS = "BTech";'

    elif "mba" in q:
        return 'SELECT * FROM STUDENTS WHERE CLASS = "MBA";'

    elif "show all" in q or "display all" in q or "all students" in q:
        return "SELECT * FROM STUDENTS;"

    else:
        return "SELECT * FROM STUDENTS;"


# -----------------------
# Execute SQL
# -----------------------
def execute_query(sql):
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()
    cursor.execute(sql)
    rows = cursor.fetchall()
    columns = [desc[0] for desc in cursor.description] if cursor.description else []
    conn.close()
    return rows, columns


# -----------------------
# PAGE 1 — Home
# -----------------------
def page_home():
    st.title("🚀 Welcome to IntelliSQL!")
    st.subheader("Intelligent SQL Querying System")
    st.write("""
    IntelliSQL converts natural language questions into SQL queries 
    and executes them on a database.
    """)


# -----------------------
# PAGE 2 — About
# -----------------------
def page_about():
    st.title("📌 About IntelliSQL")
    st.write("""
    IntelliSQL is designed to demonstrate Natural Language 
    to SQL conversion for database querying.
    
    It supports:
    - Intelligent Query Assistance
    - Data Exploration
    - Automatic SQL Generation
    - Real-Time Query Execution
    """)


# -----------------------
# PAGE 3 — Query Page
# -----------------------
def page_query():
    st.title("💡 Intelligent Query Assistance")

    user_question = st.text_input("Enter your database question:")

    if st.button("Generate & Execute"):
        if not user_question:
            st.warning("Please enter a question.")
            return

        sql_query = convert_nl_to_sql(user_question)

        st.subheader("Generated SQL Query:")
        st.code(sql_query, language="sql")

        try:
            rows, cols = execute_query(sql_query)

            st.subheader("Query Results:")

            if rows:
                df = pd.DataFrame(rows, columns=cols)
                st.dataframe(df, use_container_width=True)
            else:
                st.info("Query executed successfully. No rows returned.")

        except Exception as e:
            st.error(f"SQL Execution Error: {e}")


# -----------------------
# MAIN
# -----------------------
def main():
    st.set_page_config(page_title="IntelliSQL", layout="wide")

    st.sidebar.title("Navigation")
    page = st.sidebar.radio(
        "Go to",
        ["Home", "About", "Intelligent Query"]
    )

    if page == "Home":
        page_home()
    elif page == "About":
        page_about()
    elif page == "Intelligent Query":
        page_query()


if __name__ == "__main__":
    main()