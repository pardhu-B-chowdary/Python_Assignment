n = int(input("Enter a Number:"))
c = 0
for i in range(1,n+1):
    if n%i == 0:
        c = c+1
if c == 2:
    print(n," is a Prime Number")
else:
    print(n," is not a Prime Number" )
input()