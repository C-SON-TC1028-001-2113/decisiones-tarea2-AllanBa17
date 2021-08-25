def main():
    #escribe tu código abajo de esta línea
    edad = int(input('Ingresa tu edad: '))
    if edad >= 18:
         tramite = str(input("¿Tienes identificacion oficial? (s/n): "))
         if tramite == 's':
             print("Trámite de licencia concedido")
         elif tramite == 'n':
             print("No cumples requisitos")
         elif tramite != 's' or tramite != 'n':
             print("Respuesta incorreta")
    elif edad < 18:
         print('No cumples requisitos')
    else:
         print("Respuesta incorrecta")
    
if __name__=='__main__':
    main()

