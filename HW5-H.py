# 讀取非負整數 n（不加上任何提示字串）
n = int(input())

total = 0

# 使用 while 迴圈取出個位數並累加，直到 n 為 0
while n > 0:
    total += n % 10  # 取得目前的個位數
    n = n // 10      # 去掉個位數

# 輸出各位數總和
print(total)