from app.services.evaluator import evaluate_answer

def test_correct_answer():

    result=evaluate_answer(
        actual_answer="250 multiplied by 48 is 12,000",
        expected_answer="12000"
    )

    assert result["passed"] is True

def test_incorrect_answer():
    result=evaluate_answer(
        actual_answer="250 multipled by 48 is 10,000",
        expected_answer="12000"
    )

    assert result['passed'] is False

def test_case_insensitive_answer():
    result=evaluate_answer(
        actual_answer="Guido van Rossum developed python",
        expected_answer="Guido van Rossum"
    )

    assert result['passed'] is True

if __name__=="__main__":
    test_correct_answer()
    test_incorrect_answer()
    test_case_insensitive_answer()

    print("all evaluator tests passed")

    