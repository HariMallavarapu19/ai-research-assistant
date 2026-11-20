from langgraph.types import interrupt
from app.workflows.approval_state import ApprovalState

def approval_node(state:ApprovalState):
    print("\nWaiting for human approval...")
    decision=interrupt(
        {
            "action":state['action'],
            "message":"Approve or reject this action"
        }
    )

    return {
        "approval_status":decision
    }

def execute_action_node(state:ApprovalState):
    print("\nExecuting approved action...")

    return {
        "result":f"Action executed;{state['action']}"
    }

def reject_action_node(state:ApprovalState):
    print("\nAction rejected")

    return {
        "result":f"Action rejected:{state['action']}"
    }

def route_after_approval(state:ApprovalState):
    if state["approval_status"]=="approved":
        return "execute"
    return "reject"