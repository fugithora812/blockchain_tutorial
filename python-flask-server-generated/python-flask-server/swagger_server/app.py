# from flask import Flask, render_template
# import requests
# import os
import connexion
# from controllers import default_controller
# from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy import Integer, String

# # 実行されるファイル(test_flask-migrate.py)の置き場所をbasedirに保存
# basedir = os.path.abspath(os.path.dirname(__file__))

# app = Flask(__name__)
# app.config["SECRET_KEY"] = "secret key"

# # データベースファイルは実行ファイルと同じ場所にapp.dbという名前で作成
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
#     os.path.join(basedir, 'app.db')
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# database = SQLAlchemy(app)
# __tablename__ = "liquor_table"
# LIQUOR_NAME = database.Column(String(32), primary_key=True)
# SELLER_NAME = database.Column(String(32), primary_key=True)
# STOCK_QUANTITY = database.Column(Integer)
# TOKEN_ID = database.Column(Integer)

# database.create_all()

# API起動
apiServe = connexion.App(__name__, specification_dir="swagger/")
apiServe.add_api("swagger.yaml")
apiServe.run(port=8080)


# @app.route("/", methods=['get'])
# def index():
#     return render_template('index.html')
