class Student(object):
	__slots__=('name','age')
	pass
s=Student()
s.name = 'hu'
def set_age(self,age):
	self.age = age
Student.set_age =set_age
s.set_age(25)
print(s.age)
class stu(Student):
	__slots__ = ('hu')
st =stu()
st.hu ='hu'