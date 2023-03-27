from flask import render_template, request, url_for
from service.controllers import bp_auth as auth

# ~/auth
@auth.route("/")
def home():
    # url_for( "별칭.함수명" ) => url이 리턴된다
    print(url_for("auth_bp.login"))
    return "auth home"


@auth.route("/login")
def login():
    return "auth login"


@auth.route("/logout")
def logout():
    return "auth logout"


@auth.route("/signup")
def signup():
    return "auth signup"


@auth.route("/delete")
def delete():
    return "auth delete"
