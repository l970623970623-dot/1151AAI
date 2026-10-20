# 讀取輸入的一行資料並以空白拆分（不使用輸入提示字串）
data = list(map(int, input().split()))
a = data[0]
b = data[1]

# 使用 while 迴圈執行輾轉相除法
while b != 0:
    r = a % b
    a = b
    b = r

# 輸出最大公因數（不包含答案標籤）
print(a)