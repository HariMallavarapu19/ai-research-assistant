def evaluate_tool_selection(expected_tool:str,actual_tool:str):
    passed=expected_tool==actual_tool
    return{
        "passed":passed,
        "expected_tool":expected_tool,
        "actual_tool":actual_tool
    }