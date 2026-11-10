def is_prime(n):
    """
    使用試除法判定 n 是否為質數
    檢查範圍至除數平方不大於 n (d * d <= n)
    """
    if n < 2:
        return False
    
    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d += 1
    return True

def main():
    # 讀入區間範圍 L 與 R
    L, R = map(int, input().split())
    
    primes = []
    # 對區間內的每個整數呼叫 is_prime
    for num in range(L, R + 1):
        if is_prime(num):
            primes.append(num)
    
    # 依規定格式輸出結果
    if primes:
        print(*primes)
        print(f"{len(primes)} {sum(primes)}")
    else:
        print("NONE")
        print("0 0")

if __name__ == "__main__":
    main()