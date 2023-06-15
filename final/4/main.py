n = int(input())
grades = {}
for i in range(n):
    line = input().split()
    course = " ".join(line[:-1])
    grade = int(line[-1])
    grades[course] = grades.get(course, []) + [grade]

ans = sorted(grades.items(), key=lambda x: (-sum(x[1]) / len(x[1]), -len(x[1])))
for course, grade in ans:
    print(course)