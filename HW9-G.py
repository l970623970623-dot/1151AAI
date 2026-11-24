
shift = list(map(int, input().split()))
text = input()

result = ""
index = 0

for ch in text:
    if 'A' <= ch <= 'Z':
        new_ch = chr((ord(ch) - ord('A') - shift[index % len(shift)]) % 26 + ord('A'))
        result += new_ch
        index += 1

    elif 'a' <= ch <= 'z':
        new_ch = chr((ord(ch) - ord('a') - shift[index % len(shift)]) % 26 + ord('a'))
        result += new_ch
        index += 1

    else:
        result += ch

print(result)
