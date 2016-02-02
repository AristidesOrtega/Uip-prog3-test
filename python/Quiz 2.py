n = 1
p = 0
i = 0
while n <= 5000:
    if n%2 == 0:
        p += n
    n += 1
print ("La suma de los pares es igual a {0} ".format(p))
