from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import MessagesState
from langchain.messages import AIMessage


def mock_chatbot(state: MessagesState):

    # Count the messages received by this node
    message_count = len(state["messages"])

    return {
        "messages": [
            AIMessage(
                content=f"I received {message_count} messages."
            )
        ]
    }


def create_test_graph():

    builder = StateGraph(MessagesState)

    builder.add_node("chatbot", mock_chatbot)

    builder.add_edge(START, "chatbot")
    builder.add_edge("chatbot", END)

    memory = MemorySaver()

    return builder.compile(checkpointer=memory)


def test_checkpoint_memory():

    graph = create_test_graph()

    config = {
        "configurable": {
            "thread_id": "memory_test_001"
        }
    }

    # First conversation turn
    first_result = graph.invoke(
        {
            "messages": [
                {"role": "user", "content": "Hello"}
            ]
        },
        config=config
    )

    print("\nFirst turn:")
    print(first_result["messages"])

    # Second turn, same thread
    second_result = graph.invoke(
        {
            "messages": [
                {"role": "user", "content": "How are you?"}
            ]
        },
        config=config
    )

    print("\nSecond turn:")
    print(second_result["messages"])

    # First turn had 1 user message
    assert first_result["messages"][-1].content == "I received 1 messages."

    # Second turn should have the first turn's messages
    # plus the new user message.
    assert second_result["messages"][-1].content == "I received 3 messages."

    print("\nCheckpoint memory test passed!")


if __name__ == "__main__":
    test_checkpoint_memory()