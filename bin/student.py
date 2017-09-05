#!/usr/bin/env python 
#-*- coding:utf-8 -*-

import  os,sys,pickle

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from lib import  models
from config import  settings

def login(username,password):
	'''学生登录'''
	if os.path.exists(os.path.join(settings.BASE_STUDENT_DIR,username)):
		#拿到用户名和密码对象来判断用户名和密码是否正确
		student_obj=pickle.load(open(os.path.join(settings.BASE_STUDENT_DIR,username),'rb'))
		if student_obj.login(username,password):
			print('登录成功！\n')
			while True:
				inp=input('1、选课；2、上课；3、查看课程信息；\n')
				if inp=='1':
					select_course(student_obj)
				elif inp=='2':
					pass
				elif inp=='3':
					course_info(student_obj)
				else:
					break
		else:
			print('用户名或者密码错误')
	else:
		print('Sorry，您登录的用户不存在！')



def register(username,password):
	'''学生注册'''
	student_obj=models.Student()
	student_obj.register(username,password)

def select_course(student_obj):
	'''学生选课'''
	#读取所有课程的信息
	course_list=pickle.load(open(settings.COURSE_DB_DIR,'rb'))
	for num,item in enumerate(course_list,1):
		print(num,'\t',item.course_name,'\t',item.cost,'\t',item.teacher.name,'\t',item.create_time,'\t',item.create_admin.username)
	while True:
		num=input('请选择课程(q表示退出):\n')
		if num=='q':
			break
		selected_course_obj=course_list[int(num)-1]
		#选择的课程添加到学生的选课数据中,增加判断，存在就不添加
		if selected_course_obj not in student_obj.course_list:
			student_obj.course_list.append(selected_course_obj)
	#学生选择的课程信息写入到学生的文件中
	pickle.dump(student_obj,open(os.path.join(settings.BASE_STUDENT_DIR,student_obj.username),'wb'))

def course_info(student_obj):
	'''查看课程信息'''
	for item in student_obj.course_list:
		print(item.course_name,item.teacher.name,item.cost)


def main():
	inp=input('1、登录；2、注册；\n')
	username=input('请输入用户名:\n')
	password=input('请输入密码:\n')
	if inp=='1':
		login(username,password)
	elif inp=='2':
		register(username,password)

if __name__=='__main__':
	main()
