from Answer import *

class Question:
    def __init__(self, title : str = None, text : str = None, image : str = None, position : int = None):
        self.title = title
        self.text = text
        self.image = image
        self.position = position
        self.answers = []

    def to_json(self):
        return {
            "title": self.title,
            "text": self.text,
            "image": self.image,
            "position": self.position,
            "possibleAnswers": [answer.to_json() for answer in self.answers]
        }

    def to_python(self, json):
        self.title = json["title"]
        self.text = json["text"]
        self.image = json["image"]
        self.position = json["position"]

        for answer in json["possibleAnswers"]:
            a = Answer()
            a.to_python(answer)
            self.answers.append(a)
  