
def fib_memo(n, memo=None):
    global count
    count += 1

    if memo is None:
        memo = {}
    
    
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    
    res1 = fib_memo(n - 1, memo)
    res2 = fib_memo(n - 2, memo)
    
    memo[n] = res1 + res2
    return memo[n]

count = 0
print(f"Fibonacci 30: {fib_memo(30)}, depth: {count}")