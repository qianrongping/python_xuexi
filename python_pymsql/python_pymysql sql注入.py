import pymysql

# 创建连接对象
conn = pymysql.connect(host='localhost',
                       port=3306,
                       user='root',
                       password='123456',
                       database='jing_dong',
                       charset='utf8')

# 获取游标
cursor = conn.cursor()

# sql注入
# sql = "select * from goods where name='%s';" % "商务双肩背包'or 1=1 or ' "


# 防止sql注入 就是将传参 参数化
sql = "select * from goods where name=%s;"
# 执行sql语句
cursor.execute(sql, '商务双肩背包')

# 获取数据  返回的结果是一个元组
# row = cursor.fetchone()  # 返回第一条数据

result = cursor.fetchall()
for row in result:
    print(row)

# 关闭游标
cursor.close()
# 关闭连接
conn.close()
