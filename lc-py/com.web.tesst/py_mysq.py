import pymysql

def main():
    con = pymysql.connect(host="localhost", port=3306, database="yq", charset="utf8", user="root", password="123456")
    try:
        with con.cursor() as cursor:
            # 3. 通过游标执行SQL并获得执行结果
            result = cursor.execute(
                'insert into tb_dept values (%s, %s, %s)',
                (1, "zx", "aa")
             )
            if result == 1:
                print("添加成功")
            con.commit()
    finally:
        con.close()


if __name__ == '__main__':
    main()