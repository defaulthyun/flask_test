"""
    DB 접속 후 쿼리 수행 > 파라미터 전달
"""

import pymysql


def select_login(uid, upw):
    """
            아이디, 비밀번호를 넣어서 회원여부를 체크하는 함수
            parameter
                - uid : 아이디
                - upw : 비밀번호
            returns
                - 회원일 경우
                    - {'uid': 'guest', 'name': '게스트', 'regdate': datetime.datetime(2023, 3, 24, 13, 3, 15)}
    접속시 문제 없었음
                - 비회원일 경우, DB 오류
                    - None
    """
    connection = None
    row = None  # 로그인 쿼리 수행 결과를 담는 변수

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

            cursor.execute(sql, (uid, upw))
            row = cursor.fetchone()  # 결과셋 중 한개만 가져온다 -> 단추(리스트가 아닌 단독타입 : 딕셔너리)
            # print(row["name"])
            pass

    except Exception as e:
        print("접속 오류", e)

    else:
        print("접속시 문제 없었음")

    finally:
        if connection:
            connection.close()
    # 로그인 결과를 리턴 -> ( ... )
    return row


if __name__ == "__main__":
    # d4 개발자의 테스트 코드
    # 타 개발자가 사용 할 때는 작동안함
    # 정상 계정, 비정상 계정
    print(select_login("guest", "1234"))
    print(select_login("g", "1"))
