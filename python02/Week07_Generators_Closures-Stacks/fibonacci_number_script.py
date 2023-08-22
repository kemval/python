def fibonacci(limit):
    fib1, fib2 = 1, 1
    yield fib1
    yield fib2
    
    while True:

        next = fib1 + fib2

        if next > limit:

            break

        yield next

        fib1, fib2 = fib2, next


while True:
    try:
        limit = int(input("Enter the limit for Fibonacci generation: "))

        if limit <= 0:

            print("Enter a positive number.")

            continue
        
        fibonacci_creation = fibonacci(limit)
        
        for num in fibonacci_creation:

            print(num, end=" ")
        
        break  
    except ValueError:

        print("Please enter a valid number.")