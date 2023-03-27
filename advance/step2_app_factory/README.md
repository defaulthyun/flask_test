# 어플리케이션 팩토리
    - 엔트리 위치 조정, 코드 수정
    - app = Flask(__name__)
        - 현재 작성 한 이코드는 전역변수로 존재
        - 프로젝트의 규모가 커질 시 순환 참조를 활 확률이 높음
        - flask 구현 시 어플리케이션 팩토리라는 형태로 사용하라 => 권장
#  방법
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
            

