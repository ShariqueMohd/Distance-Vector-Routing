import sys

class Data(object):

	def __init__(self):
		self.N = 0
		self.G = []
		pass

	def setup(self):
		sys.stdin = open('InputFile.txt')

	def getInput(self):
		self.N = input()
		for i in range(self.N):
			A = raw_input().split()
			node = []
			for i in range(int(A[0])):
				node.append((int(A[2*i+1])-1, int(A[2*i+2])))
			self.G.append(node)