# Se  introduc  de  la  tastatură  trei  cifre.  Afişaţi  pe  aceeaşi  linie  5  numere  formate  cu aceste cifre luate o singură dată. 
# Exemplu: date de intrare: 3 4 2  Date de ieşire: 324  342   243  234  432.

a=int(input("introduceti prima cifra:"))
b=int(input("introduceti a doua cifra:"))
c=int(input("introduceti a treia cifra:"))
print(a,b,c,";",c,b,a,";",a,c,b,";",b,a,c,";",c,a,b ,sep="")