import json
from pathlib import Path
from datasets import Dataset
from ragas import evaluate
from ragas.metrics import answer_relevancy, context_precision, faithfulness


def load_dataset(path: str = "evaluation/dataset.json") -> Dataset:
    rows = json.loads(Path(path).read_text())
    return Dataset.from_list(rows)


def run_evaluation(path: str = "evaluation/dataset.json"):
    dataset = load_dataset(path)
    return evaluate(
        dataset,
        metrics=[faithfulness, answer_relevancy, context_precision],
    )


if __name__ == "__main__":
    print(run_evaluation())
