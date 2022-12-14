#Write a python program to read a number from user and write hello that many times using "for" and "while" Loop
n = int(input("Enter number"))
print("This is 'for' Loop")
for i in range(n):print("Hello; ",end='')
print()
j = 0
print("This is 'while' Loop")
while j < n:
    print("Hello; ",end='')
    j=j+1