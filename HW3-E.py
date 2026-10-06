# 1. 讀取輸入：共 4 行，每行包含兩個以空白分隔的整數 [1]
# 矩陣 A 的第一列與第二列
a, b = map(int, input().split())
c, d = map(int, input().split())

# 矩陣 B 的第一列與第二列
e, f = map(int, input().split())
g, h = map(int, input().split())

# 2. 依照矩陣乘法公式計算 C = AB [1]
# 第一列計算：a*e + b*g 與 a*f + b*h [1]
r1_c1 = a * e + b * g
r1_c2 = a * f + b * h

# 第二列計算：c*e + d*g 與 c*f + d*h [1]
r2_c1 = c * e + d * g
r2_c2 = c * f + d * h

# 3. 輸出結果：共 2 行，每行以空白分隔 [1]
print(f"{r1_c1} {r1_c2}")
print(f"{r2_c1} {r2_c2}")