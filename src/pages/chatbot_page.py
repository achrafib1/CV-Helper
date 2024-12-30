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


async def get_chatbot_response(user_input):
    """Retrieves a response from the chatbot based on user input."""
    try:
        # Add user input to memory
        memory.add(f"User: {user_input}", user_id="Lennex")

        # Retrieve context from memory
        context = get_context_for_response(user_input)

        # Prepare input for CrewAI
        inputs = {"user_message": user_input, "context": context}

        # Get the response
        response = CVHelper().crew().kickoff(inputs=inputs)

        # Add chatbot response to memory
        memory.add(f"Assistant: {response}", user_id="Assistant")
        return response

    except Exception as e:
        st.error(f"An error occurred: {e}")
        return "Oops, something went wrong. Please try again."


def get_context_for_response(user_input, k=3):
    """Retrieves the appropriate context for the response.
    It retrieves  messages from user and assistant chats along with relevant context for the user input
    """
    # Retrieve latest messages
    user_messages = memory.get_all(user_id="Lennex")
    assistant_messages = memory.get_all(user_id="Assistant")

    # Format and Combine the Context messages from user and assistant
    formatted_messages = []
    for message in user_messages:
        formatted_messages.append(f"User: {message['memory']}")
    for message in assistant_messages:
        formatted_messages.append(f"Assistant: {message['memory']}")
    context = "\n".join(formatted_messages)

    return context


async def run_chatbot(user_input):
    """Runs the chatbot and returns the response."""
    with st.spinner("Generating Response..."):
        response = await get_chatbot_response(user_input)
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
