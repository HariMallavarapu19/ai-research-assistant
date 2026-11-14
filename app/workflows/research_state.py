from typing import TypedDict,List

class ResearchState(TypedDict):
    question:str
    research_results:List[str]
    analysis:str
    final_answer:str
