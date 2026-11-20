from app.workflows.conversation_workflow import(
    create_conversation_workflow
)

conversation_workflow=create_conversation_workflow()

def chat(message:str,thread_id:str):
    config={
        "configurable":{
            "thread_id":thread_id
        }
    }

    response=conversation_workflow.invoke(
        {
            "messages":[
                {
                    "role":"user",
                    "content":message
                }
            ]
        },
        config=config
    )

    return response["messages"][-1].content

 