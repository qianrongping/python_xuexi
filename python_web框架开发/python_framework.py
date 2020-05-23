"""web框架的职责专门负责处理动态资源请求"""
import time
import pymysql
import json

# 路由列表
route_list = [
    # ("/index.html", index),
    # ("center.html", center)
]


# 定义带有参数的装饰器
def route(path):
    # 装饰器
    def decorator(func):
        # 当执行装饰器启动时候就需要把路由添加到路由列表里面
        # 当装饰函数的 时候 只添加一次路由即可
        route_list.append((path, func))

        def inner():
            result = func()
            return result

        return inner

    # 返回一个 装饰器
    return decorator


@route("/index.html")
def index():
    # 状态信息
    status = "200 OK"
    # 响应头信息
    response_header = [("Server", "PWS/1.1")]

    # 1. 打开指定模板文件,读取模板文件中的数据
    with open("template/index.html", "r", encoding='utf-8') as file:
        file_data = file.read()
    # 2. 查询数据库,模板里面的变量{%content%} 替换成以后从数据库里面查询的数据
    conn = pymysql.connect(host='localhost',
                           port=3306,
                           user='root',
                           password='123456',
                           database='stock_db',
                           charset='utf8')
    # 获取游标
    cursor = conn.cursor()
    sql = "select * from info;"
    # 执行sql语句
    cursor.execute(sql)
    result = cursor.fetchall()
    print(result)
    # 关闭游标
    cursor.close()
    # 关闭连接
    conn.close()

    # 遍历每一条数据,完成数据的tr标签的封装
    data = ""
    for row in result:
        data += """<tr>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td><input type="button" value="添加" id="toAdd " name="toAdd" systemidvaule="000007"></td>
        </tr>
        """ % row

    response_body = file_data.replace("{%content%}", data)
    return status, response_header, response_body


# 个人中心数据接口
@route("/center_data.html")
def center_data():
    conn = pymysql.connect(host='localhost',
                           port=3306,
                           user='root',
                           password='123456',
                           database='stock_db',
                           charset='utf8')
    # 获取游标
    cursor = conn.cursor()
    sql = '''SELECT i.code, i.short, i.chg, i.turnover, i.price, i.highs, f.note_info
            FROM info i INNER JOIN focus f
            ON i.id = f.info_id;
            '''
    # 执行sql语句
    cursor.execute(sql)
    result = cursor.fetchall()
    print(result)
    # 把元组转成列表字典(列表推导式)
    center_data_list = [{
        "code": row[0],
        "short": row[1],
        "chg": row[2],
        "turnover": row[3],
        "price": str(row[4]),
        "highs": str(row[5]),
        "note_info": row[6],
    } for row in result]
    # 把列表转成字符串数据
    # ensure_ascii=False 在控制台显示中文
    json_str = json.dumps(center_data_list, ensure_ascii=False)

    # 关闭游标
    cursor.close()
    # 关闭连接
    conn.close()

    # 状态信息
    status = "200 OK"
    # 响应头信息
    response_header = [("Server", "PWS/1.1"),
                       ("Content-Type", "text/html;charset=utf-8")]
    return status, response_header, json_str


@route("/center.html")
def center():
    # 状态信息
    status = "200 OK"
    # 响应头信息
    response_header = [("Server", "PWS/1.1")]

    # 1. 打开指定模板文件,读取模板文件中的数据
    with open("template/center.html", "r", encoding='utf-8') as file:
        file_data = file.read()
    # 2. 查询数据库,模板里面的变量{%content%} 替换成以后从数据库里面查询的数据
    # web处理后的数据
    # 当前时间
    # data = time.ctime()
    response_body = file_data.replace("{%content%}", "")
    return status, response_header, response_body


# 处理没有找到的动态资源
def not_found():
    # 状态信息
    status = "404 Not Found"
    # 响应头信息
    response_header = [('Server', 'PWS/1.1')]
    # web处理后的数据
    # 当前时间
    data = 'Not Found'
    return status, response_header, data


# 处理动态资源请求
def handle_request(env):
    # 获取动态的请求资源路劲
    request_path = env['request_path']
    print("动态资源请求的地址:", request_path)

    for path, func in route_list:
        if request_path == path:
            # 找到了指定路由,返回对应的处理函数
            result = func()
            return result
    else:
        # 没有动态资源数据,返回404
        result = not_found()
        return result

    # # 判断请求的动态资源路径,选择指定的函数处理对应的动态资源请求
    # if request_path == "/index.html":
    #     result = index()
    #     # 把处理后的结果返回给web服务器使用,让web服务器拼接响应报文时使用
    #     return result
    # elif request_path == "/center.html":
    #     result = center()
    #     # 把处理后的结果返回给web服务器使用,让web服务器拼接响应报文时使用
    #     return result


# if __name__ == '__main__':
#     center_data()
