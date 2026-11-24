
n = int(input())

count = 1

while True:
    total = sum(int(i) for i in str(n))

    print(f"Pass {count} : {total}")

    if total <= 9:
        break

    n = total
    count += 1

print(f"Digital Root of {n} : {total}")
