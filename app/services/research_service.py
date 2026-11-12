from app.core.llm import get_llm
from app.schemas.research import ResearchResponse

def get_research_chain():
    llm=get_llm()
    structured_llm=llm.with_structured_output(
        ResearchResponse
    )

    return structured_llm

def generate_research(topic:str):
    structured_llm=get_research_chain()
    response=structured_llm.invoke(
        f"""
        Research the followiing topic:{topic}
        Provide:
        1.A clear summary
        2.Three important findings
        3.A confidenc level
        """
    )

    return response
