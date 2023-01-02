class Answer:
    def __init__(self, text : str = None, isCorrect : bool = None):
        self.text = text
        self.isCorrect = isCorrect

    def to_json(self):
        return {
            "text": self.text,
            "isCorrect": self.isCorrect
        }

    def to_python(self, json):
        self.text = json["text"]
        self.isCorrect = json["isCorrect"]
  