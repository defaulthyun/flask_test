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

