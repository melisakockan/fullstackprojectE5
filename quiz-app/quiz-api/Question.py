class Question:
    def __init__(self, title : str = None, text : str = None, image : str = None, position : int = None):
        self.title = title
        self.text = text
        self.image = image
        self.position = position

    def to_json(self):
        return {
            "title": self.title,
            "text": self.text,
            "image": self.image,
            "position": self.position
        }

    def to_python(self, json):
        self.title = json["title"]
        self.text = json["text"]
        self.image = json["image"]
        self.position = json["position"]
  