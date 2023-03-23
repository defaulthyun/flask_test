"""
    파이썬 <-> DB
    파이썬으로 DB를 엑세스하여, 쿼리문을 전송, 수행결과를 받아오는 방식
        - sql 수행
            - basic에서 수행
            - pymysql 페키지 셋팅
                - https://github.com/PyMySQL/PyMySQL
        - orm 수행
            - advance에서 수행
    업무 포지션은, 지원팀, 공용 API를 만드는 Part => 함수, 클래스 형태로 라이브러리 제공
    사용방법에 대한 예제까지 제공
    
    1. DB를 터미널을 통해서 접속
    $ mysql -u root -p
    
    2. DB 생성
    create database ml_db;
    
    3. DB 목록 출력(보여줘)
    show databases;
    
    4. 현재 작업 할 DB 지정
    use ml_db;
    
    
    
    
    
"""

import pymysql as my
