# 파이썬 기반 웹 프로그래밍

# Flow
    - 단계
        - 기획 및 목표
        - 스토리보드
        - 디자인 시안, DB모델링, 프로토타입 구현(끝까지 가 본다)
        - Frontend
            - 디자인 진행(페이지 단위 계산), HTML/CSS/JS 처리
            - React or Vue or Augular : 전면, 부분 구성
        - Backend
            - 기능별 구현
                - 페이지 별 진행
                - 모델 서빙 (ML/DL) 기능 추가
                - 데이터 분석, 시각화 -> 파이썬 기반 웹에서 가지는 장점(같은 파이썬 언어로 구성되었으므로)
            - 공통 기능 구현
                - 통신 프로토콜 구현 : Request & Receive
        - DBA
            - DB설계 및 Table 구성
            - Query문 작성

    - 웹 환경 이해 및 프로그램 구성 이해
    - Flask 기반 웹 기반 백앤드(서버) 프로그래밍
    - BluePrint을 이용한 기능별 분할 구성
        - 회원관련 업무(가입, 로그인, 로그아웃, 회원탈퇴, 세션, 쿠키) 
        - 모델 서빙 파트(데이터 전처리, 모델 예측 수행, 응답처리)
        - DB관련 업무(DBMS 준비, SQL, ORM 준비, API 준비)
    - DB 연동 (SQL, ORM, ...)
    - 배포 및 운영
# 발전적 목표
- 머신러닝(딥러닝) 모델 서빙 및 서비스 구현
- 구축된 서비스를 도커 및 쿠버네티스 기반 하에서 운영
- MLOps에 연동하여 사용

# 가상환경 구축
    - 순수 파이썬으로 구축
        - 가상환경을 모아두는 폴더 생성 
            - mkdir venvs
        - 해당 폴더로 이동
            - cd venvs
        - 가상환경 생성 
            - python -m venv 가상환경이름 (flask_test)
    - 가상환경 활성화 시키는 파일 위치까지 이동
        - cd ./flask_test/Scripts
    - 가상환경 활성화
        - activate(Window) or . activate(Mac, Linux)
    - 최종 프롬포트 형태
        - (flask_test) : 윈도우
        - (flask_test) $ : 맥/리눅스 사용자 계정
        - (flask_test) # : 맥/리눅스 루트 계정

    - 아나콘다, 미니콘다 환경으로 구성

# 필요한 패키지 설치
    - requirements.txt 생성
    - 작성
        - 수동
            - 직접 기입
            - 패키지 == 버전
        - 자동 
            - 개발이 다 종료된 후 개발중에 생성 될 시 패키지가 이미 일부 설치되거나 전부 설치, 전혀 설치가 안되어도 자동으로 설치 
            - pip freeze > requirement.txt
    - 설치
        - pip install 패키지명
        - pip install -r requirement.txt
    - 번외
        - pip를 수행하면 command와 option 안내가 나와 다양한 기능 소개
            - ex) pip show Flask

# DB 연동
- 1단계 코드 : 요청시 디비 접속, 쿼리 수행, 접속 해제 => 접속/해제 반복으로 인한 속도 저하문제 존재, 접속이 몰리면 서비스 지연 문제 발생, 다만 쉽게 구현 가능
- 2단계 코드 : 서버 가동시 sqlalchemy Pool을 이용하여 동접수를 계산하여 커넥션을 생성, 요청시 -> 풀에서 커넥션 획득 -> 쿼리 수행 -> 커넥션 반납
서버 종료시 Pool에 있는 모든 커넥션 해제(반납)
- 3단계 코드 : flask-migrate -> sqlalchemy -> ORM을 이용하여 객체지향적으로 쿼리 수행
    - SQL 몰라도 됨 -> 자동 생성, DB 제품이 변경되도 동일하게 작동 
