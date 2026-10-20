# 讀取輸入的三個整數：目前存款 s、每天新增金額 d、目標金額 t
s, d, t = map(int, input().split())

# 初始化累積天數與目前金額
days = 0
current = s

# 使用 while 迴圈每日更新存款與天數，直到達標或超過目標
while current < t:
    current += d
    days += 1

# 輸出最少天數（不包含任何提示標籤）
print(days)