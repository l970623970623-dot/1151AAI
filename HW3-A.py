# 讀取輸入的三位正整數 N
N = int(input())

# 使用整數除法與取餘數拆解位數
hundreds = N // 100         # 百位數
tens = (N // 10) % 10       # 十位數
ones = N % 10               # 個位數

# 計算各位數總和與乘積
digit_sum = hundreds + tens + ones
digit_product = hundreds * tens * ones

# 計算反轉後的整數（不保留前導零）
reversed_num = ones * 100 + tens * 10 + hundreds

# 依題目要求的 4 行格式輸出
print(hundreds, tens, ones)
print(digit_sum)
print(digit_product)
print(reversed_num)