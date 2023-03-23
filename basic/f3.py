# 홈페이지 작성, 디버깅모드, 포트 5000번, 홈페이지는 화면에 "HelloWorld!" 출력
"""
    클라이언트가 서버에게 데이터를 전송하는 방법
    - 방법
        - GET/POST/PUT ... : HTTP 프로토콜(통신규약)에서 정의
        - HTTP는 헤더(고정크기)를 먼저 전송, body(가변크기)를 나중에 전송
        - GET 방식은 헤더만 전송 -> 고정크기만 전송 -> 소량 전송 (최대치 제한)
            - HTTP Header를 알면, 패킷(전송데이터)를 가로채서 데이터를 해킹할 수 있다. -> 보안 취약점
        - POST 방식은 Header 전송 -> Body 전송 -> 대량 전송
            - 구조를 모르기 때문에 보안에 상대적으로 우수, 암호화 가능 -> 보안 암호(상대적)
    - 방식
        - form 전송 : <form> 태그 사용, 화면이 껌벅거림(순식간에 진행, X 주소창 앞 아이콘 변경)
        - AJAX 전송 : 백그라운드로 서버와 통신, 화면 고정
        - websocket 전송 : 웹소켓을 열어서 통신
        - 동적파라미터 : get 헤더를 활용하여 URL에 데이터를 넣어서 전송하는 방식

    - 동적파라미터
        - HTTP 헤더의 주소 정보를 활용
    - 캐시 지우기 : ctrl + shift + r
        
"""

import os
from flask import Flask, render_template, jsonify, request, redirect, url_for
from flask_cors import CORS

app = Flask(__name__)


@app.route("/")
def hello():
    return "hello world!"


# 동적파라미터, 문자열타입으로 전송
# 용량은 헤더 사이즈, 주소 크기를 초과 할 수 없다
# 파라미터는 함수 인자를 통해서 함수 내부로 진입
# #, <, > 은 전달 안됨, 한글, 영문, 특수 대소문자 다 가능
# -> URL 인코딩으로 해결 : %12%ae..
@app.route("/news/<news_id>")
def news(news_id):
    return "전달된 데이터 [%s]" % news_id


# 1개 이상도 전달 가능한가? >> URL을 무한대로 생성 가능
# http://127.0.0.1:5000/전달값1/news2/전달값2
@app.route("/<news_id>/news2/<news_author>")
def news2(news_id, news_author):
    return "전달된 데이터 [%s], 전달된 데이터 2 [%s] " % (news_id, news_author)


# 타입 제한이 가능한가? >> int, float, path
# http://127.0.0.1:5000/news3/1234567 -> 200 OK
# http://127.0.0.1:5000/news3/hello -> 404 Not Found
@app.route("/news3/<int:news_id>")
def news3(news_id):
    return "전달된 데이터 [%s]" % news_id


# path : 전달값을 무한대로 늘려주는 옵션
# http://127.0.0.1:5000/news4/1/2/3/4/5/6/7/8/9/home/동엽/10
@app.route("/news4/<path:news_id>")
def news4(news_id):
    # 정보를 구분해서 여러개로 전달 가능(가변적)
    return "전달된 데이터 [%s]" % news_id.split("/")[-2]


if __name__ == "__main__":
    app.run(debug=True)
