import pymysql
import xlrd
import time

t1 = time.time()
print("开始了")

db = pymysql.connect(host='127.0.0.1',
                     port=3306,
                     user='root',
                     password='123456',
                     database= 'test1',
                     charset='utf8')
cur = db.cursor()
ex = xlrd.open_workbook("类别.xls")
sheet = ex.sheet_by_index(0)
rows = sheet.nrows
cols = sheet.ncols

# 跳过第一行的标题,直接从第二行开始
for row_num in range(1, rows):
    data = tuple(sheet.row_values((row_num, 0)[0]))
    type_name, type_name_cn, = data
    # print(materiel_code, materiel_name, materiel_spec, materiel_type, use_company, purchase_price, category_id, procedure_id, composition_id, memo)
    sql = """insert into
                z_goods_type(type_name, type_name_cn)
            value
            ('%s','%s')""" % (type_name, type_name_cn)
    try:
        # 执行sql语句
        cur.execute(sql)
        # 提交数据到数据库
        db.commit()
        print(f"成功了", type_name_cn)

    except Exception as e:
        # 对修改失败的数据进行撤销,表示回滚
        db.rollback()
        print(f"失败了", type_name_cn)
        print(e)

# 关闭游标
cur.close()
# 关闭连接
db.close()
t2 = time.time()
print(t2 - t1)
