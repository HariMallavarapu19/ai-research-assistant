def evaluate_answer(actual_answer:str,expected_answer:str):

    actual=actual_answer.lower().replace(",","").strip()
    expected=expected_answer.lower().replace(",","").strip()

    passed=expected in actual

    return {
        "passed":passed,
        "actual_answer":actual_answer,
        "expected_answer":expected_answer
    }

