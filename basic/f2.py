"""
    라우트 추가 -> URL 추가

"""
import os
from flask import Flask, render_template, jsonify, request, redirect, url_for
from flask_cors import CORS

# Flask 객체 인스턴스 생성
app = Flask(__name__)

# 기획서를 기반해서 총 페이지 수 만큼 URL 준비
# 뼈대를 먼저 잡아서 각 페이지에 해당되는 URL 준비
# blueprint를 사용한다면, 대분류, 중분류(생략가능), 소분류 등 트리 구조로 배치
# /login <-> blueprint 활용 : /auth/users/login


@app.route("/")
def hello():
    return "hello world!"


@app.route("/auth/users/signup")
def signup():
    return "signup page"


# 아래와 같은 url 구성은 blueprint을 사용하여 섹션을 나눠서 관리하는 것이 더 좋다
@app.route("/auth/users/login")
def login():
    return "login page"


@app.route("/auth/users/loginout")
def loginout():
    return "logout page"


if __name__ == "__main__":
    # Web 상에 기본 포트 : http -> 80 -> 생략가능
    # 나중에 웹서버(apache, nginx)와 연동
    app.run(host="0.0.0.0", port=5000, debug=True)
