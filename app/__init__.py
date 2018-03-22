from flask import Flask


app = Flask(__name__)
app = Flask(__name__, template_folder='designs/')


from app import routes