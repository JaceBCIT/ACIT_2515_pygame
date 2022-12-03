import json

class GetScore:
    """Class to read json file and save it to variable"""
    def __init__(self):
        self.filename = "./data/data.json"
        self.users = []
        self.high_score = []

        self.load_json()

    def load_json(self):
        with open(self.filename, "r") as f:
            self.board = json.load(f)

