n = int(input("Enter number of numbers in list: "))
li = [i for i in range(n)]
for i in range(n):
    li[i] = int(input(f"Enter {i+1} number: "))
#another easy  way input numbers to list with out 'n' or 'for' loop is by using map:
#li = list(map(int,input("Enter Numbers:").split()))
#To get max number number in List easily --------->  print(f"Max number in the given List is : {max(li)}")
m = 0
for i in range(n):
    if li[i]>m:
        m = li[i]
print(f"Max number in the given List is : {m}")
input()
