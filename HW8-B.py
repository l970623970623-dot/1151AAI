
N = int(input())

runners = []

for i in range(N):
    name, time, penalty = input().split()
    time = int(time)
    penalty = int(penalty)

    runners.append((name, time, penalty))

runners.sort(key=lambda x: (x[1] + x[2], x[1], x[0]))

for runner in runners:
    name, time, penalty = runner
    print(name, time + penalty)
