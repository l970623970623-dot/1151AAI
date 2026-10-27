import sys

def main():
    # 完整讀取一整行輸入（包含空行與頭尾空白）
    line = sys.stdin.readline()
    if not line:
        raw_input = ""
    else:
        # 僅去除換行符號 \n 或 \r\n，保留輸入原本頭尾的半形空白
        raw_input = line.rstrip('\r\n')

    # 1. 帳號整理 (Cleanup)
    # strip() 移除頭尾半形空白，lower() 轉小寫，split() 拆分連續空白，join('_') 以單一底線連接
    cleaned = '_'.join(raw_input.strip().lower().split())

    # 2. 合法性驗證 (Validation)
    # 長度需為 6 ~ 16 字元
    is_len_valid = 6 <= len(cleaned) <= 16
    
    # 字元僅限 a-z, 0-9, _ (完全不使用正則表達式與外部套件)
    valid_chars = set("abcdefghijklmnopqrstuvwxyz0123456789_")
    is_char_valid = all(char in valid_chars for char in cleaned)

    is_valid = is_len_valid and is_char_valid

    # 3. 依規格輸出結果
    # 第一行輸出整理後結果（若為空字串則印空白行）
    print(cleaned)
    # 第二行輸出 VALID 或 INVALID
    print("VALID" if is_valid else "INVALID")

if __name__ == "__main__":
    main()