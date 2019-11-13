#letra DNI
dni = int(input("Introduzca tu DNI: "))

resto = dni%23
#print(resto)
letras= {'T': 1,
         'R': 2,
         'W': 3,
         'A': 4,
         'G': 5,
         'M': 6,
         'Y': 7,
         'F': 8,
         'D': 9,
         'X': 10,
         'B': 11,
         'N': 12,
         'J': 13,
         'Z': 14,
         'S': 15,
         'Q': 16,
         'V': 17,
         'H': 18,
         'L': 19,
         'C': 20,
         'K': 21,
         'E': 22}
for k,v in letras.items():
    #print(v)
    if(resto == v):
        print("Tu letra es ",k)


