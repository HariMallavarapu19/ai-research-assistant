from app.workflows.research_workflow import route_after_research

def test_route_to_analysis():
    state={
        
        "question":"What is Generative AI",
        "research_results":["Generative  AI creates new contetn"],
        "analysis":"",
        "final_answer":""                  
        
    }

    result =route_after_research(state)

    assert result=="analysis"

def test_route_to_no_results():
    state={
        "question": "What is Generative AI?",
        "research_results": [],
        "analysis": "",
        "final_answer": ""
    }

    result =route_after_research(state)
    assert result=="no_results"

