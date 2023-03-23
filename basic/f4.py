"""
    - GET 방식으로 데이터 전송하기
        - 클라이언트 ( key=value&key=value )
            - Link ( 화면 교체 )
                - <a href = "http://127.0.0.1:5000/link?name=hello&age=100">링크</a>
            - FORM 전송 ( 화면 껌벅 -> 화면 전환)
                - <form action = "http://127.0.0.1:5000/link" method = "get">
                    <input name = "name" value = "hello"/>
                    <input name = "age" value = 100/>
                    <input type = "submit" value="전송"/>                   
                    </form>
            - AJAX 기능 (현재 화면 유지한 상태)<JQuery로 함축적으로 표현 시> 
                $.get({
                    url : "http://127.0.0.1:5000/link"
                    param : "name=hello&age=100",
                    success : (res) => {}
                    error : () => {}
                })
        - 서버
            - GET 방식 데이터 추출
                - name = request.args.get('name')
                - age = request.args.get('age')
    - /link쪽으로 요청하는 방식은 다양 할 수 있다, 단 사이트 설계 상 1가지로만 정의된다면
    다른 방식의 접근은 모두 비정상적인 접근( 웹 크롤링, 스크래핑, 해킹 등)
    이런 접근 필터링 할 것인가? > 보안의 기본사항
            
"""

import os
from flask import Flask, render_template, jsonify, request, redirect, url_for
from flask_cors import CORS

app = Flask(__name__)


@app.route("/link")
def link():
    # request.args['age'] -> 데이터 누락 시 서버 셧다운, 사용하면 안됨
    # request.args.get("age") -> 데이터 누락 시 None이 나와서 예외처리 가능함
    name = request.args.get("name")
    age = request.args.get("age")
    return "name : [%s]  age: [%s]" % (name, age)


@app.route("/test")
def test():
    # 엔트리포인트(진입로, 프로그램 시작점)과 같은 경로에 templates/test.html 생성
    return render_template("test.html")


if __name__ == "__main__":
    app.run(debug=True)
