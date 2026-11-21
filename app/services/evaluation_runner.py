from app.services.evaluation_services import load_evaluation_dataset
from app.services.evaluator import evaluate_answer

def run_evaluation(mock_answers:dict):
    dataset=load_evaluation_dataset()
    results=[]

    for test_case in dataset:
        test_id =test_case['id']
        expected_answer=test_case['expected_answer']
        actual_answer=mock_answers.get(test_id,"")

        evaluation_result=evaluate_answer(
            actual_answer,expected_answer
        )

        results.append(
            {
                "id":test_id,
                "category":test_case['category'],
                **evaluation_result
            }
        )

    total_tests=len(results)
    passed_tests=sum(
        1 for result in results if result['passed']
    )

    score=(
        passed_tests/total_tests*100
        if total_tests>0
        else 0
    )

    return {
        "total_tests":total_tests,
        "passed_tests":passed_tests,
        "failed_tests":total_tests-passed_tests,
        "score":score,
        "results":results
    }

