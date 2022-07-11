import time
def daysInMonth(year, month):
	if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
		return 31
	else:
		if month == 4 or month == 6 or month == 9 or month == 11:
			return 30
		else:
			if month == 2:
				if year % 400 == 0:
					return 29
				else:
					if year % 100 == 0:
						return 28
					else:
						if year % 4 == 0:
							return 29
						else:
							return 28
			else:
				return 0

def isValidDate(year, month, day):
	if year < 1000 or year > 3000:
		return False
	else:
		if day < 0 or day > 31:
			return False
		else:
			if month >= 1 and month <= 12:
				if day >= 1:
					if day <= daysInMonth(year, month):
						return True
					else:
						return False
				else:
					return False
			else:
				return False
