# 1. 讀取輸入資料
target = int(input())  # 第一行：每日目標步數 G
steps = [int(x) for x in input().split()]  # 第二行：七天步數存入串列

# 2. 計算總步數
total_steps = sum(steps)

# 3. 計算達標天數（步數 >= 目標步數）
reached_days = 0
for step in steps:
    if step >= target:
        reached_days += 1

# 4. 找出最高步數發生的所有日期（第 1 天至第 7 天）
max_step = max(steps)
max_days = []
for i in range(len(steps)):
    if steps[i] == max_step:
        max_days.append(str(i + 1))  # 日期從 1 開始計算

# 5. 計算最長連續達標天數
max_streak = 0
current_streak = 0
for step in steps:
    if step >= target:
        current_streak += 1
        if current_streak > max_streak:
            max_streak = current_streak
    else:
        current_streak = 0  # 沒達標則中斷連續計數

# 6. 依格式輸出四行結果
print(total_steps)  # 第一行：總步數
print(reached_days)  # 第二行：達標天數
print(" ".join(max_days))  # 第三行：最高步數出現的所有日期（以空白分隔）
print(max_streak)  # 第四行：最長連續達標天數