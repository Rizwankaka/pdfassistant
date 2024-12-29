import streamlit as st
from phi.assistant import Assistant
from phi.storage.assistant.postgres import PgAssistantStorage
from phi.knowledge.pdf import PDFUrlKnowledgeBase
from phi.vectordb.pgvector import PgVector2
import os
from dotenv import load_dotenv

load_dotenv()

# Streamlit app title
st.title("PDF Knowledge Base Assistant")

# Sidebar for user input
with st.sidebar:
    st.header("Configuration")
    groq_api_key = st.text_input("Enter GROQ API KEY", type="password")
    pdf_url = st.text_input("Enter PDF URL")
    user_id = st.text_input("Enter User ID", value="user")
    new_session = st.checkbox("Start New Session", value=False)

    if st.button("Load Knowledge Base"):
        if groq_api_key and pdf_url:
            os.environ["GROQ_API_KEY"] = groq_api_key
            db_url = "postgresql+psycopg://ai:ai@localhost:5532/ai"

            knowledge_base = PDFUrlKnowledgeBase(
                urls=[pdf_url],
                vector_db=PgVector2(collection="recipes", db_url=db_url)
            )

            knowledge_base.load()

            storage = PgAssistantStorage(table_name="pdf_assistant", db_url=db_url)

            run_id = None
            if not new_session:
                existing_run_ids = storage.get_all_run_ids(user_id)
                if len(existing_run_ids) > 0:
                    run_id = existing_run_ids[0]

            assistant = Assistant(
                run_id=run_id,
                user_id=user_id,
                knowledge_base=knowledge_base,
                storage=storage,
                show_tool_calls=True,
                search_knowledge=True,
                read_chat_history=True,
            )

            if run_id is None:
                run_id = assistant.run_id
                st.success(f"Started Run: {run_id}\n")
            else:
                st.success(f"Continuing Run: {run_id}\n")

            # Store the assistant in the session state
            st.session_state.assistant = assistant
        else:
            st.error("Please provide both GROQ API KEY and PDF URL.")

# Main area for interacting with the assistant
if "assistant" in st.session_state:
    assistant = st.session_state.assistant
    user_input = st.text_input("Ask a question:")

    if user_input:
        response = assistant.run(user_input)
        st.write(response)