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
        cursorclass=pymysql.cursors.DictCursor,
    )

    with connection.cursor() as cursor:
        # cursor는 with문을 벗어나면 자동으로 닫힘
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

        cursor.execute(sql)

        row = cursor.fetchone()

        # 5. 결과 확인 -> 딕셔너리 : 이름만 추출하시오 -> 순서가 중요, 인덱싱 -> '게스트'
        print(row["name"])
        pass


except Exception as e:
    print("접속 오류", e)

else:
    print("접속시 문제 없었음")

finally:
    # 2. 접속 종료 (I/O)-> close()
    if connection:
        connection.close()
