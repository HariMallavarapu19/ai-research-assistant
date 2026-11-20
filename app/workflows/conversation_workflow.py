from langgraph.graph import StateGraph,START,END
from langgraph.checkpoint.memory import MemorySaver

from app.workflows.conversation_state import ConversationState
from app.core.llm import get_llm

def chatbot_node(state:ConversationState):
    print("\nExecuting Chatbot Node....")
    llm=get_llm()
    response=llm.invoke(state['messages'])
    return {
        "messages":[response]
    }

def create_conversation_workflow():
    graph_builder=StateGraph(ConversationState)

    graph_builder.add_node("chatbot",chatbot_node)

    graph_builder.add_edge(START,"chatbot")
    graph_builder.add_edge("chatbot",END)

    memory=MemorySaver()

    workflow=graph_builder.compile(checkpointer=memory)

    return workflow




