# take input n from user and print factorial of n
# example: factorial of 5 = 1 * 2 * 3 * 4 * 5 = 120

n = int(input("enter n : "))
mul = 1
i = 1
while i <= n:
    mul *= i
    i += 1

print("factorial of n:", mul)


