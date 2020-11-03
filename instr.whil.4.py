nr=eval(input("Dati un numar:"))
k=1
suma=0
produs=1

while (k<=nr):
    suma +=k
    produs*=k
    media_ar=suma/nr
    k+=1

print(" suma: ",suma)
print("produsul: ",produs)
print("media aritmetica: ",media_ar)
