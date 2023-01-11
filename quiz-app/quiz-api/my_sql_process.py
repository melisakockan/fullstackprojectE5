import sqlite3
from Question import *
from Answer import *
from Participation import *
import os

class Database:
    def __init__(self, db):
        self.db_name = db
        self.con = sqlite3.connect(self.db_name, check_same_thread=False)
        self.con.isolation_level = None
        self.cur = self.con.cursor()

    
    def addQuestion(self, question):
        query = "INSERT INTO questions (position, title, text, image) VALUES (?, ?, ?, ?)"
        
        self.cur.execute(query, (question.position, question.title, question.text, question.image))
        self.con.commit()

        id = self.cur.lastrowid

        self.correctPositions();

        return id

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
        self.correctPositions();

    def updateQuestion(self, question, id):
        query = "UPDATE questions SET position = ?, title = ?, text = ?, image = ? WHERE id = ?"
        self.cur.execute(query, (question.position, question.title, question.text, question.image, id))
        self.con.commit()
        self.correctPositions();

    def deleteAllAnswers(self):
        query = "DELETE FROM answers"
        self.cur.execute(query)
        self.con.commit()

    def deleteAllQuestions(self):
        query = "DELETE FROM questions"
        self.cur.execute(query)
        self.con.commit()
        self.deleteAllAnswers()
        self.correctPositions();

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
        query = "SELECT * FROM participations ORDER BY score DESC"
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


    def addParticipation(self, participation):
        query = "INSERT INTO participations (date, player_name, score) VALUES (?, ?, ?)"
        self.cur.execute(query, (participation.date, participation.playerName, participation.score))
        self.con.commit()

    def getAllQuestions(self):
        query = "SELECT * FROM questions ORDER BY position ASC"
        self.cur.execute(query)
        questions = self.cur.fetchall()

        if questions is None:
            return []

        all_questions = self.allQuestionsToJson(questions)

        for question in all_questions:
            id = question["id"]
            query = "SELECT * FROM answers WHERE question_id = ?"
            self.cur.execute(query, (id,))
            answers = self.cur.fetchall()

            question["possibleAnswers"] = [self.answer_to_json(answer) for answer in answers]

        return all_questions

    def allQuestionsToJson(self, questions):
        return [{
            "id": question[0],
            "position": question[1],
            "title": question[2],
            "text": question[3],
            "image": question[4]
        } for question in questions]


    def rebuildDB(self):
        self.deleteDB()
        self.createDB()


    def deleteDB(self):
        # DROP DATABASE
        query = "DROP TABLE IF EXISTS questions"
        self.cur.execute(query)
        query = "DROP TABLE IF EXISTS answers"
        self.cur.execute(query)
        query = "DROP TABLE IF EXISTS participations"
        self.cur.execute(query)
        query = "DROP TABLE IF EXISTS themes"
        self.cur.execute(query)
        self.con.commit()

    def createDB(self):
        # CREATE DATABASE
        query = "CREATE TABLE IF NOT EXISTS questions (id INTEGER PRIMARY KEY AUTOINCREMENT, position INTEGER, title TEXT, text TEXT, image TEXT)"
        self.cur.execute(query)
        query = "CREATE TABLE IF NOT EXISTS answers (id INTEGER PRIMARY KEY AUTOINCREMENT, question_id INTEGER, text TEXT, is_correct INTEGER)"
        self.cur.execute(query)
        query = "CREATE TABLE IF NOT EXISTS participations (id INTEGER PRIMARY KEY AUTOINCREMENT, date TEXT, player_name TEXT, score INTEGER)"
        self.cur.execute(query)
        query = "CREATE TABLE IF NOT EXISTS themes (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, data TEXT, volume FLOAT)"
        self.cur.execute(query)
        self.con.commit()


    def correctPositions(self):
        print("correcting positions");
        query = "SELECT id FROM questions ORDER BY position"
        self.cur.execute(query)
        ids = self.cur.fetchall()

        if ids is None:
            return None

        for i in range(len(ids)):
            query = "UPDATE questions SET position = ? WHERE id = ?"
            self.cur.execute(query, (i+1, ids[i][0]))
            self.con.commit()


    # SOUND MANAGEMENT

    def addTheme(self, name, data, volume):
        if self.ThemeExists(name):
            self.deleteTheme(name)

        query = "INSERT INTO themes (name, data, volume) VALUES (?, ?, ?)"
        self.cur.execute(query, (name, data, volume))
        self.con.commit()

        return self.getTheme(name)

    def DefaultExists(self):
        query = "SELECT * FROM themes WHERE name = ?"
        self.cur.execute(query, ("default",))
        theme = self.cur.fetchone()

        return theme is not None
    
    def ThemeExists(self, name):
        query = "SELECT * FROM themes WHERE name = ?"
        self.cur.execute(query, (name,))
        theme = self.cur.fetchone()

        return theme is not None

    def getTheme(self, name):

        query = "SELECT * FROM themes WHERE name = ?"
        self.cur.execute(query, (name,))
        theme = self.cur.fetchone()

        if theme is None:
            if self.DefaultExists():
                return self.getTheme("default")
            else:
                return None

        return self.theme_to_json(theme)

    def theme_to_json(self, theme):
        return {
            "name": theme[1],
            "data": theme[2],
            "volume": theme[3]
        }

    def getAllThemes(self):
        query = "SELECT * FROM themes"
        self.cur.execute(query)
        themes = self.cur.fetchall()

        if themes is None:
            return []

        return [self.theme_to_json(theme) for theme in themes]

    def deleteTheme(self, name):
        query = "DELETE FROM themes WHERE name = ?"
        self.cur.execute(query, (name,))
        self.con.commit()
