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


class Admin:
	'''封装的管理员的信息'''
	def __init__(self):
		'''默认初始化管理员用户名和密码'''
		self.username=None
		self.password=None

	def login(self,username,password):
		'''
		管理员登录
		:param username:管理员用户名
		:param password: 管理员密码
		:return:
		'''
		if self.username==username and self.password==password:
			return True
		else:
			return False


	def register(self,user,passwd):
		'''
		管理员的注册
		:param user:注册的管理员用户名
		:param passwd:注册的管理员密码
		:return:
		'''
		self.username=user
		self.password=passwd
		#注册的账号信息序列化到一个文件
		path=self.username
		pickle.dump(self,open(path,'xb'))


class Teacher:
	'''封装老师的相关信息'''
	def __init__(self,name,age,admin):
		'''
		:param name: 老师名字
		:param age: 老师年龄
		:param admin: 那个管理员创建的老师
		'''
		self.name=name
		self.age=age
		#老师在程序中的资产
		self.__assets=0
		#老师创建时间
		self.create_time=time.strftime('%Y-%m-%d %H:%M:%S')
		self.create_admin=admin

	def gain(self,cost):
		'''
		老师增加的资产
		:param cost: 增加的数量
		:return:
		'''
		self.__assets+=cost


	def decrease(self,cost):
		'''
		老师减少资产
		:param cost:减少的数量
		:return:
		'''
		self.__assets-=cost

class Course:
	'''
	课程相关的信息
	'''
	def __init__(self,course_name,cost,teacher_obj,admin_obj):
		'''
		:param course_nname: 课程名称
		:param cost:课时费
		:param teacher_obj: 课程对应的老师对象(课程由老师带)
		:param admin_obj:课程对应的管理员(课程由管理员创建)
		'''
		self.course_name=course_name
		self.cost=cost
		self.teacher=teacher_obj
		self.create_time=time.strftime('%Y-%m-%d %H:%M:%S')
		self.create_admin=admin_obj

	def have_lesson(self):
		'''
		课程上课，自动给相关联的任课老师增加课时费
		:return:课程内容返回给上课者
		'''

class Student:
	pass


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
		teacher_obj=Teacher(teacher_name,teacher_age,admin_obj)
		teacher_list.append(teacher_obj)
		#判断老师是否存在,如果存在,就更新信息，如果不存在，就创建
		if os.path.exists('teacher_list'):
			exists_teacher_list=pickle.load(open('teacher_list','rb'))
			#批量更新数据(批量添加数据)
			teacher_list.extend(exists_teacher_list)
		pickle.dump(teacher_list,open('teacher_list','wb'))

def create_course(admin_obj):
	'''
	管理员创建课程
	:param admin_obj:创建课程的对象是管理员（课程是管理员创建的）
	:return:
	'''
	#管理员创建课程前，先把老师全部列出来
	teacher_list=pickle.load(open('teacher_list','rb'))
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
		course_obj=Course(course_name,course_cost,teacher_list[num-1],admin_obj)
		course_list.append(course_obj)
		#判断课程是否存在，如果存在，就更新，如果不存在，就创建
		if os.path.exists('course_list'):
			exists_course_list=pickle.load(open('course_list','rb'))
			course_list.extend(exists_course_list)
		pickle.dump(course_list,open('course_list','wb'))



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
	admin_obj = Admin()
	admin_obj.register(username, password)


def main():
	inp=int(input('1、管理员登录；2、管理员注册；\n'))
	username = input('请输入管理员用户名:\n')
	password = input('请输入管理员密码:\n')
	if inp==1:
		login(username,password)
	elif inp==2:
		register(username,password)
	else:
		sys.exit(1)


if __name__=='__main__':
	main()