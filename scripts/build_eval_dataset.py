import json
from pathlib import Path


EXAMPLE = [
    {
        "question": "What is the document about?",
        "ground_truth": "Update this with your expected answer.",
        "contexts": ["Replace with retrieved chunks after a test run."],
        "answer": "Replace with actual model answer.",
    }
]


if __name__ == "__main__":
    Path("evaluation/dataset.sample.json").write_text(json.dumps(EXAMPLE, indent=2))
    print("Wrote evaluation/dataset.sample.json")
