# 0. Import Libraries
import streamlit as st
from config import pagesetup as ps
from openai import OpenAI
import time
from app import chat

# 1. Set Page Config
app_name = "Dean's Assistant"
page_title = "Dean's Assistant"
page_subtitle = "John F Kennedy Middle School" 
page_icon = "🎓"
page_description = "Allows users to view page1."
overview_header = "Overview"
overview_text = f"**{page_subtitle}** {page_description.lower()}"

# 2. Set Page Title
titlecontainer = st.container()
with titlecontainer:
    cc = st.columns(2)
    with cc[0]:
        ps.set_title_nodiv(varTitle=page_title
                           varSubtitle=page_subtitle)
    with cc[1]:
        st.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQroYsyWjvZmkyguxf2_XUKqcWTNLkZrRbPzPL8MU5I&s', caption='Plainfield School District 202') #Streamlit image for branding
st.divider()

# 3. Set Page Overview
ps.set_page_overview(varHeader=overview_header, varText=overview_text)

chat_container = st.container(border=True)
with chat_container:
    chat.app_chat()
