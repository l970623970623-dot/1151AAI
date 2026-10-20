# 1. 讀取學生人數 n
n = int(input())

# 2. 讀取以空白分隔的整數成績，並轉為串列
scores = list(map(int, input().split()))

# 3. 初始化累加變數與及格人數
total_score = 0
pass_count = 0

# 4. 使用 for 迴圈逐筆處理（不使用 sum()）
for score in scores:
    total_score += score
    if score >= 60:
        pass_count += 1

# 5. 計算平均分數
average_score = total_score / n

# 6. 依格式輸出：第 1 行平均值保留兩位小數，第 2 行及格人數
print(f"{average_score:.2f}")
print(pass_count)