from langgraph.graph import StateGraph,START,END
from app.workflows.research_state import ResearchState

from app.workflows.nodes import(
    research_node,
    analysis_node,
    response_node
)

def create_research_workflow():
    graph_builder=StateGraph(ResearchState)

    graph_builder.add_node("research",research_node)
    graph_builder.add_node("analysis",analysis_node)
    graph_builder.add_node("response",response_node)

    graph_builder.add_edge(START,"research")
    graph_builder.add_edge("research","analysis")
    graph_builder.add_edge("analysis","response")
    graph_builder.add_edge("response",END)

    work_flow=graph_builder.compile()

    return work_flow