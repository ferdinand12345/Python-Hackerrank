if __name__ == '__main__':
	students = []

	for _ in range(int(input())):
		name = input()
		score = float(input())
		students.append((name, score))
	
	xxx = sorted(set(score for name, score in students))[1]

	for name, score in sorted(students):
		if score == xxx:
			print(name)