from app.workflows.research_workflow import create_research_workflow

def test_research_workflow():
    workflow=create_research_workflow()
    initial_state={
        "question": "What is Generative AI?",
        "research_results": [],
        "analysis": "",
        "final_answer": ""
    }

    result=workflow.invoke(initial_state)
    print("\nFinal Research Answer:")
    print(result["final_answer"])

    print("\nFinal Workflow State:")
    print(result)


if __name__ == "__main__":
    test_research_workflow()