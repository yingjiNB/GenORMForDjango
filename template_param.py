#!/usr/bin/python3
# -*- coding: UTF-8 -*-
'''
file  : template_param.py
date  : 20220128
author: yingji
desc  : 模板参数
'''

class TemplateParam(object):
	def __init__(self, out_file_name, out_file_desc, param_obj):
		self.out_file_name = out_file_name
		self.out_file_desc = out_file_desc
		self.param_obj     = param_obj

	@staticmethod
	def get_camel_style_name(name):
		if name != None:
			tmp = ""
			segs = name.split('_')
			for seg in segs:
				part = ( seg[0].upper() + seg[1:len(seg)] if len(seg) >= 1 else seg )
				tmp = tmp + part
			return tmp
		return name
