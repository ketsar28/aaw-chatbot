import os
import json
import streamlit as st
import openai

# configuring openai - api key
work_dir = os.path.dirname(os.path.abspath(__file__))
config_data = json.load(open(f'{work_dir}/config.json'))
OPENAI_API_KEY = config_data["OPENAI_API_KEY"]
openai.api_key = OPENAI_API_KEY

# configuring streamlit page settings
st.set_page_config(
    page_title="ChatGPT 4o - AAW",
    page_icon="💬",
    layout="centered"
)

# initialization chat session in streamlit if it does not exist yet
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# title of page
st.title("🤖 AAW ChatGPT 4o")

# display chat history
for message in st.session_state.chat_history:
    with st.chat_message(message['role']):
        st.markdown(message['content'])

# input field for user's message
user_prompt = st.chat_input("Ask AAW ChatGPT-4o...")

if user_prompt:
    # add user prompt and display it
    st.chat_message('user').markdown(user_prompt)
    st.session_state.chat_history.append({"role": "user", "content": user_prompt})

    # send user's message to AAW ChatGPT-4o and get a response
    response = openai.chat.completions.create(
        model='gpt-3.5-turbo',
        messages=[
            {"role":"system","content": "you are a helpful assistant!"},
            *st.session_state.chat_history
        ]
    )

    assistant_response = response.choices[0].message.content
    st.session_state.chat_history.append({"role":"assistant", "content":assistant_response})

    # display AAW ChatGPT-4o response
    with st.chat_message('assistant'):
        st.markdown(assistant_response)
