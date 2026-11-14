from app.workflows.research_state import ResearchState

def test_research_state():
    state:ResearchState={
        "question":"What is Generative AI",
        "research_results":[],
        "analysis":"",
        "final_answer":""
    }

    print("\nInitial state:")
    print(state)

    state["research_results"]=[
        "Generative AI creates new content",
        "It uses machine learning models"
    ]

    state["analysis"]=(
        "Generative AI can generate text,images"
        "audio and other types of content"
    )

    state["final_answer"]=(
        "Generative Ai is a type of a artificial intelligence"
        "that generates new content"
    )

    print("Updated State")
    print(state)

if __name__=="__main__":
    test_research_state()

