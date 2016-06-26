def scoreCompare(a, b):
	if a[1] > b[1]:
		return -1
	if a[1] < b[1]:
		return 1
	if a[1] == b[1] and a[2] > b[2]:
		return -1
	return 1

def getScores(name, powers):
	nameScore = 0
	lexoScore = 0
	length = len(name)
	for i in range(7, -1, -1):
		if i < length:
			norm = ord(name[i]) - 96
			lexoScore += norm * powers[i]
			nameScore += norm
	return (nameScore, lexoScore)


def answer(names):
	powers = [10460353203, 387420489, 14348907, 531441, 19683, 729, 27, 1]

	scores = []
	for name in names:
		scores.append((name,) + getScores(name, powers))

	scores.sort(scoreCompare)

	return [score[0] for score in scores]


test_cases = []
test_cases.append(["annie", "bonnie", "liz"])
test_cases.append(["abcdefg", "vi"])
test_cases.append(["al", "cj"])

test = 0
for test_case in test_cases:
	print "Test " + str(test) + ": "
	print answer(test_case)
	test += 1