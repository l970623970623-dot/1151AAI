# 讀取非負整數 n
n = int(input())

# 初始化階乘結果為 1（滿足定義 0! = 1）
result = 1

# 使用 for 迴圈進行累乘
for i in range(1, n + 1):
    result *= i

# 輸出階乘結果
print(result)