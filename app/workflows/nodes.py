from app.workflows.research_state import ResearchState

def research_node(state:ResearchState):
    print("\n Executingn  Research Node......")
    research_results=[
        "Generative AI creates new content",
        "It uses machine learning models",
        "It can generate text,images,audio and videos"
    ]

    return {
        "research_results":research_results
    }

def analysis_node(state:ResearchState):
    print("\nExecuting Analysis Node....")
    results=state["research_results"]
    analysis=(
        "The research indicates that Generative AI "
        "uses machine learning models to generate "
        "different types of content."
    )

    return {
        "analysis":analysis
    }

def response_node(state:ResearchState):
    print("\nExecuting Response Node....")
    final_answer=(
        f"Your question: {state['question']}\n\n"
        f"Research findings: {state['research_results']}\n\n"
        f"Analysis: {state['analysis']}"
    )

    return {
        "final_answer":final_answer
    }

    
def no_results_node(state:ResearchState):
    print("\nExecuting No Results Node")

    return {
        "final_answer":(
        "Sorry no research Results were found for your question")
    }
