import json
import os


class Progress:

    def __init__(self, list_name):
        self.filename = f"progress_{list_name}.json"

    def load(self):
        if not os.path.exists(self.filename):
            return set()

        try:
            with open(self.filename, "r") as f:
                data = json.load(f)

            return set(data.get("completed", []))

        except (json.JSONDecodeError, FileNotFoundError):
            print("Invalid progress file. Starting fresh.")
            return set()

    def save(self, completed):
        with open(self.filename, "w") as f:
            json.dump(
                {
                    "completed": list(completed)
                },
                f,
                indent=4
            )