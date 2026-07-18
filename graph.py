from typing import Annotated
from typing_extensions import TypedDict

from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from langgraph.checkpoint.memory import MemorySaver

from llm import llm


class ChatState(TypedDict):
    messages: Annotated[list, add_messages]


def chatbot(state: ChatState):
    response = llm.invoke(state["messages"])
    return {"messages": [response]}


graph = StateGraph(ChatState)

graph.add_node("chatbot", chatbot)
graph.add_edge(START, "chatbot")
graph.add_edge("chatbot", END)

memory = MemorySaver()

app_graph = graph.compile(checkpointer=memory)