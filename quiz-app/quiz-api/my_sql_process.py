import sqlite3

class Database:
    def __init__(self, db):
        self.con = sqlite3.connect(db, check_same_thread=False)
        self.cur = self.con.cursor()
    
    def addQuestion(self, values):
        query = "INSERT INTO questions (position, title, text, image) VALUES (?, ?, ?, ?)"
        
        self.cur.execute(query, (values["position"], values["title"], values["text"], values["image"]))
        self.con.commit()

        return self.cur.lastrowid