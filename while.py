fib1 = 0
fib2 = 1


n = 12
i = 5
while i < n:
    fib_sum = fib1 + fib2
    print(fib_sum)
    fib1 = fib2
    fib2 = fib_sum
    i += 1



