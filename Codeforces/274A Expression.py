a=int(input())
b=int(input())
c=int(input())
A=[]
A.append(a+b*c)
A.append(a*(b+c))
A.append(a*b*c)
A.append((a+b)*c)
print(max(A))