def main():
    # 1. 讀取菜單筆數 M
    M = int(input())

    # 使用平行串列紀錄飲料名稱與原始單價
    drink_names = []
    drink_prices = []

    for _ in range(M):
        data = input().split()
        drink_names.append(data[0])
        drink_prices.append(int(data[1]))

    # 2. 讀取訂單筆數 N
    N = int(input())

    # 平行串列：紀錄每種飲料的全班總訂購杯數
    drink_total_qty = [0 for _ in range(M)]

    # 串列：依訂單首次出現順序紀錄學生姓名
    students = []
    # 二維串列：student_orders[i][j] 代表第 i 位學生購買第 j 種飲料的數量
    student_orders = []

    # 讀取每筆訂單並進行累計
    for _ in range(N):
        data = input().split()
        s_name = data[0]
        d_name = data[1]
        qty = int(data[2])

        # 使用 index() 尋找飲料在菜單中的索引位置
        d_idx = drink_names.index(d_name)
        drink_total_qty[d_idx] += qty

        # 若學生尚未記錄，新增至學生串列並初始化該學生的飲料購買數量串列
        if s_name not in students:
            students.append(s_name)
            student_orders.append([0 for _ in range(M)])

        s_idx = students.index(s_name)
        student_orders[s_idx][d_idx] += qty

    # 3. 計算每種飲料優惠後的實際單價（滿 10 杯每杯折 5 元）
    actual_prices = []
    for i in range(M):
        base_price = drink_prices[i]
        if drink_total_qty[i] >= 10:
            actual_prices.append(base_price - 5)
        else:
            actual_prices.append(base_price)

    # 4. 依菜單順序輸出每種飲料總杯數
    for i in range(M):
        print(f"DRINK {drink_names[i]} {drink_total_qty[i]}")

    # 5. 依學生首次出現順序計算並輸出每位學生應付金額
    total_amount = 0
    for s_idx in range(len(students)):
        s_name = students[s_idx]
        s_total = 0
        for d_idx in range(M):
            s_total += student_orders[s_idx][d_idx] * actual_prices[d_idx]
        print(f"STUDENT {s_name} {s_total}")
        total_amount += s_total

    # 6. 輸出全班總額
    print(f"TOTAL {total_amount}")

if __name__ == "__main__":
    main()