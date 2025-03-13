import streamlit as st
import asyncio
from query_agent import RouterOutputAgentWorkflow
from tool_setup import QueryEngineTools

class RAGSQLAgentApp:
    """Streamlit UI for querying SQL databases using an agent workflow."""

    def __init__(self):
        """Initialize the application and workflow."""
        self.tools = QueryEngineTools()
        self.workflow = RouterOutputAgentWorkflow(
            tools=[self.tools.get_sql_tool(), self.tools.get_llama_cloud_tool()], 
            verbose=True, 
            timeout=120
        )
        self._setup_ui()

    async def run_query(self, query):
        """Runs the query asynchronously using the workflow."""
        return await self.workflow.run(message=query)

    def _setup_ui(self):
        """Setup Streamlit UI components."""
        st.title("RAG SQL Agent Query UI")

        query = st.text_input("Enter your SQL-related query:")

        if st.button("Submit"):
            if query:
                with st.spinner("Processing..."):
                    loop = asyncio.new_event_loop()
                    asyncio.set_event_loop(loop)
                    result = loop.run_until_complete(self.run_query(query))
                st.success("Query executed successfully!")
                st.write(result)
            else:
                st.warning("Please enter a query before submitting.")


# Run the Streamlit app
if __name__ == "__main__":
    RAGSQLAgentApp()
