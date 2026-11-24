#score=59.58854448852
#name="apple"
#age=68
#print(f"My name is {name} and I am {age} years old.",end=" ")
#print(f"{score:.4f}")

#name = 'peter'
#chinese = 85.6
#english = 92.3
#math = 78.9
#print(f'學生姓名：{name}')
#print(f'國文成績：{chinese:.1f}分')
#print(f'英文成績：{english:.1f}分')
#print(f'數學成績：{math:.1f}分')
#print(f'平均成績：{(chinese+english+math)/3:.2f}分')

#a = b = c = 10
#x, y, z = 1, 2.5, 'Hi'
#print(a,b,c,sep="+",end="     ")
#print(x,y,z,sep=",")

#name = input("What\'s your name?" )
#print(f"My name is {name}.")
#score = float(input("請輸入成績："))
#print(f"成績:{score:.2f}")


# 學生資料輸入範例
#print('=== 學生資料輸入系統 ===')
#name = input('姓名：')
#student_id = input('學號：')
#chinese = float(input('國文成績：'))
#english = float(input('英文成績：'))
#math = float(input('數學成績：'))

# 計算平均成績
#average = (chinese + english + math) / 3

# 格式化輸出結果
#print('=== 學生資料 ===')
#print(f'姓名：{name}')
#print(f'學號：{student_id}')
#print(f'國文：{chinese:.1f}分')
#print(f'英文：{english:.1f}分')
#print(f'數學：{math:.1f}分')
#print(f'平均：{average:.2f}分')

#numbers=input("請輸入三個數字").split()
#a=int(numbers[0])
#b=int(numbers[1])
#c=int(numbers[2])
#result = (a + b +c) /3
#print(a,b,c)
#print(f"平均值：{result:.2f}分")

#a,b,c=map(float, input("請輸入三個數字").split())
#result = (a + b +c) /3
#print(a,b,c)
#print(f"平均值：{result:.2f}分")

#score = float(input("請輸入成績:"))
#if score >= 100:
#    print(f"成績{score:.2f}分大於100分,輸入錯誤")
#elif score >= 60:
#    print(f"成績{score:.2f}分,及格")
#else:
#    print(f"成績{score:.2f}分,不及格")

#for i in range(1,10):
#    print(i,end="")


#total = 0
#for i in range(1, 101):
#    total = i+total
#print(total)

#for i in range(5):
#    for j in range(5):
#        print(i, j)

#for i in range(20):
#    if i % 2 == 0:
#        print(i,"是偶數")

#for i in range(1,21):
#    square=i**2
#    print(f"{i}的平方是{square}")


#count = 0
#while count < 6:
#  count += 1
#  print(count)

#count = 0
#while count < 6:
#    print(count)
#    count += 1

#for i in range(11):
#    if i == 7:
#        break
#      print(i)

#for i in range(11):
#    if i == 7:
#        continue
#    print(i)

#for i in range(1, 11):
#    for j in range(1, 11):
#        result = i*j
#        print(f"{i}*{j}={result}",end="\t")

#for i in range(1, 10):
#    for j in range(1, i + 1):
#        print(i,j) 

#print("2~100 的質數：")
#for num in range(2, 101):
#    is_prime = True
#    for i in range(2, int(num**0.5) + 1):
#        if num % i == 0:
#            break
#    if is_prime:
#       print(num, end=" ")



#k = int(input("請輸入一個正整數："))
#for i in range(1,k):
#    for j in range(1,i+1):
#        print("&",end="")
#    print()


for i in range(1, 6):
    for j in range(1, i + 1):
         print(i,j)
    
        
















