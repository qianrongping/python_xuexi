import pymysql

if __name__ == '__main__':

    # 创建连接对象
    conn = pymysql.connect(host='localhost',
                           port=3306,
                           user='root',
                           password='123456',
                           database='jing_dong',
                           charset='utf8')

    # 获取游标
    cursor = conn.cursor()

    # sql = "insert into goods(name, cate_name,brand_name,price,is_show,is_saleoff)" \
    #       "value ('联想p7000','笔记本','联想','6999.00',1,0);"

    # sql = "update goods set price='7999.99' where name='联想p7000';"

    sql = "delete from goods where name='联想p7000';"
    try:
        # 执行sql语句
        cursor.execute(sql)
        # 提交数据到数据库
        conn.commit()
    except Exception as e:
        # 对修改失败的数据进行撤销,表示回滚
        conn.rollback()
    finally:
        # 关闭游标
        cursor.close()
        # 关闭连接
        conn.close()
