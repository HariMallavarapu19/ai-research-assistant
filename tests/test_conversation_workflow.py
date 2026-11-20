from app.services.conversation_service import chat

def test_conversation_memory():
    thread_id="test_conversation_001"

    first_response=chat(
        "my name is hari, remember it",
        thread_id
    )

    print(first_response)

    second_response=chat(
        "what is my name",thread_id
    )

    print(second_response)

    assert "alex" in second_response.lower()