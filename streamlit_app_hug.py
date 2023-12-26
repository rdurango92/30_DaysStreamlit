import streamlit as st
import pandas as pd

# Import for API calls
import requests

# Import for navbar
from streamlit_option_menu import option_menu

# Import for dynamic tagging
from streamlit_tags import st_tags, st_tags_sidebar

# Imports for aggrid
from st_aggrid import AgGrid
from st_aggrid.grid_options_builder import GridOptionsBuilder
from st_aggrid.shared import JsCode
from st_aggrid import GridUpdateMode, DataReturnMode

# Import for loading interactive keyboard shortcuts into the app
from dashboard_utils.gui import keyboard_to_url
from dashboard_utils.gui import load_keyboard_class

# -----------------------------------------------------------

# The code below is to control the layout width of the app.
if "widen" not in st.session_state:
    layout = "centered"
else:
    layout = "wide" if st.session_state.widen else "centered"

st.set_page_config(layout=layout, page_title="Zero-Shot Text Classifier", page_icon="🤗")

# -----------------------------------------------------------

# The class below is for adding some formatting to the shortcut button on the left sidebar.
load_keyboard_class()

# -----------------------------------------------------------

# The block of code below is to display the title, logos and introduce the app.
c1, c2 = st.columns([0.4, 2])
with c1:

    st.image(
        "logo.png",
        width=110,
    )
with c2:

    st.caption("")
    st.title("Zero-Shot Text Classifier")

st.sidebar.image(
    "30days_logo.png",
)

st.write("")
st.markdown(
    """

Classify keyphrases fast and on-the-fly with this mighty app. No ML training needed!

Create classifying labels (e.g. `Positive`, `Negative` and `Neutral`), paste your keyphrases, and you're off!  

"""
)
st.write("")
st.sidebar.write("")