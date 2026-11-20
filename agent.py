
import os

from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain.agents import create_agent

from tools import add_task, view_tasks, delete_task


# Load environment variables
load_dotenv()

# Get API key
api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError("Groq API key not found. Check your .env file.")


# Connect to Groq model
llm = ChatGroq(
    model="openai/gpt-oss-20b",
    api_key=api_key,
    temperature=0.7
)


# Register tools
tools = [
    add_task,
    view_tasks,
    delete_task
]


# Create AI agent
agent = create_agent(
    model=llm,
    tools=tools,
    system_prompt=(
        "You are a helpful personal assistant. "
        "Help users manage their daily tasks. "
        "Use the available tools whenever the user "
        "asks to add, view, or delete tasks. "
        "Always explain the result clearly. "
        "When deleting tasks, use the correct task ID."
    )
)


# Function to communicate with AI agent
def ask_agent(user_input):

    response = agent.invoke({
        "messages": [
            {"role": "user", "content": user_input}
        ]
    })

    return response["messages"][-1].content


# Run terminal chatbot only when this file
# is executed directly
if __name__ == "__main__":

    user_input = input("You: ")

    answer = ask_agent(user_input)

    print("\nAI Assistant:", answer)

