
import streamlit as st

from agent import ask_agent
from database import get_tasks


# Page settings
st.set_page_config(
    page_title="My Personal Assistant",
    page_icon="🤖"
)


# Application heading
st.title("My Personal Assistant")

st.write("Hello! How can I help you today?")


# Store chat messages
if "messages" not in st.session_state:
    st.session_state.messages = []


# Sidebar
st.sidebar.title("My Tasks")

tasks = get_tasks()

if tasks:
    for task in tasks:
        st.sidebar.write(f"{task[0]}. {task[1]}")
        st.sidebar.caption(task[2])
else:
    st.sidebar.write("No tasks added yet.")


# Display chat history
for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.write(message["content"])


# User input
user_input = st.chat_input("Type your message...")


if user_input:

    # Display user message
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    with st.chat_message("user"):
        st.write(user_input)


    # Get assistant response
    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):
            response = ask_agent(user_input)

            st.write(response)


    # Store assistant response
    st.session_state.messages.append({
        "role": "assistant",
        "content": response
    })


    # Refresh task list
    st.rerun()
