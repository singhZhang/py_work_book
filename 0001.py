'''
随机生成 200 个激活码，并保存到数据库中
'''

import uuid
import pymysql


def getCode(num , length=16):
    '''
    生成指定数量，指定长度的字符串，最长32位
    :param num: 生成数量
    :param length: 生成字符串的长度
    :return: list
    '''

    result = []

    while num > 0:

        uuid_id = uuid.uuid1()

        code = str(uuid_id).replace('-', '')[:length]

        if code not in result:

            result.append(code)

            num -= 1

    return result

def save_mysql( code ):
    '''
    保存数据到MySql
    :param code: 生成的字符串
    :return:
    '''

    conn = pymysql.connect(
        host='127.0.0.1',
        port=3306,
        user='root',
        passwd='root',
        db='py_project',
        charset="utf8"
    )

    try:

        with conn.cursor() as cursor:

            sql = "insert into `codes` (`code`) VALUES (%s)"

            cursor.execute(sql, code)

            conn.commit()

        with conn.cursor() as cursor:

            sql = "select * from `codes` where `code` = %s"

            cursor.execute(sql, code)

            result = cursor.fetchone()

            print(result)

    except Exception as e :

        print("Mysql Error: {0}".format(e))

    finally:
        conn.close()


if __name__ == '__main__':

    codes = getCode(200)

    for i in codes:

        save_mysql(i)