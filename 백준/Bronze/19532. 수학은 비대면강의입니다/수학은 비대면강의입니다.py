a,b,c,d,e,f = map(int, input().split())
n = a*e-b*d
print((c*e-f*b)//n, (f*a-c*d)//n)