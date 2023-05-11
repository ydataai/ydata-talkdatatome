"""

"""
import streamlit as st
from streamlit_pandas_profiling import st_profile_report

from streamlit_chat import message


import pandas as pd
from pandas_profiling import ProfileReport

def upload_file():
    """Upload a CSV dataset"""
    df = None

    st.subheader("1. Select your dataset")
    uploaded_file = st.file_uploader("Choose a file:")

    if uploaded_file is not None:
      df = pd.read_csv(uploaded_file)
    return df

def generate_profile(df: pd.DataFrame):
    """Generate the profiling"""
    profile = ProfileReport(df, title='Data Profiling', interactions=None)
    st_profile_report(profile)
    return profile.to_json()

def ask_questions(df: pd.DataFrame, text: str):
    answer = df.sketch.ask(text)
    return answer

def run():

    df = upload_file()

    tab1, tab2, tab3 = st.tabs(["🗃 Data", "📈 Profiling", "🗣️ Talk data to me!"])

    if df is not None:
        profile=None

        with tab1:
            st.dataframe(df)

        with tab2:
            profile = generate_profile(df)

        with tab3:
            if profile:
                # container for chat history
                response_container = st.container()
                # container for text box
                container = st.container()

                with st.form(key='my_form', clear_on_submit=True):
                    user_input = st.text_area("You:", key='input', height=100)
                    submit_button = st.form_submit_button(label='Send')

                    if user_input:
                        response = df.sketch.ask(user_input)

if __name__ == '__main__':
    run()