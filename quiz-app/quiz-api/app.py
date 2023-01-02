from flask import Flask, request
from flask_cors import CORS
from jwt_utils import *
app = Flask(__name__)
CORS(app)

from my_sql_process import *
from Question import *


bdd = Database('database.db')


def check_auth(auth):
	# Si aucun token n'est envoyé, c'est qu'il y a une erreur 
		if auth is None:
			return False

		auth_token = auth.split(' ')[1]

		# Si on a reçu un token, on le décode pour vérifier qu'il s'agit du bon
		decode = decode_token(auth_token)
		if decode != 'quiz-app-admin':
			return False
		return True

@app.route('/')
def hello_world():
	x = 'world'
	return f"Hello, {x}, my name is Melisa !!!!"

@app.route('/quiz-info', methods=['GET'])
def GetQuizInfo():
	number_of_questions = bdd.getNumberOfQuestions()
	
	return {"size": number_of_questions, "scores": []}, 200

@app.route('/login', methods=['POST']) #ceci est un nouveau endpoint
def Authentification():
	payload = request.get_json()
	if payload is None:
		return 'Unauthorized', 401
	elif payload['password']=='flask2023': #Si le mot de passe est le bon
		token_built=build_token() #On génère et retourne un token à partir du mdp
		token={'token':token_built}
		return token 
	else:
		return 'Unauthorized', 401 #Sinon, retourner une erreur 401


@app.route('/questions', methods=['POST', 'GET'])
def ProcessQuestions():
    	
	if request.method == 'POST':
			
		# On Récupère le token envoyé en paramètre
		auth = request.headers.get('Authorization')

		if not check_auth(auth):
			return 'Unauthorized', 401

		# Si c'est vraiment le bon token, on peut ajouter la question à notre BDD et retourner l'id de la question
		else:
			my_question = Question()
			my_question.to_python(request.get_json())

			
			if bdd.getIdByPosition(my_question.position) is not None:
				bdd.offsetPosition(my_question.position)
				

			id = bdd.addQuestion(my_question)

			for answer in my_question.answers:
				bdd.addAnswer(answer, id)

		return str(id), 200

	elif request.method == 'GET':
		position = request.args.get('position')
		if position is None:
			return 'Incorrect position', 404
		
		question = bdd.getQuestionByPosition(position)

		if question is None:
			return 'Position does not exist', 404

		return question.to_json(), 200



	else:
		return 'Unauthorized', 401


@app.route('/questions/<id>', methods=['GET', 'PUT', 'DELETE'])
def Process(id):
    
	if id == "all" and request.method == 'DELETE':
		# On Récupère le token envoyé en paramètre
		auth = request.headers.get('Authorization')

		if not check_auth(auth):
			return 'Unauthorized', 401

		else:
			bdd.deleteAllQuestions()
			return 'All questions deleted', 204


	# If id is not an integer
	elif not id.isdigit():
			return 'Incorrect ID', 401

	question = bdd.getQuestionById(id)

	if question is None:
		return 'ID does not exist', 404

    	
	if request.method == 'GET':
		return question.to_json(), 200

	elif request.method == 'PUT':
		# On Récupère le token envoyé en paramètre
		auth = request.headers.get('Authorization')

		if not check_auth(auth):
			return 'Unauthorized', 401

		else: # On est bien authentifié
			# On récupère la nouvelle question
			new_question = Question()
			new_question.to_python(request.get_json())

			if new_question.position != question.position:
				bdd.offsetUpdatePosition(question.position, new_question.position)

			# On supprime les anciennes réponses
			bdd.deleteAnswers(id)

			# On ajoute les nouvelles réponses
			for answer in new_question.answers:
				bdd.addAnswer(answer, id)

			# On met à jour la question
			bdd.updateQuestion(new_question, id)

			return 'OK', 204

	elif request.method == 'DELETE':
    		# On Récupère le token envoyé en paramètre
		auth = request.headers.get('Authorization')

		if not check_auth(auth):
			return 'Unauthorized', 401

		else: # On est bien authentifié
			bdd.deleteQuestion(id)
			bdd.deleteAnswers(id)

			position = question.position
			bdd.offsetDeletePosition(position)

			return 'OK', 204




if __name__ == "__main__":
    app.run(debug=True)