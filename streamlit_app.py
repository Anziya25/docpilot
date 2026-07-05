import mimetypes
import requests
import streamlit as st

API_URL = "http://127.0.0.1:8000"

st.set_page_config(
    page_title="Enterprise Document Intelligence",
    page_icon="📚",
    layout="wide"
)

st.title("📚 Enterprise Document Intelligence Platform")

st.markdown("---")

# ==================================================
# Upload Documents
# ==================================================

st.header("Upload Documents")

uploaded_file = st.file_uploader(
    "Choose a document",
    type=["pdf", "txt", "docx"]
)

if uploaded_file is not None:

    if st.button("Upload Document"):

        mime_type = (
            mimetypes.guess_type(uploaded_file.name)[0]
            or "application/octet-stream"
        )

        files = {
            "file": (
                uploaded_file.name,
                uploaded_file,
                mime_type,
            )
        }

        response = requests.post(
            f"{API_URL}/upload",
            files=files,
        )

        if response.status_code == 200:

            st.success("Document uploaded successfully!")

            st.json(response.json())

        else:

            st.error(response.text)

st.markdown("---")

# ==================================================
# Build Vector Store
# ==================================================

st.header("Build Knowledge Base")

if st.button("Build Vector Store"):

    response = requests.post(
        f"{API_URL}/index"
    )

    if response.status_code == 200:

        st.success("Knowledge Base Built Successfully!")

        st.json(response.json())

    else:

        st.error(response.text)

st.markdown("---")

# ==================================================
# Ask Questions
# ==================================================

st.header("Ask Questions")

question = st.text_input(
    "Enter your question"
)

if st.button("Ask"):

    if question.strip() == "":

        st.warning("Please enter a question.")

    else:

        response = requests.post(
            f"{API_URL}/chat",
            json={
                "question": question
            }
        )

        if response.status_code == 200:

            result = response.json()

            st.subheader("Answer")

            st.write(result["answer"])

            st.subheader("Sources")

            for source in result["sources"]:
                st.json(source)

        else:

            st.error(response.text)