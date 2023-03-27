# 어플리케이션 구동
        - flask 명령 사 기본으로 찾는 파일 ( 아래 파일들은 공존하면 의도치 않는 것이 수행 될 수 있다.)
        - 여기서 1개만 사용하도록 지향 ( 다 있어서 무방 )
            - wsgi.py
            - app.py
            - 환경변수에 지정된 파일을(FLASK_APP-xxx) 찾는다
    - 커스텀 설정
        - 1. 환경 변수를 지정하고 실행 -> OS에 설정하거나 혹은 shell(MAC/Linux) or cmd(Window)를 작성하여 구동
            - set FLASK_APP=start_app
            - flask run
        - 2. 환경변수 파일을 읽어서 처리
            - conda install python-dotenv -y (자동 yes)
            - pip install python-dotenv
            - 파일 생성
                - env.config~~`~``~```
                - start_app.py
            - 실행
                - flask -e ./env.config run
        - 3. 명령 수행 시 옵션 제공
            - flask --app start_app run
            - flask --app start_app -- debug run
        


# 실습

    - wsgi.py 파일 생성
        - flask run