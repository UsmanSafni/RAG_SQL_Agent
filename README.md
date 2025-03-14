# RAG and Text-to-SQL Agent

This project builds a custom agent that can  query either your LlamaCloud index for RAG-based retrieval or a separate SQL query engine as a tool. In this example, we'll use PDFs of Wikipedia pages of US cities and a SQL database of their populations and states as documents.

We use:

- LlamaIndex for orchestrating the agent.
- Phoenix-arize for observability.
- Streamlit to build the UI.

A demo is shown below:

[Video demo](demo.mp4)

[Hugging space Space](demo.mp4)

 

## Installation and setup

**Setup LlamaCloud API**:

Get an API key from [LLamaCloud](https://cloud.llamaindex.ai/project/3e57d6f7-a4d2-482b-bedd-b72547d1a286/api-key) and set it in the `.env` file as follows:

```bash
LLAMA_CLOUD_API_KEY=<YOUR_API_KEY> 
```

**Setup Observability**:

For Observability, set  setup an integration with LlamaTrace. Get an API key from [LlamaTrace](https://llamatrace.com/login) and set it in the `.env` file as follows:

```bash
PHOENIX_API_KEY=<YOUR_API_KEY> 
```

**Setup OpenAI API**:

Get an API key from [OpenAI](https://platform.openai.com/) and set it in the `.env` file as follows:

```bash
OPENAI_API_KEY=<YOUR_API_KEY> 
```

**Install Dependencies**:
   Ensure you have Python 3.11 or later installed.

   ```bash
   pip install -r requirements.txt
   ```

**Run the app**:

   Run the app by running the following command:

   ```bash
   streamlit run app.py
   ```

---

## 📬 Stay Updated with Our Newsletter!
**Get a FREE Data Science eBook** 📖 with 150+ essential lessons in Data Science when you subscribe to our newsletter! Stay in the loop with the latest tutorials, insights, and exclusive resources. [Subscribe now!](https://join.dailydoseofds.com)

[![Daily Dose of Data Science Newsletter](https://github.com/patchy631/ai-engineering/blob/main/resources/join_ddods.png)](https://join.dailydoseofds.com)

---

## Contribution

Contributions are welcome! Please fork the repository and submit a pull request with your improvements.
