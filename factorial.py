n=int(input("Enter a number: "))
p=1
for i in range(1,n+1):
    p*=i
print(f"Factorial of {n} is {p}")  