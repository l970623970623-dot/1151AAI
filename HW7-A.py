def parking_fee(minutes):
    """
    根據停車分鐘數計算單次停車費用
    """
    if minutes == 0:
        return 0
    
    # 計算 30 分鐘區間數（不足 30 分鐘自動進位算 1 個區間）
    intervals = (minutes + 29) // 30
    fee = intervals * 30
    
    # 單次停車費上限為 200 元
    return min(200, fee)

def main():
    # 讀取記錄數 N
    n = int(input())
    
    # 讀取 N 個車輛的停車分鐘數
    minutes_list = list(map(int, input().split()))
    
    # 依序呼叫 parking_fee 計算每輛車費用
    fees = [parking_fee(m) for m in minutes_list]
    
    # 第一行輸出各車費用（以空白分隔）
    print(" ".join(map(str, fees)))
    
    # 第二行輸出總收入（費用總和）
    print(sum(fees))

if __name__ == "__main__":
    main()