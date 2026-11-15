import json
from app.core.llm import get_llm
from app.workflows.research_state import ResearchState
from app.tools.search_tool import get_search_tool


def extract_text(response):
    """Extract readable text from an LLM response
    Handles both string and content block responses"""

    content=response.content
    if isinstance(content,str):
        return content
    if isinstance(content,list):
        text_parts=[]
        for block in content:
            if isinstance(block,dict) and block.get("type")=="text":
                text_parts.append(block.get("text",""))

        return "\n".join(text_parts)

    return str(content)

def research_node(state:ResearchState):
    print("\n Executingn  Research Node......")
    search_tool=get_search_tool()
    results=search_tool.invoke({
        "query":state['question']
    })

    if isinstance(results,dict):
        raw_results=results.get("results",[])
        research_results=[]
        for item in raw_results:
            if isinstance(item,dict):
                research_results.append(
                    f"Title:{item.get('title','N/A')}\n"
                    f"URL:{item.get('url','N/A')}\n"
                    f"Content:{item.get('content','')}"
                )


        if not research_results and results.get("answer"):
            research_results.append(results["answer"])

    elif isinstance(results,list):
        research_results=[
            str(item) for item in results
        ]
              
    else:
        research_results=[str(results)] if results else []

    print(f"Research results collecteed:{len(research_results)}")

    return {
        "research_results":research_results
    }
    


def analysis_node(state:ResearchState):
    print("\nExecuting Analysis Node....")
    llm=get_llm()
    research_data="\n\n".join(
        state['research_results']
    )

    prompt=f"""
    You are an expert research analyst 
    User question:
    {state['question']}
    Research information:
    {research_data}
    Analyze the research information.

    Identify:
    1. The most important findings.
    2. Important facts and patterns.
    3. Any conflicting or uncertain information.
    4. What information directly answers the question.

    Do not invent facts that are not supported by the research.
    """

    response=llm.invoke(prompt)
    analysis=extract_text(response)
    return {
        "analysis":analysis
    }
    
def response_node(state:ResearchState):
    print("\nExecuting Response Node....")
    llm=get_llm()
    prompt=f"""
    YOu are an AI research assistant

    user question:
    {state['question']}

    Research results:
    {state['research_results']}
     
     Generate a clear, accurate and well-structured answer.

    Requirements:
    1. Answer the user's original question.
    2. Use the supplied research information.
    3. Do not invent facts.
    4. Include relevant source URLs from the research results.
    5. Mention uncertainty when necessary.
    """

    response=llm.invoke(prompt)
    final_answer=extract_text(response)
    return {
        "final_answer":final_answer
    }
def no_results_node(state:ResearchState):
    print("\nExecuting No Results Node")

    return {
        "final_answer":(
        "Sorry no research Results were found for your question")
    }
