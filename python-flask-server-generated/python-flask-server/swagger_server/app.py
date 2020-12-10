from flask import Flask, render_template, request
import requests
from controllers import default_controller

app = Flask(__name__)  # インスタンス生成


@app.route("/", methods=['get'])
def index():
    return render_template('index.html')
