import json
from pathlib import Path

def load_evaluation_dataset():
    dataset_path=Path("evaluations/dataset.json")

    with open(dataset_path,"r",encoding="utf-8") as file:
        dataset=json.load(file)

    return dataset

  