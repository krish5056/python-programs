def calc():
    no1=int(input("1st no:"))
    no2=int(input("2nd no:"))
    add=no1+no2
    sub=no1-no2
    mul=no1*no2
    div=no1/no2
    return add,sub,mul,div
ans=calc()
print(ans)
print(type(ans))

