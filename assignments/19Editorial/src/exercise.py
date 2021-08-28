from math import ceil

def main():
    # escribe tu código abajo de esta línea
    palabras = int(input("Dame el número de palabras: "))
    pag = ceil(palabras / 450)
    total = (pag * 60) * 0.9
    print("El costo de la publicación es: ", total)
  

if __name__ == '__main__':
    main()
