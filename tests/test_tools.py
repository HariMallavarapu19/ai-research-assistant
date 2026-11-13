from app.tools.calculator_tool import calculator
from app.tools.wikipedia_tool import wikipedia_search

def test_calculator():
    result=calculator.invoke({
        "expression":"250*48"
    })

    print("\nCalculator result:",result)

def test_wikipedia():
    result=wikipedia_search.invoke({
        "query":"Python programming language"
    })
    print("\nWikipedia result",result)

if __name__=="__main__":
    test_calculator()
    test_wikipedia()

    