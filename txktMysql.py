# -*-coding:utf-8 -*-
"""
@author:戎兴瑞
@file:txktMysql.py
@time:2022/11/3 15:13
"""
import pymysql
from Txktspiders import settings
# 建立mysql连接
sqlConnect = pymysql.connect(
    host = settings.Mysql_host,
    user = settings.Mysql_user,
    passwd = settings.Mysql_pwd,
    db = settings.Mysql_db,
    port = settings.Mysql_port
)
# 建立游标
cur = sqlConnect.cursor()
class Sql():
    # 创建表（create）
    @staticmethod
    def create_table():
        str = 'CREATE TABLE txkt(id int  auto_increment primary key , uname varchar(255), info varchar(255));'
        cur.execute(str)
        sqlConnect.commit()
        pass

    # 插入数据（insert）
    @staticmethod
    def insert_txkt(date):
        str = 'insert into txkt(uname,info) values("%s","%s");' % (
        date['name'], date['info'])
        cur.execute(str)
        sqlConnect.commit()
