import pymysql
import xlrd
import time

t1 = time.time()
print("开始了")

db = pymysql.connect(host='8.129.186.89',
                     port=3306,
                     user='root',
                     password='db7b6a8392355c76',
                     database='wms',
                     charset='utf8')
cur = db.cursor()
ex = xlrd.open_workbook("deti.xls")
sheet = ex.sheet_by_index(0)
rows = sheet.nrows
cols = sheet.ncols

# 跳过第一行的标题,直接从第二行开始
for row_num in range(1, rows):
    data = tuple(sheet.row_values((row_num, 0)[0]))
    materiel_id, materiel_code = data
    # print(type(materiel_code))
    # print(materiel_code, materiel_name, materiel_spec, materiel_type, use_company, purchase_price, category_id, procedure_id, composition_id, memo)
    sql = """insert into
                materiel_detail(materiel_id,materiel_code)
            value
            ('%s', '%s')""" % (materiel_id, materiel_code)
    # print(sql)

    try:
        # 执行sql语句
        cur.execute(sql)
        # 提交数据到数据库
        db.commit()
        print(f"成功了", materiel_code)

    except Exception as e:
        # 对修改失败的数据进行撤销,表示回滚
        db.rollback()
        print(f"失败了", materiel_code)
        print(e)

# 关闭游标
cur.close()
# 关闭连接
db.close()
t2 = time.time()
print(t2 - t1)
