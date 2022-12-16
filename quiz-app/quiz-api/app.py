from flask import Flask, request
from flask_cors import CORS
from jwt_utils import build_token
app = Flask(__name__)
CORS(app)

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
	if payload['password']=='flask2023':#Si le mot de passe est le bon
		token_built=build_token()#On génère et retourne un token à partir du mdp
		token={'token':token_built}
		return token 
	else:
		return 'Unauthorized', 401 #Sinon, retourner une erreur 401


if __name__ == "__main__":
    app.run()