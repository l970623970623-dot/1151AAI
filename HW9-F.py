
A, B = map(int, input().split())

if A > B:
    A, B = B, A

for num in range(max(2, A), B + 1):
    is_prime = True

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print(num, end=" ")
