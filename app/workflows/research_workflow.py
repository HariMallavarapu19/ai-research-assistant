from langgraph.graph import StateGraph,START,END
from app.workflows.research_state import ResearchState

from app.workflows.nodes import(
    research_node,
    analysis_node,
    response_node,
    no_results_node
)

def route_after_research(state:ResearchState):
    """Decide which node should execute after research"""
    if state["research_results"]:
        return "analysis"
    return "no_results"


def create_research_workflow():
    graph_builder=StateGraph(ResearchState)

    graph_builder.add_node("research",research_node)
    graph_builder.add_node("analysis",analysis_node)
    graph_builder.add_node("response",response_node)
    graph_builder.add_node("no_results",no_results_node)

    graph_builder.add_edge(START,"research")
    graph_builder.add_conditional_edges(
        "research",
        route_after_research,{
            "analysis":"analysis",
            "no_results":"no_results"
        }
    )
    graph_builder.add_edge("analysis","response")
    graph_builder.add_edge("response",END)
    graph_builder.add_edge("no_results",END)

    work_flow=graph_builder.compile()

    return work_flow