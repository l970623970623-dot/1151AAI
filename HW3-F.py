def solve():
    try:
        # 讀取第一列 (例如: 1 2)
        row1 = input().split()
        # 讀取第二列 (例如: 3 4)
        row2 = input().split()
        
        a, b = float(row1[0]), float(row1[1])
        c, d = float(row2[0]), float(row2[1])

        det = a * d - b * c

        inv_a = d / det
        inv_b = -b / det
        inv_c = -c / det
        inv_d = a / det

        print(f"{inv_a:.4f} {inv_b:.4f}")
        print(f"{inv_c:.4f} {inv_d:.4f}")
    except (EOFError, IndexError, ValueError):
        pass

if __name__ == "__main__":
    solve()