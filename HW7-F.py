import sys

def best_total(prices, index, remaining):
    """
    計算從索引 index 起的商品、在剩餘預算 remaining 時能達到的最大購物總額。
    簽名嚴格符合題目要求：best_total(prices, index, remaining)
    """
    # 邊界條件：商品索引超出範圍或剩餘預算歸零
    if index >= len(prices) or remaining <= 0:
        return 0
    
    # 剪枝優化：若當前商品超出剩餘預算，直接跳過不買
    if prices[index] > remaining:
        return best_total(prices, index + 1, remaining)
    
    # 決策分支 1：不選擇目前商品
    option1 = best_total(prices, index + 1, remaining)
    
    # 決策分支 2：選擇目前商品
    option2 = prices[index] + best_total(prices, index + 1, remaining - prices[index])
    
    # 回傳最大可行金額
    return max(option1, option2)

def main():
    # 讀取第一行：N 與 B (輸入如 "4 100")
    first_line = input().split()
    if not first_line:
        return
    N = int(first_line[0])  # 第一個數字：商品數量 N
    B = int(first_line[1])  # 第二個數字：預算 B
    
    # 讀取第二行：N 個商品價格 (輸入如 "60 45 40 30")
    second_line = input().split()
    prices = [int(p) for p in second_line[:N]]
    
    # 主程式從索引 0 與預算 B 開始進行遞迴
    result = best_total(prices, 0, B)
    print(result)

if __name__ == '__main__':
    main()