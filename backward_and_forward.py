def answer(n):
	base = 2
	while True:
		value = convertBase(n, base)
		if isPalindrome(value):
			return base

		base += 1

def convertBase(n, b):
	based = []
	while n > 0:
		based.append(n % b)
		n /= b
	return based

def isPalindrome(value):
	last = len(value) / 2
	for i in range(0, last):
		if value[i] != value[len(value) - i - 1]:
			return False
	return True


print(answer(1000))