#!/usr/bin/env python 
#-*- coding:utf-8 -*-

import  time
import  pickle
import  os
from config import  settings

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
		path=os.path.join(settings.BASE_ADMIN_DIR, self.username)
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
	'''学生相关信息'''
	def __init__(self):
		self.username=None
		self.password=None

		self.course_list=[]
		self.study_dict={}

	def select_course(self,course_obj):
		pass

	def login(self,username,password):
		'''
		学生登录
		:param username:学生账户
		:param password:学生账户密码
		:return:
		'''
		if self.username==username and self.password==password:
			return True
		else:
			return False

	def register(self,username,password):
		'''
		学生注册
		:param username:注册的学生姓名
		:param password:注册的学生姓名的密码
		:return:
		'''
		self.username=username
		self.password=password

		path=os.path.join(settings.BASE_STUDENT_DIR,self.username)
		pickle.dump(self,open(path,'xb'))