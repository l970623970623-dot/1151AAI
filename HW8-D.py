
N = int(input())

stock = {}

for i in range(N):
    item, qty = input().split()
    stock[item] = int(qty)

Q = int(input())

total_sold = 0
rejected = 0

for i in range(Q):
    action, item, qty = input().split()
    qty = int(qty)

    if action == "ADD":
        stock[item] = stock.get(item, 0) + qty

    elif action == "BUY":
        if item in stock and stock[item] >= qty:
            stock[item] -= qty
            total_sold += qty
        else:
            rejected += 1

print(total_sold, rejected)

for item in sorted(stock):
    print(item, stock[item])
