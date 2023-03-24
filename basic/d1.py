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
    
    6. 테이블 변경
    ALTER TABLE `users`
	CHANGE COLUMN `uid` `uid` VARCHAR(32) NOT NULL COMMENT '고객 로그인 ID' COLLATE 'utf8mb4_general_ci' AFTER `id`,
	CHANGE COLUMN `upw` `upw` VARCHAR(128) NOT NULL COMMENT '고객 로그인 PW' COLLATE 'utf8mb4_general_ci' AFTER `uid`,
	CHANGE COLUMN `name` `name` VARCHAR(32) NOT NULL COMMENT '고객 이름' COLLATE 'utf8mb4_general_ci' AFTER `upw`,
	CHANGE COLUMN `regdate` `regdate` TIMESTAMP NOT NULL DEFAULT current_timestamp() COMMENT '고객 가입일' AFTER `name`;

"""

import pymysql as my
