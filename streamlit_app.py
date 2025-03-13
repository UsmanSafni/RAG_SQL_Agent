import streamlit as st
import asyncio
from query_agent import RouterOutputAgentWorkflow
from tool import sql_tool, llama_cloud_tool
import llama_cloud_setup1

# Initialize workflow
wf = RouterOutputAgentWorkflow(tools=[sql_tool, llama_cloud_tool], verbose=True, timeout=120)

async def main1(query):
    result = await wf.run(message=query)
    return result



# Streamlit UI
st.title("RAG SQL Agent Query UI")

# User input
query = st.text_input("Enter your SQL-related query:")

if st.button("Submit"):
    if query:
        with st.spinner("Processing..."):
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            result = loop.run_until_complete(main1(query))  # Properly handling async function
        st.success("Query executed successfully!")
        st.write(f"{result}")
    else:
        st.warning("Please enter a query before submitting.")