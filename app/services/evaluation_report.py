def format_evaluation_report(report: dict):

    lines = []

    lines.append("=" * 50)
    lines.append("     AI Evaluation Report")
    lines.append("=" * 50)

    lines.append(f"Total Tests:{report['total_tests']}")
    lines.append(f"Passed     :{report['passed_tests']}")
    lines.append(f"Failed     :{report['failed_tests']}")
    lines.append(f"Score      :{report['score']:.2f}%")

    lines.append("Test Results")

    for result in report["results"]:

        status = "PASS" if result["passed"] else "FAIL"

        lines.append(
            f"{result['id']} | {status}"
        )

    lines.append("=" * 50)

    return "\n".join(lines)