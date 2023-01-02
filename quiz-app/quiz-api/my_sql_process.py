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

    def question_to_json(self, question, answers):
        return {
            "id": question[0],
            "position": question[1],
            "title": question[2],
            "text": question[3],
            "image": question[4],
            "possibleAnswers": [self.answer_to_json(answer) for answer in answers]
        }


    def answer_to_json(self, answer):
        return {
            "id": answer[0],
            "question_id": answer[1],
            "text": answer[2],
            "isCorrect": True if answer[3] == 1 else False
        }
    
    def getQuestionById(self, id):
        query = "SELECT * FROM questions WHERE id = ?"
        self.cur.execute(query, (id,))
        question_sql = self.cur.fetchone()

        if question_sql is None:
            return None

        query = "SELECT * FROM answers WHERE question_id = ?"
        self.cur.execute(query, (id,))
        answers_sql = self.cur.fetchall()

        question = Question()
        
        question.to_python(self.question_to_json(question_sql, answers_sql))

        return question

    def getIdByPosition(self, position):
        query = "SELECT id FROM questions WHERE position = ?"
        self.cur.execute(query, (position,))
        id = self.cur.fetchone()

        if id is None:
            return None

        return id[0]

    def getQuestionByPosition(self, position):
        id = self.getIdByPosition(position)

        if id is None:
            return None

        return self.getQuestionById(id)


    def deleteAnswers(self, question_id):
        query = "DELETE FROM answers WHERE question_id = ?"
        self.cur.execute(query, (question_id,))
        self.con.commit()

    def deleteQuestion(self, id):
        query = "DELETE FROM questions WHERE id = ?"
        self.cur.execute(query, (id,))
        self.con.commit()

    def updateQuestion(self, question, id):
        query = "UPDATE questions SET position = ?, title = ?, text = ?, image = ? WHERE id = ?"
        self.cur.execute(query, (question.position, question.title, question.text, question.image, id))
        self.con.commit()

    def deleteAllAnswers(self):
        query = "DELETE FROM answers"
        self.cur.execute(query)
        self.con.commit()

    def deleteAllQuestions(self):
        query = "DELETE FROM questions"
        self.cur.execute(query)
        self.con.commit()
        self.deleteAllAnswers()

    def offsetPosition(self, position):
        query = "UPDATE questions SET position = position + 1 WHERE position >= ?"
        self.cur.execute(query, (position,))
        self.con.commit()

    def offsetUpdatePosition(self, old_position, new_position):
        if old_position < new_position:
            query = "UPDATE questions SET position = position - 1 WHERE position > ? AND position <= ?"
            self.cur.execute(query, (old_position, new_position))
        else:
            query = "UPDATE questions SET position = position + 1 WHERE position >= ? AND position < ?"
            self.cur.execute(query, (new_position, old_position))
        self.con.commit()
  

    def offsetDeletePosition(self, position):
        query = "UPDATE questions SET position = position - 1 WHERE position > ?"
        self.cur.execute(query, (position,))
        self.con.commit()

    def getNumberOfQuestions(self):
        query = "SELECT COUNT(*) FROM questions"
        self.cur.execute(query)
        number = self.cur.fetchone()

        if number is None:
            return None

        return number[0]

    
    def deleteAllParticipations(self):
        query = "DELETE FROM participations"
        self.cur.execute(query)
        self.con.commit()

    def getAllParticipations(self):
        query = "SELECT * FROM participations"
        self.cur.execute(query)
        participations = self.cur.fetchall()

        if participations is None:
            return []

        all_participations = self.allParticipationsToJson(participations)

        return all_participations

    def allParticipationsToJson(self, participations):
        return [{
            "date": participation[1],
            "playerName": participation[2],
            "score": participation[3]
        } for participation in participations]