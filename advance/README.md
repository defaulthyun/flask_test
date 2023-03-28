# Flask Entry Point : step1_flask_run
    - 서버에 운영되는 방식에 맞춰 구성
    - 명령어 조정 : Flask 명령어 사용
    - flask --app start_app -- debug run

# 애플리케이션 팩토리
    - 플라스크 객체 관리 및 중복 참조를 배제하기 위한 구성

# BluePrint
    - 사이트, 주제별 페이징 분할 처리

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
    

# 입력 폼 유효성
    - 계획된 루트가 아닌 방식으로 진입 시 이를 리젝하는 처리(보안기능)
    - 입력폼 관리 및 구성 -> WTF를 적용 

# 로그인 및 세션 관리 기본
    - JWT 활용한 인증방식, 세션관리
        - 1단계 토큰 비교
            -> 토큰 만료시간을 짧게 줘서 관리하는 방법
# DB 관련
    - Pooling 처리 
    - ORM 처리
    - Migrate 모듈을 활용하는 방식 ( 테이블 생성도 Flask에서 진행)

# REST API 구성

# 문서화
    - swagger_ui

# 로그인 및 세션 관리 응용
    - JWT 활용한 인증방식, 세션관리
        - 2단계 redis db(Nosql, key-value)
            - 인증토큰(짧은 만료), 리플레시토큰(긴 만료)
    - 암호화 모듈을 사용한 비밀번호 관리

# Traffic 용량 제한 처리
    - rate_limit 모듈 활용



