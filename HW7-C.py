def normalize(text):
    """
    整理字串：只保留 ASCII 英文字母與數字，並將英文字母轉為小寫。
    """
    cleaned = []
    for char in text:
        # 判斷是否為 ASCII 英文字母或數字
        if ('a' <= char <= 'z') or ('A' <= char <= 'Z') or ('0' <= char <= '9'):
            cleaned.append(char.lower())
    return "".join(cleaned)


def is_palindrome(text, left, right):
    """
    遞迴判定是否為回文。
    以包含兩端的索引範圍 [left, right] 進行比較。
    不使用迴圈、推導式、切片或 reversed()。
    """
    # 基本情況：範圍交叉或重疊（字串長度為 0 或 1），判定為回文
    if left >= right:
        return True
    
    # 兩端字元不相等，非回文
    if text[left] != text[right]:
        return False
    
    # 直接呼叫自身，比較下一組兩端字元
    return is_palindrome(text, left + 1, right - 1)


# 主程式：讀取輸入並執行判斷
if __name__ == "__main__":
    raw_text = input()
    normalized_text = normalize(raw_text)
    
    # 傳入 0 與 len - 1 作為邊界索引
    if is_palindrome(normalized_text, 0, len(normalized_text) - 1):
        print("YES")
    else:
        print("NO")