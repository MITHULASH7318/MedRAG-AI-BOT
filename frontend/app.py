import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/query"

st.set_page_config(page_title="MedRAG AI", page_icon="🧠")

st.title("🧠 MedRAG - Medical AI Assistant")

user_query = st.text_input("Enter your medical question:")

if st.button("Ask AI"):
    if user_query.strip() == "":
        st.warning("Please enter a question")
    else:
        with st.spinner("Searching research papers..."):
            try:
                response = requests.post(
                    API_URL,
                    json={"question": user_query}
                )

                data = response.json()

                st.subheader("Answer")
                st.write(data["answer"])

                if "sources" in data:
                    st.subheader("Sources")
                    for src in data["sources"]:
                        st.write("-", src["text"])

            except Exception as e:
                st.error(f"Error: {e}")