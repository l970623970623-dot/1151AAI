def main():
  # 讀取一行包含三個以空白分隔的正整數
  a, b, c = map(int, input().split())

  # 判斷是否能組成三角形：任意兩邊長度之和嚴格大於第三邊
  if (a + b > c) and (a + c > b) and (b + c > a):
    # 依邊長條件進行分類
    if a == b == c:
      print('Equilateral')
    elif a == b or b == c or a == c:
      print('Isosceles')
    else:
      print('Scalene')
  else:
    print('Invalid')


if __name__ == '__main__':
  main()