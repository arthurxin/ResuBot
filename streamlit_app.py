import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain.schema import AIMessage, HumanMessage, SystemMessage
from streamlit_features import main
from tempfile import TemporaryDirectory

def check_key():
    """Returns `True` if the user had the correct api_key."""

    def key_entered():
        """Checks whether the api_key entered by the user is correct."""
        if st.session_state["api_key"] == "free-trail":
            st.session_state["api_key"] = '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'
            st.session_state["api_key_correct"] = True
        elif check_api_key_valid(st.session_state["api_key"]):
            st.session_state["api_key_correct"] = True
        else:
            st.session_state["api_key_correct"] = False

    if "api_key_correct" not in st.session_state:
        # First run, show input for password.
        st.write("Input your openai key to use the resume adapt agent, or inpur free-trail to try it free.")
        st.text_input("Input your openai key to use the resume adapt agent, or inpur free-trail to try it free.",
            "", type="password", on_change=key_entered, key="api_key"
        )
        return False
    elif not st.session_state["api_key_correct"]:
        # Password not correct, show input + error.
        st.text_input(
            "Openai api key", type="password", on_change=key_entered, key="api_key"
        )
        st.error("😕 Password incorrect")
        return False
    else:
        # Password correct.
        return True



def check_api_key_valid(API_KEY):
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
    
st.header("ResuBot")
st.subheader("revising user's resume to match the requirements and expectations of a specific job website url")
st.text("1.upload your resume")
st.text("2.input job website url")
st.text("3.click generate")
st.text("4.download")
st.text("")

# if check_key():
#     with TemporaryDirectory() as user_path:
#         main(st.session_state["api_key"],user_path)

with TemporaryDirectory() as user_path:
    st.session_state["api_key"] = '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'
    main(st.session_state["api_key"],user_path)