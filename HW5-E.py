# 讀取輸入的整數 n
n = int(input())

# 處理邊界條件 F(0) = 0 與 F(1) = 1
if n == 0:
    print(0)
elif n == 1:
    print(1)
else:
    # 設置 F(0) 與 F(1) 的初始數值
    a, b = 0, 1
    # 使用 for 迴圈從第 2 項逐步更新數值至第 n 項
    for _ in range(2, n + 1):
        a, b = b, a + b
    print(b)