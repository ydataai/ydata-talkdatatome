"""

"""
import asyncio
from contextlib import contextmanager

import aiohttp
import streamlit as st
from streamlit_pandas_profiling import st_profile_report

from streamlit_chat import message

import pandas as pd
from pandas_profiling import ProfileReport

# Create a context manager to run an event loop
@contextmanager
def setup_event_loop():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    try:
        yield loop
    finally:
        loop.close()
        asyncio.set_event_loop(None)

def upload_file():
    """Upload a CSV dataset"""
    df = None

    st.subheader("1. Select your dataset")
    uploaded_file = st.file_uploader("Choose a file:")

    if uploaded_file is not None:
      df = pd.read_csv(uploaded_file, sep=';')
    return df

def generate_profile(df: pd.DataFrame):
    """Generate the profiling"""
    profile = ProfileReport(df, title='Data Profiling', interactions=None)
    st_profile_report(profile)
    return profile.to_json()

def ask_questions(df: pd.DataFrame, text: str):
    import sketch
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
            # Use the context manager to create an event loop
            with setup_event_loop() as loop:
                user_input=None
                import sketch

                user_input = st.text_input('What is your question?')

                if user_input:
                    response = st.text(df.sketch.ask(user_input, call_display=False))


if __name__ == '__main__':
    run()