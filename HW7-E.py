import sys

# 依題目規範定義遞迴函數 (內含記憶化 Memoization，無任何迴圈/推導式)
def count_ways(step, n, blocked, memo):
    # 邊界條件：超出階梯範圍
    if step > n:
        return 0
    
    # 邊界條件：踏上損壞的階梯
    if blocked[step]:
        return 0
    
    # 成功到達第 N 階
    if step == n:
        return 1
    
    # 記憶化：若先前已計算過該階梯到終點的走法，直接傳回紀錄值
    if memo[step] != -1:
        return memo[step]
    
    # 遞迴呼叫：分別計算走 1 階與走 2 階，並紀錄至 memo
    memo[step] = count_ways(step + 1, n, blocked, memo) + count_ways(step + 2, n, blocked, memo)
    return memo[step]

def main():
    # 讀取第一行輸入：N 與 K
    line1 = sys.stdin.readline()
    if not line1.strip():
        return
    
    parts = line1.split()
    n = int(parts[0])  # 取出第一個數值 (N)
    k = int(parts[1])  # 取出第二個數值 (K)
    
    # 初始化 blocked 串列 (長度 n+1)
    blocked = [False] * (n + 1)
    
    # 若 K > 0，讀取第二行的損壞階梯編號
    if k > 0:
        line2 = sys.stdin.readline()
        damaged_list = line2.split()
        for i in range(k):
            damaged_stair = int(damaged_list[i])
            blocked[damaged_stair] = True
            
    # 初始化 memo 串列 (長度 n+1，預設皆為 -1)
    memo = [-1] * (n + 1)
    
    # 依題目規範從 step=0 開始呼叫 count_ways
    ans = count_ways(0, n, blocked, memo)
    
    # 輸出結果
    print(ans)

if __name__ == '__main__':
    main()