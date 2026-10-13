# 讀取一行包含三個以空白分隔的整數
a, b, c = map(int, input().split())

# 使用 if-elif-else 條件判斷式找出最大值
if a >= b and a >= c:
    max_val = a
elif b >= c:
    max_val = b
else:
    max_val = c

# 輸出最大值（不包含任何提示文字或答案標籤）
print(max_val)