import calendar
from datetime import datetime
import streamlit as st
import pandas as pd

st.write("""
# Expense Tracker App

Try this absolutely innovative app!

""")

page_title = "Expense Tracker App"
layout = "centered"

st.set_page_config(page_title = page_title, layout=layout)
st.title(page_title)
