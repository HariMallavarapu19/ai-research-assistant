from langchain.tools import tool
import numexpr

@tool
def calculator(expression:str)->str:
    """
    Calculate mathematical expressions.

    Use this tool for arithmetic calculations
    such as addition, subtraction, multiplication,
    division and powers.
    """
    try:
        result=numexpr.evaluate(expression).item()
        return str(result)
    except Exception:
        return "Unable to calculate the expression"

        
    
