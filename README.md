# 파이썬 기반 웹 프로그래밍

# 목표
    - 웹 환경 이해 및 프로그램 구성 이해
    - Flask 기반 웹 기반 백앤드(서버) 프로그래밍
    - BluePrint을 이용한 기능별 분할 구성
    - DB 연동 (SQL, ORM)
    - 배포 및 운영
# 발전적 목표
- 머신러닝(딥러닝) 모델 서빙 및 서비스 구현
- 구축된 서비스를 도커 및 쿠버네티스 기반 하에서 운영
- MLOps에 연동하여 사용

# 가상환경 구축
    - 파이썬으로 구축
        - 가상환경을 모아두는 폴더 생성 
            - mkdir venvs
        - 해당 폴더로 이동
            - cd venvs
        - 가상환경 생성 
            - python -m venv 가상환경이름 (flask_test)
    - 가상환경 활성화 하는 명령어 위치까지 이동
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
            - 개발이 다 종료된 후, 개발중에 생성된다면
            - pip freeze > requirement.txt
    - 설치
        - pip install 패키지명
        - pip install -r requirement.txt

