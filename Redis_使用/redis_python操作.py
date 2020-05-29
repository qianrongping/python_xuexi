# encoding = utf-8
import redis

if __name__ == '__main__':
    try:
        rs = redis.Redis(host='localhost', port=6379,
                         db=0, password=123456)
    except Exception as e:
        print(e)

    # 操作string
    # 添加
    result = rs.set("name", "rubin1")
    print(result)

    # 获取
    name = rs.get("name")
    print(name)
