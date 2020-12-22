#!/usr/bin/env python3

# import connexion
from flask import Flask, render_template
# from swagger_server import encoder


def main():
    app = Flask(__name__)
    # app = connexion.App(__name__, specification_dir='./swagger/')
    # app.app.json_encoder = encoder.JSONEncoder
    # app.add_api('swagger.yaml', arguments={'title': '酒類在庫取得・検索API'})
    # app.run(port=8080)

    @app.route("/", methods=['get'])
    def index():
        return render_template('index.html')


if __name__ == '__main__':
    main()
