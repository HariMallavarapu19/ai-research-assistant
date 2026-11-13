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
    main()

from app.services.search_service import search_web

def main():
    query="Latest developments in ai agents"
    print("Searching the web")
    results=search_web(query)
    print(results)

if __name__=="__main__":
    main()

from app.services.tool_service import research_with_tools

def main():
    print("AI research assistant")
    while True:
          query=input("What would you like to search")
          if query.lower()=='exit':
               break
          try:
              result=research_with_tools(query)
              print("Researching...")
  
              print(result)

          except Exception as error:
              print(f"\nSomething went wrong:{error}")

if __name__=="__main__":
    main()"""

from app.agents.research_agent import run_research_agent

def main():
    print("AI Research Assistant-Agent Mode")
    while True:
        query=input("\n Ask you question(or type exit)")
        if query.lower()=="exit":
            print("GOOD BYE")
            break
        try:
            result=run_research_agent(query)
            print("\nResearch Assistant:")
            print(result)

        except Exception as error:
            print(f"\n Something went wrong:{error}")

if __name__=="__main__":
    main()

