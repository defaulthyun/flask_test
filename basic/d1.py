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
    
    5. 고객 테이블 생성
    
    # USING BTREE : 검색 속도를 높이는 방식 중 하나로 특정 컬럼을 지정
    
    CREATE TABLE `users` (
        `id` INT(11) NOT NULL AUTO_INCREMENT COMMENT '고객 고유 관리 ID',
        `uid` VARCHAR(32) NOT NULL COMMENT '고객 로그인 ID' COLLATE 'utf8mb4_general_ci',
        `upw` VARCHAR(128) NOT NULL COMMENT '고객 로그인 PW' COLLATE 'utf8mb4_general_ci',
        `name` VARCHAR(32) NOT NULL COMMENT '고객 이름' COLLATE 'utf8mb4_general_ci',
        `regdate` TIMESTAMP NOT NULL DEFAULT current_timestamp() COMMENT '고객 가입일',
        PRIMARY KEY (`id`) USING BTREE,
        UNIQUE INDEX `id` (`id`) USING BTREE,
        UNIQUE INDEX `uid` (`uid`) USING BTREE
    )
    COMMENT='고객 테이블'
    COLLATE='utf8mb4_general_ci'
    ENGINE=InnoDB
    ;
    
    # 컬럼 추가 : ADD COLUMN
    # 컬럼 변경 : MODIFY COLUMN
    # 컬럼 이름 포함 변경 : CHANGE COLUMN
    # 컬럼 삭제 : DROP  COLUMN
    # 테이블 이름 변경 : RENAME
    # ALTER TABLE <테이블명> CHANGE COLUMN <OLD 컬럼> <NEW 컬럼> <데이터 타입> [FIRST|AFTER <컬럼명>]

    ALTER TABLE `users`
	CHANGE COLUMN `uid` `uid` VARCHAR(32) NOT NULL COMMENT '고객 로그인 ID' COLLATE 'utf8mb4_general_ci' AFTER `id`,
	CHANGE COLUMN `upw` `upw` VARCHAR(128) NOT NULL COMMENT '고객 로그인 PW' COLLATE 'utf8mb4_general_ci' AFTER `uid`,
	CHANGE COLUMN `name` `name` VARCHAR(32) NOT NULL COMMENT '고객 이름' COLLATE 'utf8mb4_general_ci' AFTER `upw`,
	CHANGE COLUMN `regdate` `regdate` TIMESTAMP NOT NULL DEFAULT current_timestamp() COMMENT '고객 가입일' AFTER `name`;

    6. 회원가입 -> insert
    - INSERT INTO [<DB명>.]<테이블명> (컬럼명, 컬럼명, ...) values (값, 값, ...);
    - `` : 키워드를 테이블명, 컬럼명등등 사용하면 벡틱를 통해 처리 가능
    INSERT INTO 
        `ml_db`.`users` 
            (`uid`, `upw`, `name`, `regdate`) 
        VALUES 
            ('guest', '1234', '게스트', now());    
    
    7. 회원 정보 수정 -> update
    
    8. 회원 탈퇴 -> delete
        - 1년간 보관, 완전 삭제?
    
    9. 로그인 -> select (쿼리의 분량이 가장 많다)
    -- 회원 가입 여부 조회 -> 로그인 처리 쿼리 
    -- 대소문자 구분이 안함 
    -- 제시한 ID, PW와 일치하는 row 데이터를 가져와서 uid, name, regdate 값을 출력하시오.
    SELECT 
        uid, `name`
    FROM 
        users
    WHERE 
        uid = 'guest'
    AND
        upw = '1234';
"""

import pymysql

connection = None

try:
    # 1. 접속
    connection = pymysql.connect(
        host="localhost",  # 127.0.0.1 (서버측)
        # port = 3306, # 포트
        user="root",  # 사용자 계정, root 계정 외 사용 권장
        password="1q2w3e4r",  # 비밀번호
        database="ml_db",  # 접속할 DB
        # cursorclass = pymysql.cursors.DictCursor
    )
    print("접속 성공")

except Exception as e:
    print("접속 오류", e)

else:
    print("접속시 문제 없었음")

finally:
    # 2. 접속 종료 (I/O)-> close()
    if connection:
        connection.close()
    print("접속 종료 성공")
