"""from app.core.llm import get_llm

def main():
    print("Connecting to gemini")
    llm=get_llm()
    print("Sending request to llm")
    response=llm.invoke(
        "Explain what an ai research assistant does in two sentences"
    )
    print("0Gemini Response")

    if isinstance(response.content,list):
        for item in response.content:
            if item.get("type")=='text':
                print(item['text'])
    else:
        print(response.content)

if __name__=="__main__":
    main()

from app.services.research_service import generate_research

def main():
    topic="AI Agents"
    print("Starting research....")
    result=generate_research(topic)

    print("Topic",result.topic)
    print("Summary",result.summary)
    print("\nKey Findings")
    for finding in result.key_findings:
        print("-",finding)

    print("\nConfidence:",result.confidence)


if __name__=="__main__":
    main()"""

from app.services.search_service import search_web

def main():
    query="Latest developments in ai agents"
    print("Searching the web")
    results=search_web(query)
    print(results)

if __name__=="__main__":
    main()