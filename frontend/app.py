import os
from dotenv import load_dotenv
import streamlit as st
import requests

load_dotenv()

st.set_page_config(
    page_title="Supply Chain Risk Assistant",
    page_icon="📦",
    layout="wide"
)

if "history" not in st.session_state:
    st.session_state.history = []

with st.sidebar:
    st.title("📦 About")
    st.markdown("""
    ### Enterprise GenAI Supply Chain Risk Intelligence Assistant

    **Technologies Used**
    - FastAPI
    - FAISS Vector Database
    - Sentence Transformers
    - Groq LLM
    - Multi-Agent System
    - Streamlit Frontend
    """)
    st.divider()
    st.subheader("Example Questions")
    examples = [
        "List delayed orders in East region",
        "Which warehouse has the most delayed orders?",
        "Which products need replenishment?",
        "Which supplier has delivery issues?",
        "Show all pending orders",
        "Show stock shortages"
    ]

    for q in examples:
        st.write("•", q)
    st.divider()
    st.subheader("Investigation History")
    if st.session_state.history:
        for item in reversed(st.session_state.history):
            st.write("•", item)
    else:
        st.caption("No investigations yet.")

st.title("📦 Enterprise GenAI Supply Chain Risk Intelligence Assistant")
query = st.text_input(
    "Ask a Supply Chain Question",
    placeholder="Example: List delayed orders in East region"
)

if st.button("🔍 Investigate"):
    if query.strip() == "":
        st.warning("Please enter a question.")
        st.stop()

    BACKEND_URL = os.getenv("BACKEND_URL")
    url = f"{BACKEND_URL}/chat"

    API_KEY = os.getenv("API_KEY")
    headers = {
        "x-api-key": API_KEY
    }
    payload = {
        "query": query
    }
    try:
        with st.spinner(
            "🔍 Running Multi-Agent Investigation..."
        ):
            response = requests.post(
                url,
                headers=headers,
                json=payload,
                timeout=60
            )
        if response.status_code == 200:
            result = response.json()
            st.session_state.history.append(query)
            col1, col2, col3 = st.columns(3)
            col1.metric("Documents", len(result["documents"]))
            col2.metric("Risks",len(result["risks"]))
            col3.metric("Recommendations",len(result["recommendations"]))
            st.divider()
            tab1, tab2, tab3, tab4 = st.tabs(
                [
                    "📄 Documents",
                    "⚠️ Risks",
                    "💡 Recommendations",
                    "📊 Report"
                ]
            )

            with tab1:
                st.subheader("Retrieved Documents")
                if result["documents"]:
                    for doc in result["documents"]:
                        st.success(doc)
                else:
                    st.info("No documents found.")

            with tab2:
                st.subheader("Identified Risks")
                if result["risks"]:
                    for risk in result["risks"]:
                        st.warning(risk)
                else:
                    st.info("No risks detected.")

            with tab3:
                st.subheader("Recommendations")
                if result["recommendations"]:
                    for rec in result["recommendations"]:
                        st.info(rec)
                else:
                    st.info("No recommendations generated.")

            with tab4:
                st.subheader("Executive Investigation Report")
                st.markdown(result["report"])
                st.download_button(
                    label="📥 Download Report",
                    data=result["report"],
                    file_name="investigation_report.txt",
                    mime="text/plain"
                )

        elif response.status_code == 401:
            st.error("Invalid API Key.")

        else:
            st.error(f"API Error: {response.status_code}")
            st.json(response.json())

    except requests.exceptions.ConnectionError:
        st.error(
            """
            Could not connect to FastAPI.
            Make sure this is running
            uvicorn src.api.main:app --reload
            """
        )

    except requests.exceptions.Timeout:
        st.error(
            "Request timed out."
        )

    except Exception as e:
        st.error(
            f"Error: {str(e)}"
        )

