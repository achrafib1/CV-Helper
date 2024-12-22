# # main app file
# from cv_helper_agents.crew import CvHelper
import warnings

# warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# CvHelper_crew = CvHelper()
# while True:
#     user_input = input("Please enter your input (or type 'exit' to quit):\n user:  ")
#     if user_input.lower() == "exit":
#         print("Exiting the chat. Goodbye!")
#         break
#     user_input_dict = {"user_input": user_input}
#     res = CvHelper_crew.crew().kickoff(inputs=user_input_dict)
#     print(f"Output:\n agent:  {res}")

from cv_helper_agents.crew import CVHelper
from mem0 import Memory
from dotenv import load_dotenv

load_dotenv()

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


def run():
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit", "bye"]:
            print("Chatbot: Goodbye! It was nice talking to you.")
            break

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
        print(f"Assistant: {response}")

run()