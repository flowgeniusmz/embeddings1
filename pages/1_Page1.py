# 0. Import Libraries
import streamlit as st
from config import pagesetup as ps

# 1. Set Page Config
app_name = "FlowGenius AI"
page_title = "FlowGenius AI"
page_subtitle = "Page 1" 
page_icon = "🌐☁️"
page_description = "Allows users to view page1."
overview_header = "Overview"
overview_text = f"**{page_subtitle}** {page_description.lower()}"

# 2. Set Page Title
ps.set_title(varTitle=page_title, varSubtitle=page_subtitle)

# 3. Set Page Overview
ps.set_page_overview(varHeader=overview_header, varText=overview_text)