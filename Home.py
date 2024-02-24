# 0. Import Libraries
import streamlit as st
from config import pagesetup as ps
from openai import OpenAI
import time

# 1. Set Page Config
app_name = "FlowGenius AI"
page_title = "FlowGenius AI"
page_subtitle = "Page 2" 
page_icon = "🌐☁️"
page_description = "Allows users to view page1."
overview_header = "Overview"
overview_text = f"**{page_subtitle}** {page_description.lower()}"

# 2. Set Page Title
ps.set_title(varTitle=page_title, varSubtitle=page_subtitle)

# 3. Set Page Overview
ps.set_page_overview(varHeader=overview_header, varText=overview_text)

# 4. Set Instances
client = OpenAI(api_key=st.secrets.openai.api_key)

# 5. Set Session State
if "assistant_id" not in st.session_state:
    st.session_state.assistant_id = st.secrets.openai.assistant_key_3
if "thread_id" not in st.session_state:
    st.session_state.thread_id = client.beta.threads.create().id
if "messages" not in st.session_state:
    st.session_state.messages=[]

st.chat_message("assistant").markdown("How may I help you today?")
                                      


if prompt := st.chat_input("Enter a question (ex:  A student just had his third tardy. What consequences should I consider?)"):
    new_msg = {"role": "user", "content": prompt}
    #st.chat_message("user").markdown(prompt)
    st.session_state.messages.append(new_msg)
    new_thread_msg = client.beta.threads.messages.create(
        thread_id=st.session_state.thread_id,
        role="user",
        content=prompt
    )
    run = client.beta.threads.runs.create(
        thread_id=st.session_state.thread_id,
        assistant_id=st.session_state.assistant_id
    )
    while run.status=="in_progress" or run.status=="queued":
        time.sleep(1)
        run = client.beta.threads.runs.retrieve(
            run_id=run.id,
            thread_id=st.session_state.thread_id
        )
        if run.status=="completed":
            message_list = client.beta.threads.messages.list(
                thread_id=st.session_state.thread_id,
                order="desc"
            )
            message_data = message_list.data[0]
            print(message_data)
            message_content = message_data.content[0]
            message_text = message_content.text
            message_value = message_text.value
            response_message = {"role": "assistant", "content": message_value}
            st.session_state.messages.append(response_message)
            for msgs in st.session_state.messages:
                role = msgs.role
                content = msgs.content
                with st.chat_message(role):
                    st.markdown(content)
