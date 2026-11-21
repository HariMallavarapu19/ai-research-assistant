from app.services.evaluation_report import format_evaluation_report

def test_format_evaluation_report():
    report= {
        "total_tests": 4,
        "passed_tests": 3,
        "failed_tests": 1,
        "score": 75.0,
        "results": [
            {
                "id": "EVAL-001",
                "passed": True
            },
            {
                "id": "EVAL-002",
                "passed": True
            },
            {
                "id": "EVAL-003",
                "passed": True
            },
            {
                "id": "EVAL-004",
                "passed": False
            }
        ]
    }

    formatted_report=format_evaluation_report(report)
    print("\nformatted_report")

    assert "AI Evaluation Report" in formatted_report
    assert "Total Tests:4" in formatted_report
    assert "Passed     :3" in formatted_report
    assert "Failed     :1" in formatted_report
    assert "75.00%" in formatted_report
    assert "EVAL-004 | FAIL" in formatted_report

if __name__=="__main__":
    test_format_evaluation_report()