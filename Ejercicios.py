#Funcion para imprimir filas de astericos segun un numero ingresado
def Dibujo(Numero1):
    x=1
    while x<=Numero1 :
        print("*"*x, end="")
        x=x+1
        print("")
    print("")

#Funcion que va restando i al numero enviado desde consola
def Descenso (Numero1):
    for i in range (Numero1+1):
        print(Numero1 -i,end=", ")
    print("\n")

#Funcion que revisa el modular de dos numeros y verifica si el numero enviado
# como parametro es primo segun un valor booleano.
def Primo (Evaluar):
    if(Evaluar == 2):
        print("Es primo\n")  
    elif(Evaluar<2):
        print("No es primo\n")
    else:
        EsPrimo = True
        for i in range (2,Evaluar):
            if(Evaluar % i == 0):
                EsPrimo = False
        if(EsPrimo == True):
            print("Es primo\n")
        else:
            print("No es primo\n")
        
print("\n------------------Bienvenido------------------")

Seguir = True

while Seguir ==True:

    print("Puedes ingresar el numero del ejercicio que deseas realizar")
    print("1.Asteriscos.\n2.Cuenta regresiva.\n3.Verificacion de numero primo.\n4Terminar.")
    Opcion = int (input(">"))

    while Opcion>4 or 1>Opcion:
        print("Digita un numero dentro de las opciones mostradas")
        print("1.Asteriscos.\n2.Cuenta regresiva.\n3.Verificacion de numero primo.")
        Opcion = int (input(">"))



    if Opcion == 1:
        print("Ingresa un numero entero")
        Numero1 = int (input(">"))
        Dibujo(Numero1)

    elif Opcion == 2:
        print("Ingresa un numero entero")
        Numero1 = int (input(">"))
        Descenso(Numero1)

    elif Opcion == 3:
        print("Ingresa un numero entero")
        Numero1 = int (input(">"))
        Primo(Numero1) 

    elif Opcion == 4:
        Seguir = False  
        print ("------ Fin ------") 

#Fin 