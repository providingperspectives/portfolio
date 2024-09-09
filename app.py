from flask import Flask
from views import main
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.register_blueprint(main)

if __name__ == "__main__":
    app.run(debug=True)