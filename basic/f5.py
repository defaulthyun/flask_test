"""
    - POST 방식으로 데이터 전송하기
        - 클라이언트 (Json, Xml, Text, Form(key=value&key=value), Form-encode, Graphql, Binary )
            - FORM 전송 ( 화면 껌벅 -> 화면 전환, [Form, Form-encode 형식] )
                - <form action = "http://127.0.0.1:5000/link" method = "post">
                    <input name = "name" value = "hello"/>
                    <input name = "age" value = 100/>
                    <input type = "submit" value="전송"/>                   
                    </form>
            - AJAX 기능 (현재 화면 유지한 상태) <JQuery로 함축적으로 표현 시> 
                $.post({
                    url : "http://127.0.0.1:5000/link"
                    param : "name=hello&age=100",
                    success : (res) => {}
                    error : (err) => {}
                })
        - 서버
            - POST 방식 데이터 추출
                - name = request.form.get('name')
                - age = request.form.get('age')
    - /link쪽으로 요청하는 방식은 다양 할 수 있다, 단 사이트 설계 상 1가지로만 정의된다면
    다른 방식의 접근은 모두 비정상적인 접근( 웹 크롤링, 스크래핑, 해킹 등)
    이런 접근 필터링 할 것인가? >> 보안의 기본사항
"""

import os
from flask import Flask, render_template, jsonify, request, redirect, url_for, session
from flask_cors import CORS
from d4 import select_login

# Flask 객체 인스턴스 생성
app = Flask(__name__)

# 세션을 위해서 시크릿 키 지정
# 임의값, 통상 해시값 활용
app.secret_key = "14d5yd93yhd1hs"

# 로그인을 하여 세션을 얻은 후 홈페이지를 진행해야 사이트의 내용을 보내주겠다 -> 컨셉
@app.route("/")
def hello():
    if not "uid" in session:  # 세션안에 uid 값이 존재하는가?
        # return redirect('/login') # url을 사용 할 때는 하드코딩 하지 않는다
        #  url_for('사용하고자 하는 URL과 연결된 함수명을 기입')
        return redirect(url_for("login"))
    return "hello world"


# @app.route : 기본적인 GET 방식
# 메소드 추가는 => methods=['POST', ...]
@app.route("/login", methods=["GET", "POST"])
def login():
    # method 별 분기
    if request.method == "GET":
        return render_template("login.html")
    elif request.method == "POST":

        # request.form['id'] : 값이 누락되면 서버 셧다운됨
        # 1. 로그인 정보 획득
        uid = request.form.get("id")
        upw = request.form.get("pw")  # 암호는 차후에 해싱 암호화(관리자도 볼 수 없다)
        print(uid, upw)

        # 2. 회원 여부 쿼리
        result = select_login(uid, upw)

        # 3. 회원 여부에 따른 처리
        if result:
            # 세션 : 클라이언트 정보를 서버가 유지하여
            # 장점 : 클라이언트가 간편하게 웹을 이용 할 수 있도록 도움을 줌
            # 단점 : 접속유저가 많으면 서버측 메모리에 부하가 온다
            # 해결 : JWT를 사용하여 보완 ( 사이트 구성 시 인증쪽에서 활용 : 차주 진행 )

            # 3-1. 세션 생성, 기타 필요한 조치 수행
            session["uid"] = uid
            # 3-2. 서비스 메인 화면으로 이동
            return redirect(url_for("hello"))
            pass
        else:
            # 4. 회원 아닐 시
            # render_template() => jinja2 템플릿 엔진 사용
            return render_template("error.html", msg="로그인 실패")

        # 임시 : 회원 아닐 시 적당한 메시지 후 다시 로그인 유도
        # return redirect("http://www.naver.com")  # 요청을 다른 URL로 포워딩한다.


if __name__ == "__main__":
    app.run(debug=True)
