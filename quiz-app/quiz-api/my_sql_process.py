import sqlite3
from Question import *
from Answer import *

class Database:
    def __init__(self, db):
        self.con = sqlite3.connect(db, check_same_thread=False)
        self.con.isolation_level = None
        self.cur = self.con.cursor()

    
    def addQuestion(self, question):
        query = "INSERT INTO questions (position, title, text, image) VALUES (?, ?, ?, ?)"
        
        self.cur.execute(query, (question.position, question.title, question.text, question.image))
        self.con.commit()

        return self.cur.lastrowid

    def addAnswer(self, answer, question_id):
        query = "INSERT INTO answers (question_id, text, is_correct) VALUES (?, ?, ?)"
        
        self.cur.execute(query, (question_id, answer.text, answer.isCorrect))
        self.con.commit()

    def getQuestion(self, id):
        query = "SELECT * FROM questions WHERE id = ?"
        self.cur.execute(query, (id,))
        question_sql = self.cur.fetchone()

        query = "SELECT * FROM answers WHERE question_id = ?"
        self.cur.execute(query, (id,))
        answers_sql = self.cur.fetchall()

        question = Question()
        question.id = question_sql[0]
        question.position = question_sql[1]
        question.title = question_sql[2]
        question.text = question_sql[3]
        question.image = question_sql[4]

        for answer_sql in answers_sql:
            answer = Answer()
            answer.id = answer_sql[0]
            answer.text = answer_sql[2]
            answer.isCorrect = True if answer_sql[3] == 1 else False

            question.answers.append(answer)

        return question