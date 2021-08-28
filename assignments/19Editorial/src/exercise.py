def main():
    # escribe tu código abajo de esta línea
    palabras = int(input("Dame el número de palabras: "))
    pag = palabras / 450
    unapag = 60
    dospag = 120
    if pag <= 1:
        pagina = unapag - (unapag * .1)
        print("El costo de la publicación es:", pagina)
    else:
        paginas = dospag - (dospag * .1)
        print("El costo de la publicación es:", paginas)
  

if __name__ == '__main__':
    main()
    