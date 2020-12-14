from flask import Flask, render_template, request
import requests
from controllers import default_controller
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, String

app = Flask(__name__)  # インスタンス生成
app.config["SECRET_KEY"] = "secret key"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite://flask.sqlite"

database = SQLAlchemy(app)
__tablename__ = "liquor_table"
LIQUOR_NAME = database.Column(String(32), primary_key=True)
SELLER_NAME = database.Column(String(32), primary_key=True)
STOCK_QUANTITY = database.Column(Integer)
TOKEN_ID = database.Column(Integer)

database.create_all()


@app.route("/", methods=['get'])
def index():
    return render_template('index.html')
