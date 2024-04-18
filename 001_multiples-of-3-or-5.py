# https://projecteuler.net/problem=1
sol=0
i = 0
while (i<1000) :
    if i%3 == 0 or i%5 == 0 :
        sol += i
    i += 1
print(sol)
# 233168
