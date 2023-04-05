# 어플리케이션 팩토리

    - 엔트리 위치 조정, 코드 수정
    - app = Flask(__name__)
        - 현재 작성 한 이코드는 전역변수로 존재
        - 프로젝트의 규모가 커질 시 순환 참조를 활 확률이 높음
        - flask 구현 시 어플리케이션 팩토리라는 형태로 사용하라 => 권장

# 방법

    - 플라스크 객체를 생성하는 코드
        - 특정 패키지 밑에 위치 => ex) service
        - __init__.py로 이름변경
        - 구조
            - service
                ▷ __init__.py
        - 최종 실행 명령
            - flask --app service --debug run

# 블루프린트

    - URL과 함수의 매핑(라우트)를 관리하는 도구

# BootStrap

    - [BootStrap 공홈](https://getbootstrap.com/)
    - 부트스트랩 적용, 베이스 페이지 구성
        -  [Download](https://getbootstrap.com/docs/5.3/getting-started/download/) >> 압축해제
        - static 폴더 하위 파일 위치
            - bootstrap.min.css(js)
        - [Snippets](https://getbootstrap.com/docs/5.3/examples/)
        - [무료 템플릿 사이트 추천](https://reumpang.tistory.com/149)
    - 디자인 적용 기준 설정
        - static 밑에 공통으로 사용 할 CSS(부트스트립 적용)
            - SASS를 사용하는 회사도 존재 >> CSS -> SASS
    - flask-bootstrap -> 2017년 이후로 업데이트 X
        - 부트스트랩 3.x 버전임 => 사용 X

# Form

    - 입력 폼 유효성 검사 및 비정상적인 루트로 접근 시 처리 방지
    - 웹 프로그램에서 FORM은 사용자에게 입력 양식을 편리하게 제공
    - 폼 모듈을 활용하여, 데이터 입력 필수 여부, 길이, 형식, 유효성, 컨트롤 기능
    - [flask-wtf](https://flask-wtf.readthedocs.io/en/1.0.x/)
        - pip install flask-wtf
        - 기본 구성
            - SECRET_KEY 필수 구성
            - CSRF ( Cross Site Request Forgery )
                - 사용자의 요청을 위조하여 웹 사이트를 공격하는 기법
                - CSRF 토큰을 웹페이지를 내려줄때 삽입해서 요청이 들어올때 그 값이 같이 요청을 타고 들어오게 처리
                    - 이 값이 요청에 존재하는 경우 ( 값 자체도 유효해야 함), 정상적인 루트로 진입했음을 인지
                    - <input type='hidden' name ='' value=''> 이 패턴을 잘 체크
                    - SECRET KEY 값 기반으로 해싱하여 토큰 생성
                        - 웹 상에서 가장 잘 지켜야 할 정보 -> SECRET_KEY룰 잘 관리 해야함

        - 실습
            - 환경설정(변수)를 세팅해서 SECRET_KEY를 관리
            - 방식
                - OS 레벨 설정
                - 파이썬 객체로 설정 (O)
                - 환경변수 파일로 설정
                    - Flask 객체가 로드하면서 세팅 (O)
                    - Flask를 가동하면서 세팅
                    - Key-Value, DB Connection 값 등...
            - 질문 폼 페이지 생성
                - url = ~/main/question(GET방식)
                - html = question.html
                    - base.html를 상속받아서 내부는 div로만 감싸둔다

# JWT 개요

    - JSON Web Tokens
    - 토큰 기반 인증 반식
    - 왜 나왔고, 기존대비 어떤 점이 유리한지는 2단계 기술사 표현
    - 세션에 고객정보를 담아서 보관하지 않고, 고객이 필요한 정보를 토큰에 저장해서 클라이언트가 보관( 방식에 따라서는 서버측에도 DB 보관), 이를 증명서 활용한다. (요청이 왔을때 권한이 있는지 점검)
    - 구성
        - header : 헤더, jwt 토큰 유형, 해시알고리즘 사용 정보 기록(RSA, SHA256, ...)
        - payload : 저장할 정보 -> 클라이언트 정보, 메타데이터, ...
        - signature : 서명, 헤더에서 지정한 알고리즘으로 + 플라스크의 Secret Key를 재료로 서명을 생성 (checksum)
    - 위험요소
        - 해커는 서버측의 시크릿을 탈취하면, jwt 정보를 해킹 할 수 있다.
        - 인증서의 시간이 길면(만료시간), 해석시간의 확률이 높아진다 (기한이 짧게 구성)
            - 문제점
                - 사용자는 빈번하게 로그인 -> 불편함, 오버헤드(서버측)
            - 해결책
                - 만료시간 연장 전략 혹은 리플레시토큰을 서버측을 저장해서 이를 기반으로 토큰 기간을 갱신 (2단계 진행)
    - 설치
        - pip install PyJWT bcrypt
    - 참고문헌
        - [📚 JWT 토큰 인증 이란? - 💯 이해하기 쉽게 정리](https://inpa.tistory.com/entry/WEB-%F0%9F%93%9A-JWTjson-web-token-%EB%9E%80-%F0%9F%92%AF-%EC%A0%95%EB%A6%AC)
        - [JWT 토큰 암호화 알고리즘 - HS256과 RS256](https://velog.io/@ddangle/JWT-%ED%86%A0%ED%81%B0-%EC%95%94%ED%98%B8%ED%99%94-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-HS256%EA%B3%BC-RS256)
        - [RS256, HS256 차이](https://hwannny.tistory.com/72)
        - [JWT(Json Web Token) 알아가기](https://brunch.co.kr/@jinyoungchoi95/1)
        - [암호화의 종류와 Bcrypt](https://velog.io/@yenicall/%EC%95%94%ED%98%B8%ED%99%94%EC%9D%98-%EC%A2%85%EB%A5%98%EC%99%80-Bcrypt)
        - [BCrypt 동작원리 파헤치기](https://wildeveloperetrain.tistory.com/175)
        - [bcrypt 사용시 encode(), decode()가 필요한 이유](https://medium.com/@likegondry/python-bcrypt-%EC%82%AC%EC%9A%A9%EC%8B%9C-encode-decode-%EA%B0%80-%ED%95%84%EC%9A%94%ED%95%9C-%EC%9D%B4%EC%9C%A0-85af32ee6835)

'''

# TODO 주석 활용

    - TODO
        - 해야할 작업
    - FIXME
        - 오작동, 버그가 발생되는 코드
    - HACK
        - 해결은 했으나, 개선점이 필요한 코드
    - XXX
        - 이 부분은 큰 문제점, 오류를 가지고 있다

# DB 연동

    - pool(풀링기법)
        - 백앤드 서버 가동 시, Backend - DB 간 일정량의 커넥션을 따라 맺어서
        - 큐(Queue: FIFO)에서 담아서 관리
        - 접속과 해제라는 반복 작업에 따른 응답시간지연원인을 제거, 일정량의 동접이 발생 시, 안정적인 처리 속도 제공
    - orm
        - 객체지향방식을 코드에서 DB 연동 및 처리등 관리
        - 원칙적으로 SQL을 몰라도 처리가능
            - DB Vendor가 교체되더라도 동일하게 작동
        - 단점
            - 쿼리가 최적화 되었다고 볼 수 없다 -> 기계적인 생성
        - 설치
            - pip install sqlalchemy flask-migrate
    - DB 생성
        - FLASK_APP=service 은 없어도 되는데, 이 앱은 app or wsfi로 시작하는 엔트리가 없어 별도로 지정해야된다.
        - flask --app service db init
            - sqllite : 소형 DB, 스마트폰에 사용되는 DB, DB 자동 생성 및 파일럿 형태에서 사용
            - mysql와 같은 DB(케이스별 상이)는 실제로는 생성 안됨
        - MAC)FLASK_APP=service flask db init
        - migrations 폴더가 새로 생성돈다
            - 내부는 자동으로 만들어지는 구조이므로, 관려하지 않음
            - 단 versions 밑으로 수정할때마다 새로운 버전 DB 관련 생성
        - 모델(테이블) 생성, 변경
            - model > models.py에 테이블 관련 내용 기술
            - service> __init.py
                - !!! from .model import models : 주석해제, 신규작성 !!!
            - flask --app service db migrate
        - 모델(테이블) 생성, 변경 후 DB 적용
            - flask --app service db upgrade
        - 컨테이너 이미지 생성 시
            - 위 명령들을 차례대로 수행해서 DB 초기화, 생성과정 수행

    - 필요한 기능들 시뮬레이션
        - DBA는 sql문을 작성해서 쿼리 구현
        - ORM는 shell을 열어 파이썬 코드로 구현
            - Flask --app service shell
                - 질문 등록 (Insert)
                    ```
                    from service.model.models import Question, Answer
                    from datetime import datetime
                    q1 = Question(title="질문1", content="내용1", reg_dat
                    e = datetime.now())
                    from service import db
                    db.session.add(q1)
                    db.session.commit()
                    ```
                - 질문 조회
                   ```
                   # 전체 데이터 조회 : select * from question;
                   qs = Question.query.all()
                   ```
                   # 일부 데이터 조회 : select * from question where
                   qs[0].title >> '질문1'
                   qs[0].id >>  1
                   # id값을 넣어서 조회 : select * from question where id =1;
                   Question.query.get(1)

                   # 내용 중 '용' 문자열이 존재하면 다 가져오시오 : select * from question where content like '%용%';
                   Question.query.filter( Question.content.like('%용%')).all()

                - 질문 수정
                    ```
                    >>> q1 = Question.query.get(1)
                    # 변경하고 싶은 부분만 수정
                    # update question set title ='질문1을 변경' where id = 1;
                    >>> q1.title = "질문1을 변경"
                    >>> db.session.commit()
                    ```
                - 질문 삭제
                    ```
                    q1 = Question.query.get(1)
                    # delete from question where id = 1;
                    db.session.delete(q1)
                    de.session.commit()
                    ```
                - 답변 등록
                   ```
                        # 질문 2개 추가
                        >>> q1 = Question(title="질문1", content="내용1", reg_date = datetime.now())
                        >>> q2 = Question(title="질문2", content="내용2", reg_date = datetime.now())
                        >>> db.session.add(q1)
                        >>> db.session.add(q2)
                        >>> db.session.commit()

                        # 질문 1개를 찾고 답변을 등록
                        >>> q2 = Question.query.get(2)
                        >>> q2.title
                        '질문1'
                        >>> a = Answer(question=q2, content='질문1에 대한 답변', reg_date=datetime.now())
                        >>> db.session.add(a)
                        >>> db.session.commit()

                        # 답변을 통해서 질문 찾기 & 질문을 통해서 답변 찾기
                        ```
                            >>> a.question
                            <Question 2>
                            >>> q2.answer_set # 역 참조의 이름을 사용하여 답변들을 다 찾아온다 [backref=db.backref('answer_set')]
                            [<Answer 1>]
                        ```
                        # 질문을 삭제하면 답변도 다 삭제되는가? -> No
                        db.session.delete(q2)
                        db.session.commit()

                        # 답변의 참조 question id 값만 NULL
                        # 작성자가 서로 다르므로, 삭제 권리는 없고, 참조만 제거됨
                        +----+-------------+--------------------------+---------------------+
                        | id | question_id | content                  | reg_date            |
                        +----+-------------+--------------------------+---------------------+
                        |  1 |        NULL | 질문1에 대한 답변        | 2023-04-05 13:14:23 |
                        +----+-------------+--------------------------+---------------------+

                        # 본인 답변 삭제
                        db.session.delete(a)
                        db.session.commit()

                   ```
