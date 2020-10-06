# Ion şi Vasile joacă următorul joc: 
# Ion spune un număr iar Vasile trebuie să găsească cinci  numere  consecutive,  crescătoare,  numărul  din  mijloc  fiind  cel  ales  de  Ion. 
# Exemplu: Ion spune 10, Vasile spune 8 9 10 11 12. Ajutaţi-l pe Vasile să găsească răspunsul mai repede.

n=int(input("introduceti numarul:"))
print(n-2,n-1,n,n+1,n+2, sep=";")