# https://projecteuler.net/problem=2

# Fibonacci using a hash table dynamically (DP)
def fib(n, ht) :
    if n in ht :
        return ht[n]
    else :
        ht[n] = ht[n-1] + ht[n-2]
        del ht[n-2]
        return ht[n]

# Initialize the hash table and initial values
ht = {}
ht[1] = 1
ht[2] = 2
result = 2
# Look for the sum of even Fib values (up to 4M).
for i in range(3, 100) :
    fib_i = fib(i, ht)
    if fib_i > 4000000 :
        break
    if fib_i % 2 == 0 :
        result += fib_i
print(result)

# 4613732
