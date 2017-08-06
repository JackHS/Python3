from enum import Enum
Month = Enum('Month',('JAN','FEB'))
for name,menber in Month.__members__.items():
	print(name,'=>',menber,',',menber.value)