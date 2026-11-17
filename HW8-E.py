
N = int(input())

records = set()

for i in range(N):
    student, booth = input().split()
    records.add((student, booth))

counts = {}

for student, booth in records:
    counts[student] = counts.get(student, 0) + 1

ranking = list(counts.items())

ranking.sort(key=lambda x: (-x[1], x[0]))

print(len(records))

for student, count in ranking:
    print(student, count)
