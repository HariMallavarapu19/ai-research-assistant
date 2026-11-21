from app.services.evaluation_runner import run_evaluation

def test_evaluation_runner():
    mock_answers={
        "EVAL-001": "250 multiplied by 48 is 12000",
        "EVAL-002": "Python was developed by Guido van Rossum",
        "EVAL-003": "25 multiplied by 4 is 100",
        "EVAL-004": "Recent AI developments include new AI models and research."
    }

    report=run_evaluation(mock_answers)

    print('\nEvaluation Report')
    print(report)

    assert report['total_tests']==4
    assert report['passed_tests']==3
    assert report['failed_tests']==1
    assert report['score']==75.0

if __name__=='__main__':
    test_evaluation_runner()