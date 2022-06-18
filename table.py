#!/usr/bin/python3
# -*- coding: UTF-8 -*-
'''
file  : table.py
date  : 20220128
author: yingji
desc  : 连接数据库,读取表及表字段基本信息
'''

import pymysql
from config import *


class Field(object):
    # name = ""  # 字段名
    # data_type = ""  # 数据类型
    # comment = ""  # 字段描述
    # is_pk = False  # 主键标识
    # which_table = ""  # 归属表名

    def __init__(self, name, data_type,default, comment, is_pk, which_table):
        self.name = name
        self.data_type = data_type
        self.default = default
        self.comment = comment
        self.is_pk = is_pk
        self.which_table = which_table

class DbIndex:
    '''
    数据库索引对象
    '''
    def __init__(self) -> None:
        self.name = "" # 索引名称
        self.unique_flag = False # 唯一索引
        self.column_name_list = [] # 索引字段名称 按字段序号排序

class Table(object):
    def __init__(self, table_info):
        self.name = table_info[0]
        self.comment = table_info[1]
        self.fields = []
        self.unique_index = []
        self.index_dict = {} #  {"key_name":["DbIndex"]}
        _unique_index = self.ShowUniqueIndexFromDB(self.name)
        for index in _unique_index:
            if index[2] == 'F_org_code':
                self.unique_index.append(index[4].replace('F_', ''))

            # 初始化index_dict
            key_name = index[2]
            column_name = index[4]
            if key_name not in self.index_dict.keys():
                self.index_dict[key_name] = DbIndex()

            self.index_dict[key_name].name = key_name
            if index[1] == 0: self.index_dict[key_name].unique_flag = True
            self.index_dict[key_name].column_name_list.append( column_name )

        for record in self.ShowFieldsFromDB(self.name):
            print(record)
            is_pk = False
            if record[4] == "PRI":
                is_pk = True
            if record[0] != 'id':
                print(record)
                self.fields.append(Field(record[0], record[1], record[5], record[8], is_pk, table_info))

    @staticmethod
    def ShowFieldsFromDB(name):
        db = pymysql.connect(host=IP,
                             port=PORT,
                             user=USERNAME,
                             password=PASSWORD,
                             database=DATABASE,
                             charset="utf8")
        cursor = db.cursor()
        # 获取表的所有字段信息
        '''
        mysql字段定义类：show full fields from name
        字段信息格式如下
        Field: Fdevice_id
        Type: int
        Collation: NULL
        Null: NO
        Key: PRI
        Default: NULL
        Extra: auto_increment
        Privileges: select,insert,update,references
        Comment: 设备id
        '''
        sql = "show full fields from %s" % name
        cursor.execute(sql)
        records = cursor.fetchall()
        db.close()
        return records

    @staticmethod
    def show_table(name):
        db = pymysql.connect(host=IP,
                             port=PORT,
                             user=USERNAME,
                             password=PASSWORD,
                             database=DATABASE)
        cursor = db.cursor()
        sql = f"""
        SELECT
            TB.TABLE_NAME,      -- 表名
            TB.TABLE_COMMENT   -- 表名注释
        FROM
            INFORMATION_SCHEMA.TABLES TB
        Where TB.TABLE_SCHEMA = '{name}' -- 数据库名
        """
        cursor.execute(sql)
        records = cursor.fetchall()

        db.close()

        return records

    @staticmethod
    def ShowTables():
        db = pymysql.connect(host=IP,
                             port=PORT,
                             user=USERNAME,
                             password=PASSWORD,
                             database=DATABASE)
        cursor = db.cursor()
        sql = "show tables"
        cursor.execute(sql)
        records = cursor.fetchall()

        db.close()

        return records

    @staticmethod
    def ShowUniqueIndexFromDB(table_name):
        db = pymysql.connect(host=IP,
                             port=PORT,
                             user=USERNAME,
                             password=PASSWORD,
                             database=DATABASE)
        cursor = db.cursor()
        sql = f"show index from {table_name}"
        cursor.execute(sql)
        records = cursor.fetchall()

        db.close()

        return records


class Table_init(object):
    def __init__(self, name):
        self.name = name
