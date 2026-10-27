# 讀取輸入：四個整數 B (原餐費), N (人數), R (服務費百分比), C (折價券金額)
B, N, R, C = map(int, input().split())

# 1. 計算服務費：原餐費乘以服務費百分比，不足 1 元捨去（使用整數除法 //）
service_fee = (B * R) // 100

# 2. 計算應付總額：原餐費 + 服務費 - 折價券金額（若小於 0 則改為 0）
total = B + service_fee - C
if total < 0:
    total = 0

# 3. 計算公平分攤金額與人數
q = total // N       # 每人基礎應付金額（商）
b = total % N        # 需要多付 1 元的人數（餘數）
a = N - b            # 付基礎金額 q 元的人數

# 4. 輸出結果
print(total)         # 第一行：應付總額 T
print(f"{q} {a}")    # 第二行：q a（a 人各付 q 元）
print(f"{q + 1} {b}")# 第三行：q+1 b（b 人各付 q+1 元）