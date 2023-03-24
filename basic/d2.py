"""
    - DB 접속 후 쿼리 수행
"""

import pymysql

connection = None

try:
    connection = pymysql.connect(
        host="localhost",
        # port = 3306,
        user="root",
        password="1q2w3e4r",
        database="ml_db",
        # 조회 결과는 [ {}, {}, {}, ...] >> 이런 형태로 추출된다
        # 사용 안하면 [ (,), (,), ...] 이런 형태로 나옴
        # cursorclass = pymysql.cursors.DictCursor
    )

    # 쿼리 수행
    # pymysql은 커서를 획득해서 쿼리를 수행한다 -> Rule
    # 1. 커서 획득 ( 이런식도 가능 )
    # connection.cursor(cursor=pymysql.cursors.DictCursor)
    with connection.cursor() as cursor:
        # 2. sql문 준비
        sql = """
        SELECT 
            uid, `name`, regdate
        FROM 
            users
        WHERE 
            uid = 'guest'
        AND
            upw = '1234';
        """
        # 3. sql 쿼리 수행
        cursor.execute(sql)

        # 4. 결과 획득
        row = cursor.fetchone()

        # 5. 결과 확인 -> 튜플 : 이름만 추출하시오 -> 순서가 중요, 인덱싱 -> '게스트'
        # 튜플로 결과를 받는 것은 결과값의 순서가 바뀌지 않는다는 전제로는 가능
        # 유연하게 대체하고 싶다면, 컬러 순서가 변경되든, 쿼리문의 순서가 변경되던지 -> 관게 X
        # 순서 없는 자료구조 -> 딕셔너리!! -> d3.py로 이동하여 계속
        print(row[1])
        pass


except Exception as e:
    print("접속 오류", e)

else:
    print("접속시 문제 없었음")

finally:
    # 2. 접속 종료 (I/O)-> close()
    if connection:
        connection.close()
