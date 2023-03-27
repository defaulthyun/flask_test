import os
from flask import Flask
from flask_cors import CORS

"""
    create_app는 플라스크 내부에서 정의된 함수명(수정 X)
    flask run을 수행하면 내부적으로 엔트리포인트 모듈에서 create_app() 를 찾는다   
    차후, 다른 모듈에서는 flask.current_app 이라는 변수로 app을 접근 할 수 있다(모듈가져오기)
"""

## Flask 객체 인스턴스 생성


def create_app():
    app = Flask(__name__)

    # 접속 URL 설정
    @app.route("/")
    def home():
        return "home page custom_app"

    return app
