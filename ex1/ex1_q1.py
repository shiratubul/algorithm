
def fib_recursive(n):
    global count
    count += 1
    if n <= 1:
        return n
    return fib_recursive(n - 1) + fib_recursive(n - 2)

for num in [10, 20, 30, 50]:
    count = 0
    print(f"Fibonacci({num}): {fib_recursive(num)} ")
    print(f"depth:{count} ")
