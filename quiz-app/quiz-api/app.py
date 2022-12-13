from flask import Flask
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
	x = 'world'
	return f"Hello, {x}, my name is Melisa !!!!"

if __name__ == "__main__":
    app.run()