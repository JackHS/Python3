class Student(object):
	"""docstring for Student"""
	def __init__(self, name,sex):
		self.name =name
		self.sex =sex
	def printSex(self):
		print ('%s:%s'%(self.name,self.sex))
		
hu =Student('hushiwei','man')
hu.printSex()
