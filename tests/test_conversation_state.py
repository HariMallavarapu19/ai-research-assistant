from app.workflows.conversation_state import ConversationState

def test_conversation_state():
    state:ConversationState={
        "messages":[
            {
                "role":"user",
                "content":"What is Generative AI"
            }, 
            {
                "role":"assistant",
                "content":"Generative AI creates  new content"
            }
        ]
    }

    assert len(state['messages'])==2

    print('\nConversation State')
    print(state)

if __name__=="__main__":
    test_conversation_state()

