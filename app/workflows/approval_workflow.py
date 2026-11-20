from langgraph.graph import StateGraph,START,END
from langgraph.checkpoint.memory import MemorySaver

from app.workflows.approval_state import ApprovalState

from app.workflows.approval_nodes import (
    approval_node,
    execute_action_node,
    reject_action_node,
    route_after_approval
)

def create_approval_workflow():

    graph_builder=StateGraph(ApprovalState)
    
    graph_builder.add_node("approval",approval_node)
    graph_builder.add_node("execute",execute_action_node)
    graph_builder.add_node("reject",reject_action_node)

    graph_builder.add_edge(START,"approval")
    graph_builder.add_conditional_edges(
        "approval",
        route_after_approval,
        {
            "execute":"execute",
            "reject":"reject"
        }
    )

    graph_builder.add_edge("execute",END)
    graph_builder.add_edge("reject",END)

    memory=MemorySaver()
    workflow=graph_builder.compile(
        checkpointer=memory
    )

    return workflow

