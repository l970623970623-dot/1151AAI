# 讀取正整數 n（不加任何輸入提示字元）
n = int(input())

# 使用巢狀 for 迴圈產生 n 列 n 欄的乘法表
for i in range(1, n + 1):
    for j in range(1, n + 1):
        # 每個數字以欄寬 4 靠右對齊，不加額外分隔字元
        print(f"{i * j:4d}", end="")
    # 每行結尾換行
    print()