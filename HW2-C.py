# 1. 讀取同一列輸入的分鐘數 m 與秒數 s
m, s = map(int, input().split())

# 2. 依據公式計算總秒數 (60 * m + s)
total_seconds = 60 * m + s

# 3. 印出總秒數結果
print(total_seconds)