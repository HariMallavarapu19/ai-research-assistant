from app.services.evaluation_runner import run_evaluation
from app.services.evaluation_report import format_evaluation_report

def main():
    mock_answers = {
        "EVAL-001": "12000",
        "EVAL-002": "Guido van Rossum",
        "EVAL-003": "100",
        "EVAL-004": "I cannot provide current AI developments."
    }

    report =run_evaluation(mock_answers)
    formatted_report=format_evaluation_report(report)
    print(formatted_report)

if __name__=="__main__":
    main()


