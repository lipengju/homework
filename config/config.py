#!/usr/bin/env python 
#-*- coding:utf-8 -*-

import  os,sys


BASE_DIR=os.path.dirname(os.path.dirname(__file__))

BASE_ADMIN_DIR=os.path.join(BASE_DIR,'db','admin')
TEACHER_DB_DIR=os.path.join(BASE_DIR,'db','teacher_list')
COURSE_DB_DIR=os.path.join(BASE_DIR,'db','course_list')

print(BASE_ADMIN_DIR)
print(TEACHER_DB_DIR)
print(COURSE_DB_DIR)


