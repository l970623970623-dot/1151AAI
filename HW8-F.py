
N = int(input())

records = []

for i in range(N):
    user, item = input().split()
    records.append((user, item))

target, K = input().split()
K = int(K)

users = {}

for user, item in records:
    if user not in users:
        users[user] = set()
    users[user].add(item)

target_items = users[target]

similar_users = []

for user in users:
    if user != target and users[user] & target_items:
        similar_users.append(user)

scores = {}

for user in similar_users:
    for item in users[user] - target_items:
        scores[item] = scores.get(item, 0) + 1

ranking = sorted(scores.items(), key=lambda x: (-x[1], x[0]))

R = min(K, len(ranking))

if R == 0:
    print(0)
else:
    print(R)
    for item, score in ranking[:R]:
        print(item, score)
