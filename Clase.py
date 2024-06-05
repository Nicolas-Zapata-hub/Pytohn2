import os
import msvcrt
import csv
while True:
    clases = {1,2,3,4,5,6,7,8,9,10}    
    usuarios = []
    print("<<<Press any key to continue>>>")
    msvcrt.getch()
    os.system("cls")
    print(f""""
        
    1. Registrar un nuevo usuario.
    2. Reservar una clase y generar reporte CSV.
    3. Consultar clases disponibles.
    4. Consultar reservas de un usuario.
    5. Salir del programa """)
    opcion = int(input("Seleccione : "))
    if opcion==5:
        print("Adios 👋") 
    elif opcion==1:
        nombre = input("Ingrese el nombre : ")
        if nombre>5:
            print("Nombre registrado")
            usuarios.append(nombre)
        id = float(input("Ingrese su id (El id debe tener más de 5 numeros) : "))
        if id>4:
            usuarios.append(id=nombre)
            print("ID Registrado")
    elif opcion==2:
        print(f"""Que clase desea reservar?
              
              1.- Clase introductoria
              2.- Clase avanzada
              3.- Clase de reapaso
              4.- Clase de contenido nuevo
              5.- Clase de repaso 
              6.- Clase de entrenamiento
              7.- Clase de simulacro de la prueba
              8.- Clase de repaso
              9.- Actividad de trabajo en equipo
              10.- la prueba """)  
        seleccion = int(input("Seleccione : "))   
        if seleccion==1:
            print("Clase intrductoria reservada")
        elif seleccion==2:
            print("Clase de avanzada reservada") 
        elif seleccion==3:
            print("Clase de repaso reservada")            
        elif seleccion==4:
            print("Clase de contenido nuevo reservada") 
        elif seleccion==5:
            print("Clase de repaso  reservada") 
        elif seleccion==6:
            print("Clase de entrenamiento reservada") 
        elif seleccion==7:
            print("Clase de simulacro de prueba reservada")
        elif seleccion==8:
            print("Clase de repaso reservada") 
        elif seleccion==9:
            print("Clase actividad de trabajo en equipo reservada") 
        elif seleccion==10:
            print("La prueba reservada")                              