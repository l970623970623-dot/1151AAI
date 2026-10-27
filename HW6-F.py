def main():
    # 讀取向後移動的位置數 K
    k = int(input())
    
    # 讀取原始訊息 S（input() 會讀取整行並自動保留開頭、結尾與連續空白）
    s = input()
    
    result = []
    for char in s:
        # 大寫英文字母處理
        if 'A' <= char <= 'Z':
            encrypted_char = chr((ord(char) - ord('A') + k) % 26 + ord('A'))
            result.append(encrypted_char)
        # 小寫英文字母處理
        elif 'a' <= char <= 'z':
            encrypted_char = chr((ord(char) - ord('a') + k) % 26 + ord('a'))
            result.append(encrypted_char)
        # 數字、空白與標點符號保持原樣
        else:
            result.append(char)
            
    # 輸出一行加密後的完整訊息
    print("".join(result))

if __name__ == "__main__":
    main()