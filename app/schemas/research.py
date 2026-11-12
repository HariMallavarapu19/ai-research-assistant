from pydantic import BaseModel,Field
from typing import List,Literal

class ResearchResponse(BaseModel):
    topic:str=Field(
        description="The main research topic"
    )

    summary:str=Field(
        description="A short summary of the research"
    )

    key_findings:List[str]=Field(
        description="Important findings from the research"
    )

    confidence:Literal['low','medium','high']=Field(
        description='Confidene level of the response'
    )