def main():
    # 讀取單行輸入的總秒數 S
    S = int(input().strip())
    
    # 計算小時數（總秒數整除 3600）
    hours = S // 3600
    
    # 計算剩餘秒數換算成的分鐘數
    minutes = (S % 3600) // 60
    
    # 計算最後剩餘的秒數
    seconds = S % 60
    
    # 依序輸出小時數、分鐘數、秒數，以一個空白分隔
    print(f"{hours} {minutes} {seconds}")

if __name__ == "__main__":
    main()