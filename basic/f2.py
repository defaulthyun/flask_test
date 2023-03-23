'''
    라우트 추가 -> URL 추가

'''
import os
from flask import Flask, render_template, jsonify, request, redirect, url_for
from flask_cors import CORS

# Flask 객체 인스턴스 생성
app = Flask(__name__)

# 접속 URL 설정
@app.route('/')
def hello():
    return "hello world!"

if __name__ == '__main__':
    # Web 상에 기본 포트 : http -> 80 -> 생략가능
    # 나중에 웹서버(apache, nginx)와 연동
    app.run(host = '0.0.0.0', port = 5000, debug=True)