def main():
    # 讀取 N
    N = int(input().strip())
    
    # 讀取初始清單 (N=0 時消耗空白行)
    if N > 0:
        playlist = input().strip().split()
    else:
        input()
        playlist = []
        
    # 讀取 Q
    Q = int(input().strip())
    
    # 執行 Q 個指令
    for _ in range(Q):
        line = input().strip().split()
        if not line:
            continue
        
        op = line  # 第一個字串為指令名稱
        
        if op == "ADD":
            name = line[1]  # 第二個字串為歌曲名稱
            playlist.append(name)
        elif op == "REMOVE":
            name = line[1]  # 第二個字串為歌曲名稱
            if name in playlist:
                playlist.remove(name)
        elif op == "REVERSE":
            playlist.reverse()
            
    # 輸出結果
    print(len(playlist))
    if len(playlist) == 0:
        print("EMPTY")
    else:
        print(" ".join(playlist))

if __name__ == "__main__":
    main()