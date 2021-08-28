def main():
    # escribe tu código abajo de esta línea
    Saldo_del_mes_anterior = float(input("Dame el saldo del mes anterior: "))
    Ingresos = float(input("Dame los ingresos: "))
    Egresos = float(input("Dame los egresos: "))
    Número_de_cheques_expedidos = int(input("Dame el número de cheques: "))
    
    p2 = Ingresos-Egresos-(Número_de_cheques_expedidos*13)
    p1 = Saldo_del_mes_anterior + p2
    saldo_final = p1-(p1*0.075) 

    print("El saldo final de la cuenta es:", saldo_final)

if __name__ == '__main__':
    main()
    