X1,X2,X3 = map(int, input().split())
m=(X1+X2+X3)/3
v= ((X1-m)**2+(X2-m)**2+(X3-m)**2)/3
print(f"{m:.2f} {v:.2f}")