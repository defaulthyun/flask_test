import os
from flask import Flask
from flask_cors import CORS

## Flask 객체 인스턴스 생성

app = Flask(__name__)

# 접속 URL 설정
@app.route("/")
def home():
    return "home page custom_app"