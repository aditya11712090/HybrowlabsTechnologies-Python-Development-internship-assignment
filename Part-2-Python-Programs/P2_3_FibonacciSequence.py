def fibonacci(n):
    if n < 1:
        return "Invalid input. Please enter a positive integer greater than or equal to 1."
    elif n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

n = int(input("How many Fibonacci numbers would you like to print? "))

for i in range(1, n+1):
    print(fibonacci(i))
