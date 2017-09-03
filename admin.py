#!/usr/bin/env python 
#-*- coding:utf-8 -*-

"""
选课系统:
管理员：
     创建老师：姓名，性别，年龄，资产
     创建课程：课程名称，上课时间，课时费，关联老师
     使用pickle保存在文件中
学生：
    学生：用户名，密码，性别，年龄，选课列表，上课记录
    1、列举所有课程
    2、选择课程
    3、学生上课
    4、ret=课程.work()获取课程的返回
    资产+=课时费
"""

import  random
import  time
import  pickle
import os
import  sys
from lib import  models
from config import  settings




def create_teacher(admin_obj):
	'''
	创建老师
	:param admin_obj: 创建老师的对象管理员(老师是管理员创建的)
	:return:
	'''
	teacher_list=[]
	while True:
		teacher_name=input('请输入老师姓名(q表示退出):\n')
		if teacher_name=='q':
			break
		teacher_age=int(input('请输入老师年龄:\n'))
		teacher_obj=models.Teacher(teacher_name,teacher_age,admin_obj)
		teacher_list.append(teacher_obj)
		#判断老师是否存在,如果存在,就更新信息，如果不存在，就创建
		if os.path.exists(settings.TEACHER_DB_DIR):
			exists_teacher_list=pickle.load(open(settings.TEACHER_DB_DIR, 'rb'))
			#批量更新数据(批量添加数据)
			teacher_list.extend(exists_teacher_list)
		pickle.dump(teacher_list, open(settings.TEACHER_DB_DIR, 'wb'))

def create_course(admin_obj):
	'''
	管理员创建课程
	:param admin_obj:创建课程的对象是管理员（课程是管理员创建的）
	:return:
	'''
	#管理员创建课程前，先把老师全部列出来
	teacher_list=pickle.load(open(settings.TEACHER_DB_DIR, 'rb'))
	for num,item in enumerate(teacher_list,1):
		print(num,item.name,item.age,item.create_time,item.create_admin.username)
		#创建课程对象,创建课程列表
	course_list=[]
	while True:
		course_name=input('请输入课程(q表示退出):\n')
		if course_name=='q':
			break
		course_cost=float(input('请输入课时费:\n'))
		course_teacher_num=int(input('请选择老师(通过序号选择老师):\n'))
		course_obj=models.Course(course_name,course_cost,teacher_list[num-1],admin_obj)
		course_list.append(course_obj)
		#判断课程是否存在，如果存在，就更新，如果不存在，就创建
		if os.path.exists(settings.COURSE_DB_DIR):
			exists_course_list=pickle.load(open(settings.COURSE_DB_DIR, 'rb'))
			course_list.extend(exists_course_list)
		pickle.dump(course_list, open(settings.COURSE_DB_DIR, 'wb'))



def login(username,password):
	'''管理员的登录方法'''
	# 登录前判断管理员账号是否存在
	if os.path.exists(username):
		admin_obj = pickle.load(open(username, 'rb'))
		# 对登录判断，登录成功是返回true，失败是false
		if admin_obj.login(username, password):
			print('恭喜您，登录成功！')
			while True:
				#管理员登录成功,创建老师或者创建课程
				inp=int(input('1、创建老师；2、创建课程；\n'))
				if inp==1:
					create_teacher(admin_obj)
				elif inp==2:
					create_course(admin_obj)
				else:
					break
		else:
			print('Sorry，账号或者密码错误')
	else:
		print ('Sorry,用户不存在')
		inp=input('是否注册Y/N？\n')
		if inp=='Y' or inp=='y':
			register(username,password)
			print('register success!')
			inp=input('是否登录Y/N?\n')
			if inp=='Y' or inp=='y':
				login(username,password)
			else:
				sys.exit()
		elif inp=='N' or inp=='n':
			sys.exit(1)


def register(username,password):
	'''管理员的注册方法'''
	admin_obj = models.Admin()
	admin_obj.register(username, password)


def main():
	inp=int(input('1、管理员登录；2、管理员注册；\n'))
	username = input('请输入管理员用户名:\n')
	password = input('请输入管理员密码:\n')
	if inp==1:
		login(username,password)
	elif inp==2:
		register(username,password)
		inp=input('是否登录y/n？\n')
		if inp=='y':
			login(username,password)
		else:
			sys.exit(1)
	else:
		sys.exit(1)


if __name__=='__main__':
	main()