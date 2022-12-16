#Write a Python program to check if a number is pallindrome or not
n = int(input("Enter a number:"))
t = n
d = 0
while n > 0 :
    r = n%10
    d = d*10+r
    n = n//10
if(d == t):
    print(d," is a Pallindrome")
else:
    print(d," is not a Pallindrome")
input()