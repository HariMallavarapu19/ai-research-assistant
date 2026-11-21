from app.services.evaluation_services import load_evaluation_dataset

def test_load_evaluation_dataset():
    dataset=load_evaluation_dataset()

    print("\nLoaded evaluation dataset")
    print(dataset)

    assert len(dataset)==4

    for test_case in dataset:
        assert "id" in test_case
        assert "question" in test_case
        assert "expected_answer" in test_case
        assert "expected_tool" in test_case
        assert "category" in test_case

    print("\nEvaluation dataset loaded successfully")

if __name__=="__main__":
    test_load_evaluation_dataset()

