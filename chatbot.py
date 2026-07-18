from dotenv import load_dotenv
import os

from typing import Annotated
from typing_extensions import TypedDict

from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage

from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from langgraph.checkpoint.memory import MemorySaver

# Load environment variables
load_dotenv()

# Initialize LLM
llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key=os.getenv("GROQ_API_KEY")
)

# Define State
class ChatState(TypedDict):
    messages: Annotated[list, add_messages]

# Chatbot Node
def chatbot(state: ChatState):
    response = llm.invoke(state["messages"])
    return {
        "messages": [response]
    }

# Build Graph
graph = StateGraph(ChatState)

graph.add_node("chatbot", chatbot)

graph.add_edge(START, "chatbot")
graph.add_edge("chatbot", END)

# Add Memory
memory = MemorySaver()

# Compile Graph
app = graph.compile(checkpointer=memory)

# Configuration
config = {
    "configurable": {
        "thread_id": "1"
    }
}

# Chat Loop
while True:
    user_input = input("\nYou: ")

    if user_input.lower() in ["exit", "quit"]:
        break

    result = app.invoke(
        {
            "messages": [HumanMessage(content=user_input)]
        },
        config=config
    )

    print("\nAI:", result["messages"][-1].content)