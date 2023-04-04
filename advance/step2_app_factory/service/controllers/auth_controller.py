from flask import render_template, request, url_for, jsonify
from service.controllers import bp_auth as auth

# 시간 정보 획득, 시간차를 계산하는 함수
from datetime import datetime, timedelta

# Flask 객체 획득
from flask import current_app

# 암호화 관련
import jwt
import bcrypt

# ~/auth
@auth.route("/")
def home():
    # url_for( "별칭.함수명" ) => url이 리턴된다
    print(url_for("auth_bp.login"))
    return "auth home"


@auth.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    else:
        # jwt 관련 체크 -> 정상(200), 오류(401)

        # 1. uid, upw 획득
        uid = request.form.get("uid")
        upw = request.form.get("upw")

        # 2. uid, upw로 회원이 존재하는지 체크 -> (DB 사용해야되지만 임시 값으로 비교)
        if uid == "guest" and upw == "1234":

            # 3. 회원이면 토큰 생성
            payload = {
                "id": uid,
                # 만료시간 : 토큰이 발급되고 나서 24시간 후 토큰이 만료됨
                # utcnow() : 영국 그리니치 기준 시각  + seconds=60*60*24 : 24시간
                "exp": datetime.utcnow() + timedelta(seconds=60 * 60 * 24),
            }

            # 토큰 발급 -> 시크릿 키, 해싱 알고리즘("HS256"), 데이터(payload)
            SECRET_KEY = current_app.config["SECRET_KEY"]  # 환경변수값 획득

            # 발급
            token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")

            # 4. 응답 전문 구성 -> 응답
            return jsonify({"code": 1, "token": token})


@auth.route("/logout")
def logout():
    return "auth logout"


@auth.route("/signup")
def signup():
    
    # 비밀번호 암호화
    password = "1234"

    # 암호화된 값은 DB에 패스워드 컬럼에 저장
    bcrypt_pw = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    # 확인 및 복호화
    print(password, bcrypt_pw, bcrypt.checkpw(password.encode('utf-8'),b))

    return "auth signup"


@auth.route("/delete")
def delete():
    return "auth delete"