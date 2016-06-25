def answer(intervals):
	starts = []
	ends = []
	for i in intervals:
		starts.append(i[0])
		ends.append(i[1])

	starts.sort()	# Solution times out--Error(408)--on submit, but not verify.
	ends.sort()		# I think these lines may be the culprit.

	count = ends[0] - starts[0]
	for i in range(1, len(starts)):
		count += min(ends[i] - ends[i - 1], ends[i] - starts[i])

	return count


test_cases = []
test_cases.append([[1, 3], [3, 6]])
test_cases.append([[10, 14], [4, 18], [19, 20], [19, 20], [13, 20]])
test_cases.append([[10, 1400], [4, 1800], [19, 2000], [1900, 2000], [130, 1073741823]])

test = 0
for test_case in test_cases:
	print "Test " + str(test) + ": " + str(answer(test_case))
	test += 1