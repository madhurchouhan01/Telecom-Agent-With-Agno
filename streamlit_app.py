import streamlit as st
from agno.team.team import Team
from agno.agent import Agent, RunResponse
from agno.models.groq import Groq
from agno.tools.duckduckgo import DuckDuckGoTools
from query import check_balance
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize Agents
faq_agent = Agent(
    name="FAQ Agent",
    role="You are an FAQ agent that provides information to users about any asked query.",
    model=Groq(id="llama-3.3-70b-versatile"),
    instructions=[
        "You need to give the solution to the user.",
        "You should not explain reasons for issues unless explicitly asked by the user.",
    ],
    tools=[DuckDuckGoTools()]
)

acc_agent = Agent(
    name="Account Agent",
    role="You are an Account Agent with access to user account information.",
    model=Groq(id="llama-3.3-70b-versatile"),
    instructions=[
        "You need to give the account information to the user.",
        "If you do not have information, simply say - 'No Data is Available!'",
    ],
    tools=[check_balance],  # Ensure `check_balance` returns a string or JSON response
)

# Initialize Customer Support Team
customer_support_agent = Team(
    name="Customer Support Agent",
    mode="route",
    model=Groq("llama-3.3-70b-versatile"),
    members=[faq_agent, acc_agent],
    show_tool_calls=True,
    markdown=True,
    instructions=[
        "You are a lead Customer Support Agent that routes the user to the appropriate agent based on the query.",
        "If no agent can handle the task, respond with - 'This query is not supported.'",
    ],
    show_members_responses=True,
)

# Streamlit UI
st.set_page_config(page_title="Customer Support Chatbot", layout="centered")

st.title("📞 Customer Support Chatbot")
st.write("Ask your queries about telecom services, account details, and FAQs.")

# User Input
user_query = st.text_input("Enter your query:")

if st.button("Submit Query"):
    if user_query:
        try:
            with st.spinner("Processing your request..."):
                run: RunResponse = customer_support_agent.run(user_query)
                response = run.content
                st.success("AI:")
                st.markdown(response)  # Display as Markdown
        except Exception as e:
            st.error(f"Error occurred: {e}")
    else:
        st.warning("Please enter a query.")

# Run with: streamlit run streamlit_app.py
