import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain.schema import AIMessage, HumanMessage, SystemMessage

def check_key():
    """Returns `True` if the user had the correct api_key."""

    def key_entered():
        """Checks whether the api_key entered by the user is correct."""
        if check_api_key_usage(st.session_state["api_key"]):
            st.session_state["api_key_correct"] = True
        else:
            st.session_state["api_key_correct"] = False

    if "api_key_correct" not in st.session_state:
        # First run, show input for password.
        st.text_input(
            "Openai api key", type="password", on_change=key_entered, key="api_key"
        )
        return False
    elif not st.session_state["api_key_correct"]:
        # Password not correct, show input + error.
        st.text_input(
            "Password", type="password", on_change=key_entered, key="api_key"
        )
        st.error("😕 Password incorrect")
        return False
    else:
        # Password correct.
        return True



def check_api_key_usage(API_KEY):
    chat = ChatOpenAI(temperature=0, openai_api_key=API_KEY, model_name='gpt-3.5-turbo-0613',max_tokens=5)
    messages = [
    HumanMessage(content="return me a True"),
    ]
    try:
        result = chat(messages)
    except:
        return False
    else:
        return True


if check_password():
    st.write("Here goes your normal Streamlit app...")
    st.button("Click me")