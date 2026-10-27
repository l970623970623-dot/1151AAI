def solve():
    # 讀取商品種類數 N (自動去餘空白)
    n = int(input().strip())
    
    # 使用平行串列儲存商品名稱與小計
    names = []
    subtotals = []
    
    # 精確讀取 N 行商品資料，讀完立刻結束輸入
    for _ in range(n):
        line = input().split()
        name = line[0]         # 商品名稱字串 (如 "Milk")
        price = int(line[1])    # 單價
        quantity = int(line[2]) # 數量
        
        # 每滿 3 件扣除 1 件免費
        paid_quantity = quantity - (quantity // 3)
        subtotal = paid_quantity * price
        
        names.append(name)
        subtotals.append(subtotal)
    
    # 計算總和與滿額折扣 (滿 1000 折 100)
    total_sum = sum(subtotals)
    final_total = total_sum - 100 if total_sum >= 1000 else total_sum
    
    # 找出最高小計商品 (同金額時選較早輸入者)
    max_subtotal = -1
    top_name = ""
    for i in range(n):
        if subtotals[i] > max_subtotal:
            max_subtotal = subtotals[i]
            top_name = names[i]
            
    # 依序輸出各商品小計 (格式：Milk 300)
    for i in range(n):
        print(f"{names[i]} {subtotals[i]}")
        
    # 輸出 TOTAL 與 TOP
    print(f"TOTAL {final_total}")
    print(f"TOP {top_name}")

if __name__ == "__main__":
    solve()