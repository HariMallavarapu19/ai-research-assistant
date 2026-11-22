from app.services.tool_evaluator import evaluate_tool_selection

def test_correct_tool_selection():
    result=evaluate_tool_selection(
        expected_tool="calculator",
        actual_tool="calculator"
    )

    assert result['passed'] is True

def test_incorrect_tool_selection():
    result=evaluate_tool_selection(
        expected_tool="calculator",
        actual_tool='wikipedia_search'
    )
    assert result['passed'] is False

def test_web_search_tool_selection():
    result=evaluate_tool_selection(
        expected_tool="tavily_search",
        actual_tool="tavily_search"
    )
    assert result['passed'] is True

if __name__=="__main__":
    test_correct_tool_selection()
    test_incorrect_tool_selection()
    test_web_search_tool_selection()

    print('All tool  evaluation tests passed')

