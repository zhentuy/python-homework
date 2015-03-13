#coding:utf-8
'''
我这个有笔试题你看下能做下不能
我有个矩阵

1，2，4，6
2，5，6，9
4，6，7，10
6，9，10，11

这个矩阵你看下x,y=y,x
你要写一个class:
1、包含验证我这个矩阵是否成功
2、我给你一个坐标，要可以成功改变这个矩阵对应的元素
3、初始化的时候由你自己初始化
4、我给你一个坐标，我要得到这一行元素
'''
import random

class SymMat(object):

	def __init__(self, length=4):
		self.length = length
		self.matrix = [[0]*length]*length
		values = range(length*2)
		for x, line in enumerate(self.matrix):
			v = random.sample(values, length-x)
			self.matrix[x] = self.matrix[x][:x] + v


		for x, line in enumerate(self.matrix):
			for y, v in enumerate(line):
				 self.matrix[y][x] = self.matrix[x][y]

	@staticmethod
	def valid(mat):
		try:
			for x, line in enumerate(mat):
				for y, v in enumerate(line):
					if mat[x][y] == mat[y][x]:
						pass
					else:
						return False
		except (IndexError, TypeError):
			return 'is not a valid matrix'
		return True
	
	def get_line(self, x, y):
		if x <= self.length and y <= self.length:
			return self.matrix[x]
		else:
			return "index out of range"
	
	def set_value(self, x, y, value):
		if x <= self.length and y <= self.length:
			self.matrix[x][y] = value
			self.matrix[y][x] = value
		else:
			return "index out of range"

def pprint(l):
	for i in l:
		print i

