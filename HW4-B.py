# 讀取輸入年份 y (1 <= y <= 9999)
y = int(input())

# 依序根據西曆規則判斷閏年或平年
if y % 400 == 0:
    print("Leap")
elif y % 100 == 0:
    print("Common")
elif y % 4 == 0:
    print("Leap")
else:
    print("Common")