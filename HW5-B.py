# 讀取輸入單行，將以空白分隔的三個正整數分別賦值給 a, b, k
a, b, k = map(int, input().split())

count = 0      # 紀錄 k 的倍數個數
total_sum = 0  # 紀錄 k 的倍數總和

# 使用 for 迴圈遍歷區間 [a, b]（包含兩端，故 range 終點設為 b + 1）
for i in range(a, b + 1):
    # 搭配整除判斷（餘數為 0 表示為 k 的倍數）
    if i % k == 0:
        count += 1
        total_sum += i

# 依序輸出倍數個數與總和，兩者以空白分隔
print(f"{count} {total_sum}")