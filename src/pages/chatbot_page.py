import streamlit as st
from cv_helper_agents.crew import CVHelper
from dotenv import load_dotenv
import os
from mem0 import Memory
import asyncio

st.set_page_config(page_title="chatbot_page", layout="wide")
st.markdown(
        "<style>  ul[data-testid=stSidebarNavItems]  {display: none;} </style>",
        unsafe_allow_html=True,
    )

load_dotenv()

# Load Environment Variables

config = {
    "api_version": "v1.1",
    "vector_store": {
        "provider": "chroma",
        "config": {
            "collection_name": "chatbot_memory",
            "path": "./chroma_db",
        },
    },
}

memory = Memory.from_config(config)


# Initialize session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []


async def run_chatbot(user_input):
    """Runs the chatbot and returns the response."""
    with st.spinner("Generating Response..."):
        # Add user input to memory
        memory.add(f"User: {user_input}", user_id="Lennex")

        # Retrieve all user and assistant messages for the current conversation
        user_messages = memory.get_all(user_id="Lennex")
        assistant_messages = memory.get_all(user_id="Assistant")

        # Combine and format context from both user and assistant memories
        context = "\\n".join([message["memory"] for message in user_messages] + [message["memory"] for message in assistant_messages])

        inputs = {
            "user_message": f"{user_input}",
            "context": f"{context}",
        }
        response = CVHelper().crew().kickoff(inputs=inputs)

        # Add chatbot response to memory
        memory.add(f"Assistant: {response}", user_id="Assistant")
        return response



st.title("CV Helper Chatbot")

# Display Chat History
for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Get user input
if prompt := st.chat_input("Type your message here..."):
    st.session_state.chat_history.append({"role": "user", "content": prompt})

    # Get the chatbot response
    response = asyncio.run(run_chatbot(prompt))

    # Append chatbot's response to chat history
    st.session_state.chat_history.append({"role": "assistant", "content": response})
    # Display Chat History
    for message in st.session_state.chat_history:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])