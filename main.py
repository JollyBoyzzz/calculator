print("Enter A and B, and operation",
      "1. +",
      "2. -",
      "3. *",
      "4. /")
a = int(input())
b = int(input())
c = int(input())

if c == 1:
    print(a+b)
elif c == 2:
    print(a-b)
elif c == 3:
    print(a*b)
elif c == 4:
    print(a/b)
