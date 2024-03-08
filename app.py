import ai
import streamlit as st
from streamlit_chat import message
from dotenv import load_dotenv

load_dotenv(".env")

chat_placeholder = st.empty()

st.session_state.setdefault('user', [])
st.session_state.setdefault('bot', [])

def on_input_change():
    user_input = st.session_state.user_input
    if user_input.strip():
        st.session_state.user.append(user_input)
        bot_answer = ai.send_question(user_input)
        st.session_state.bot.append(bot_answer)

def on_btn_click():
    del st.session_state.past[:]
    del st.session_state.generated[:]

st.title("Chat placeholder")

with chat_placeholder.container():
    st.button("Clear message", on_click=on_btn_click)
    for i in range(len(st.session_state['user'])):
        message(st.session_state['user'][i], is_user=True, key=f"{i}_user")
        message(st.session_state['bot'][i], key=f"{i}")

with st.container():
    st.text_input("User Input:",  on_change=on_input_change, key="user_input")
