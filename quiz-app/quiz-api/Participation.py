from datetime import datetime

class Participation:

    def __init__(self):
        self.playerName = None
        self.score = 0
        self.answers = None
        # Get current date time
        self.date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")


    def to_python(self, json):
        self.playerName = json["playerName"]
        self.answers = json["answers"]


    def compute_score(self, questions):
        if len(self.answers) != len(questions):
            self.score = None
            return

        for i in range(len(self.answers)):
            selected_answer = self.answers[i]

            if questions[i].answers[selected_answer].isCorrect:
                self.score += 1


    def to_json(self):
        return {
            "date": self.date,
            "playerName": self.playerName,
            "score": self.score
        }