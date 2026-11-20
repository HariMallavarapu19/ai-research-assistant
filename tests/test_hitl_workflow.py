from langgraph.types import Command

from app.workflows.approval_workflow import create_approval_workflow


def test_approval_workflow():
    workflow=create_approval_workflow()
    config={
        "configurable":{
            "thread_id":"approval_test_001"
        }
    }

    initial_state={
        "action":"Delete old project files",
        "approval_status":"",
        "result":""
    }

    paused_result=workflow.invoke(
        initial_state,
        config=config
    )

    print(paused_result)
    final_result=workflow.invoke(
        Command(resume="approved"),
        config=config
    )

    print(final_result)

    assert final_result['approval_status']=="approved"
    assert "Action executed" in final_result['result']

def test_rejection_workflow():

    workflow = create_approval_workflow()

    config = {
        "configurable": {
            "thread_id": "approval_test_002"
        }
    }

    initial_state = {
        "action": "Delete old project files",
        "approval_status": "",
        "result": ""
    }

    paused_result = workflow.invoke(
        initial_state,
        config=config
    )

    final_result = workflow.invoke(
        Command(resume="rejected"),
        config=config
    )

    print("\nRejected workflow:")
    print(final_result)

    assert final_result["approval_status"] == "rejected"
    assert "Action rejected" in final_result["result"]
if __name__=="__main__":
    test_rejection_workflow()