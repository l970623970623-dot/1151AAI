
N, M = map(int, input().split())

A = set(input().split())
B = set(input().split())

result1 = sorted(A & B)
result2 = sorted(A | B)
result3 = sorted(A - B)
result4 = sorted(B - A)

for result in [result1, result2, result3, result4]:
    if result:
        print(" ".join(result))
    else:
        print("NONE")
