import json

class GetScore:
    def __init__(self):
        self.filename = "./data/data.json"
        self.users = []
        self.high_score = []

        self.load_json()

    def load_json(self):
        with open(self.filename, "r") as f:
            self.board = json.load(f)

        for i in self.board.keys():
            self.users.append(i)
        
        for j in self.board.values():
            self.high_score.append(j[0])
        
