#!/usr/bin/python3
# -*- coding: UTF-8 -*-
'''
file  : gentbl
date  : 20220128
author: yingji
desc  : 连接数据库,读取表信息,生成表对应的api(c++)
'''

import sys
import os
import getopt
import copy
from mako.template import Template
from template_param import *

from config import * 
from table import *


def gen_code(table_name):
    table_info_tuple = Table.show_table(table_name)
    tableInit = Table_init(table_info_tuple)
    # __init__文件写入
    f_init = open(os.path.join(g_output_dir, "__init__.py"), 'wb+')
    init_temp = Template(filename=TEMP_INIT_PATH, input_encoding='UTF-8')
    f_init.write(init_temp.render(TEMPLATE_PARAM=tableInit).encode("utf-8"))
    f_init.close()
    del init_temp

    # 生成dbs文件
    for table_info in table_info_tuple:
        table = Table(table_info)
        fp = open(os.path.join(g_output_dir, table.name + ".py"), 'wb+')
        template = Template(filename=TEMP_FILE_PATH, input_encoding='UTF-8')
        fp.write(template.render(TEMPLATE_PARAM=table).encode("utf-8"))
        fp.close()
        del template
        
    # 生成dbs dto文件
    for table_info in table_info_tuple:
        table = Table(table_info)
        fp = open(os.path.join("./app/model", table.name + "_dto.py"), 'wb+')
        template = Template(filename=TEMP_DB_DTO_PATH, input_encoding='UTF-8')
        fp.write(template.render(TEMPLATE_PARAM=table).encode("utf-8"))
        fp.close()
        del template
        
    # 生成dbs dto文件
    for table_info in table_info_tuple:
        table = Table(table_info)
        fp = open(os.path.join("./app/model", table.name + "_mapper.py"), 'wb+')
        template = Template(filename=TEMP_DB_MAPPER_PATH, input_encoding='UTF-8')
        fp.write(template.render(TEMPLATE_PARAM=table).encode("utf-8"))
        fp.close()
        del template
        

    table_list = []
    table_name_sorted_list = sorted([table_name for table_name in table_info_tuple],key=lambda i: i)
    for table_info in table_name_sorted_list:
        table_list.append(Table(table_info))

    # fp = open(os.path.join("./../genapi/idl/", "mep_info_idl" + ".py"), 'wb+')
    # template = Template(filename=TEMP_INFO_PATH, input_encoding='UTF-8')
    # fp.write(template.render(TABLE_LIST=table_list).encode("utf-8"))
    # fp.close()
    # del template

    # 生成readme文件
    fp = open(os.path.join("./sql/", "README.md"), 'wb+')
    template = Template(filename=TEMP_README_PATH, input_encoding='UTF-8')
    fp.write(template.render(TABLE_LIST=table_list).encode("utf-8"))
    fp.close()
    del template

if __name__ == '__main__':
    gen_code(DATABASE)
