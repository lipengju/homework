#!/usr/bin/env python 
#-*- coding:utf-8 -*-

import  os,sys


BASE_DIR=os.path.dirname(os.path.dirname(__file__))

BASE_ADMIN_DIR=os.path.join(BASE_DIR,'db','admin')
BASE_STUDENT_DIR=os.path.join(BASE_DIR,'db','student')
TEACHER_DB_DIR=os.path.join(BASE_DIR,'db','teacher_list')
COURSE_DB_DIR=os.path.join(BASE_DIR,'db','course_list')
LOG_DIR=os.path.join(BASE_DIR,'log','log.md')

print(LOG_DIR)
