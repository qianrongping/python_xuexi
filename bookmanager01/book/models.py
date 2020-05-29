from django.db import models

# Create your models here.

"""
1.ORM
    表-->类
    字段-->属性

2. 模型类需要继承自models.Model

3.模型会自动为我们添加(生产)一个主键

4. 属性名 = 属性类型(选项)
        属性类型和 MySQL 相似
        选择:
        CharField: 必须设置 max_length
        null: 是否为空
        unique:唯一
        default: 设置默认值
        verbose_name: 主要是admin 后台显示
书籍表:
    id,name,pub_date,read_count,comment_count,is_del
"""


class BookInfo(models.Model):
    # 属性名 = 属性类型(选择)
    name = models.CharField(max_length=10, unique=True, verbose_name='名字')
    # 发布日期
    pub_date = models.DateField(null=True)
    # 阅读量
    read_count = models.IntegerField(default=0)
    # 评论量
    comment_count = models.IntegerField(default=0)
    # 是否逻辑删除
    is_del = models.BooleanField(default=False)

    # 改表名
    class Meta:
        db_table = 'bookinfo'
        # 修改admin的显示信息的配置
        verbose_name = 'admin'

    def __str__(self):
        return self.name


# 准备人物列表信息的模型类
class PeopleInfo(models.Model):
    GENDER_CHOICES = (
        (0, 'male'),
        (1, 'female')
    )
    name = models.CharField(max_length=20, verbose_name='名称')
    gender = models.SmallIntegerField(choices=GENDER_CHOICES, default=0, verbose_name='性别')
    description = models.CharField(max_length=200, null=True, verbose_name='描述信息')
    book = models.ForeignKey(BookInfo, on_delete=models.CASCADE, verbose_name='图书')  # 外键
    is_delete = models.BooleanField(default=False, verbose_name='逻辑删除')

    class Meta:
        db_table = 'peopleinfo'
        verbose_name = '人物信息'

    def __str__(self):
        return self.name
