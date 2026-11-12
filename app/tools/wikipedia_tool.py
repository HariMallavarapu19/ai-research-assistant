from langchain.tools import tool
import wikipedia

@tool
def wikipedia_search(query:str)->str:
    """
    Search Wikipedia for general knowlege
    and retrieve a summary about a topic or person
    """

    try:
        result=wikipedia.summary(
            query,
            sentence=5,
            auto_suggest=True
        )

        return result
    except wikipedia.exceptions.DisambiguationError as error:
        return(
            "The topic is ambiguos"
            f"Possible topics:{error.options[:5]}"
        )

    except wikipedia.exceptions.PageError:
        return "No Wikipedia page was found for this topic"

    except Exception:
        return "Wikipedia search failed"
