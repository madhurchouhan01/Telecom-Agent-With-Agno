import streamlit as st
from agents import handle_query


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
                response = handle_query(user_query)
            with st.chat_message('Momos', avatar="🤖"):
                st.markdown(response)  # Display as Markdown
        except Exception as e:
            st.error(f"Error occurred: {e}")
    else:
        st.warning("Please enter a query.")

# Run with: streamlit run streamlit_app.py
