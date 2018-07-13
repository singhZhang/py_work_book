'''
生成激活码，并将激活码保存到redis
'''

import uuid
import redis


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


def save_redis( code ):
    '''
    保存数据到redis，以 list的形式存储
    :param code:
    :return:
    '''

    r = redis.Redis(
        host='127.0.0.1',
        port=6379
    )

    r.lpush('code', code)



if __name__ == '__main__':

    codes = getCode(20, 100)

    for item in codes:

        print(item)

        save_redis( item )

