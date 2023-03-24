"""
    DB 접속 후 쿼리 수행 > 파라미터 전달
"""

import pymysql


def select_login():
    connection = None

    try:
        connection = pymysql.connect(
            host="localhost",
            # port = 3306,
            user="root",
            password="1q2w3e4r",
            database="ml_db",
            cursorclass=pymysql.cursors.DictCursor,
        )

        with connection.cursor() as cursor:
            # 파라미터는 %s표시로 순서대로 세팅된다. '값' -> ''는 자동으로 세팅된다.
            sql = """
            SELECT 
                uid, `name`, regdate
            FROM 
                users
            WHERE 
                uid = %s
            AND
                upw = %s;
            """

            # execute() 함수의 2번 인자가 파라미터 전달하는 처리, 튜플로 표현

            cursor.execute(sql, ("guest", "1234"))
            row = cursor.fetchone()

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


if __name__ == "__main__":
    # d4 개발자의 테스트 코드
    # 타 개발자가 사용 할 때는 작동안함
    select_login()
