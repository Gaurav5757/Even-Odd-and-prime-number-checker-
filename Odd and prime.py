n = int(input("Enter a number: "))

# Even or Odd
if n % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")

# Prime Number
if n <= 1:
    print("Not a Prime Number")
else:
    for i in range(2, n):
        if n % i == 0:
            print("Not a Prime Number")
            break
    else:
        print("Prime Number")