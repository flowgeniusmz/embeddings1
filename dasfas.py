from openai import OpenAI
import streamlit as st
client = OpenAI(api_key=st.secrets.openai.api_key)

run = client.beta.threads.runs.retrieve(run_id="run_FiGZKGFr2f9XWDJZXhlHz1ud", thread_id="thread_9Innf1CvFpqrTa4tegMguds1")
print(run)
print(run.status)