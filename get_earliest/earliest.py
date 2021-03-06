def my_get_earliest(date1, date2):
	date1List = date1.split('/')
	date2List = date2.split('/')


	def testValue(list1, list2, index):
		val1 = int(list1[index])
		val2 = int(list2[index])

		if val1 == val2:
			return

		return list1 if val1 < val2 else list2


	yearTest = testValue(date1List, date2List, 2)
	if yearTest:
		return date1 if yearTest == date1List else date2
	else:
		monthTest = testValue(date1List, date2List, 0)
		if(monthTest):
			return date1 if monthTest == date1List else date2
		else:
			dayTest = testValue(date1List, date2List, 1)
			if(dayTest):
				return date1 if dayTest == date1List else date2
			else:
				return 'Could not compute'


def solution_get_earliest(date1, date2):
  """Return earliest of two MM/DD/YYYY-formatted date strings."""
  (m1, d1, y1) = date1.split('/')
  (m2, d2, y2) = date2.split('/')
  return date1 if (y1, m1, d1) < (y2, m2, d2) else date2




