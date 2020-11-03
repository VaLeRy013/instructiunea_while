n = 0
s = 0
while ((n % 2 == 0) or (n % 3 != 0)):
    n = eval(input("dati un numar: "))
    if n % 2 == 0:
        s += n

print("suma:", s)
