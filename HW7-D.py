# 1. 定義遞迴 gcd(a, b)，以 b == 0 為基底條件
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

# 2. 定義 simplify_recipe 函式，呼叫自訂 gcd 求三數最大公因數並回傳最簡比例
def simplify_recipe(tea, milk, syrup):
    # 先求前兩數的 gcd，再與第三數求 gcd
    g = gcd(gcd(tea, milk), syrup)
    return tea // g, milk // g, syrup // g

# 3. 主程式：處理多筆輸入並呼叫 simplify_recipe 輸出結果
def main():
    n = int(input())
    for _ in range(n):
        tea, milk, syrup = map(int, input().split())
        t_simplified, m_simplified, s_simplified = simplify_recipe(tea, milk, syrup)
        print(f"{t_simplified} {m_simplified} {s_simplified}")

if __name__ == '__main__':
    main()