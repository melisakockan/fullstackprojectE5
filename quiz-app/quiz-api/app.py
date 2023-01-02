from flask import Flask, request
from flask_cors import CORS
from jwt_utils import *
app = Flask(__name__)
CORS(app)

from my_sql_process import *
from Question import *

bdd = Database('database.db')

@app.route('/')
def hello_world():
	x = 'world'
	return f"Hello, {x}, my name is Melisa !!!!"

@app.route('/quiz-info', methods=['GET'])
def GetQuizInfo():
	return {"size": 0, "scores": []}, 200

@app.route('/login', methods=['POST']) #ceci est un nouveau endpoint
def Authentification():
	payload = request.get_json()
	if payload['password']=='flask2023': #Si le mot de passe est le bon
		token_built=build_token() #On génère et retourne un token à partir du mdp
		token={'token':token_built}
		return token 
	else:
		return 'Unauthorized', 401 #Sinon, retourner une erreur 401


@app.route('/questions', methods=['POST'])
def ProcessQuestions():
    	
    # On Récupère le token envoyé en paramètre
	auth = request.headers.get('Authorization')

	# Si aucun token n'est envoyé, c'est qu'il y a une erreur 
	if auth is None:
		return 'Unauthorized', 401

	auth_token = auth.split(' ')[1]

	# Si on a reçu un token, on le décode pour vérifier qu'il s'agit du bon
	decode = decode_token(auth_token)
	if decode != 'quiz-app-admin':
		return 'Unauthorized', 401

	# Si c'est vraiment le bon token, on peut ajouter la question à notre BDD et retourner l'id de la question
	else:
		my_question = Question()
		my_question.to_python(request.get_json())

		id = bdd.addQuestion(my_question)

	return str(id), 200

	

if __name__ == "__main__":
    app.run(debug=True)