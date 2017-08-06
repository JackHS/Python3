def log(func):
	def wapper(*args,**kw):
		print('call %s():'%func.__name__)
		return func(*args,**kw)
	return wapper
@log
def abs():
	pass
@log
def now():
	print('2017')
abs()
now()