
# FUNCIONES
def menu():
    print("Lista de contactos")

    # print para espacio
    print("")
    # Menu
    print("1. Imprimir los contactos")
    print("2. Guardar nuevo contacto")
    print("3. Editar contacto existente")
    print("4. Eliminar contacto")
    print("5. Salir")
    # print para espacio
    print("")

    opcion = input("Escoja el el numero de la opcion que desea realizar: ").strip()

    # print para espacio
    print("")
    return opcion

# para evitar que envien cadenas de texto vacias se creo la siguiente funcion de input con varios intentos
def input_dato_valido(tipo):
    contador = 0
    while contador < 3:
        valor = input(f"Ingrese el {tipo} del contacto: ")
        if valor:
            return valor
        else:
            contador += 1
            print(f"Ingrese un {tipo} valido")
            print(f"Intento {contador}/3. El campo no puede estar vacío.")
            
    print("Excedio el limite de intentos de ingresar un valor valido")
    return None

# iniciar la diccionario
contactos = {}

# LOGICA DE MENU

while True:
    # imprimir menu
    op = menu()

    # VER CONTACTOS
    if op == "1":
        print("")
        print("Imprimiendo su lista de contactos")
        print("")
        # imprimir todos los cantactos en una tabla ordenada
        for nombre, celular in contactos.items():
            print(f"{nombre} --------- {celular}")
        
        # print para espacio
        print("")
        # volver al menu
        input("Aplaste enter para volver al menu ")
    # GUARDAR
    elif op == "2":
        print("")
        print("Guardando contacto")
        print("")
        ## preguntando el nombre del contacto
        nombre = input_dato_valido(tipo="nombre")
        
        # verificando que el input no haya recibido una cadena vacia
        if not nombre:
            # si manda una cadena vacia lo devuelve al menu
            continue

        # verificando que el contacto no se encuentre registrado
        if nombre in contactos:
            print(f"El contacto ya se encuentra registrado con el numero {contactos[nombre]}")
            continue

        # guardando el celular 
        num_cell = input_dato_valido(tipo="celular")
        if not num_cell:
            # devuelve al menu
            continue
        # Una ves verificado los pasos anteriores
        # se registra el nuevo contacto
        contactos[nombre] = num_cell
        print(f"Contacto guardado como {nombre}: {contactos[nombre]} ")


    # EDITAR
    elif op == "3":
        print("")
        print("Buscando contacto para editar")
        print("")
        # bucar a traves del nombre el contacto a editar
        nombre = input_dato_valido(tipo="nombre")

        # verificando si el nombre ya se encuentra registrado
        if nombre not in contactos:
            # notificamos que esta registrado y lo mandamos al menu nuevamente
            print(f"El nombre no se encuentra registrado en su lista de contactos")
            continue
        
        # imprimir el contacto a editar            
        print("")
        print(f"{nombre} --------- {contactos[nombre]}")
        # escoger que va a editar
        
        print("1. Cambiar nombre")
        print("2. Cambiar numero")
        cambio = input("Escoja la opcion: ").strip()
        # cambiando el nombre
        if cambio == "1":
            nuevo_nombre = input_dato_valido(tipo="nombre")
            if not nuevo_nombre:
                # no ingreso texto en el nuevo nombre, entonces lo devolvemos al menu
                continue

            # borramos el anterior debido a que la claves en el diccionario son inmutables, y creamos el nuevo contacto con el mismo nombre.
            contactos[nuevo_nombre] = contactos.pop(nombre)
            # mostrar el contacto actualiazado
            print(f"El contacto {nuevo_nombre} ha sido actualizado a {contactos[nuevo_nombre]}")
            
        # cambiando el numero
        elif cambio == "2":
            nuevo_numero = input_dato_valido(tipo="celular")
            contactos[nombre] = nuevo_numero
            # mostrar el contacto actualiazado
            print(f"El contacto {contactos[nombre]} ha sido actualizado")
        else:
            print("Porfavor escoja una opcion correcta")


    # ELIMINAR
    elif op == "4":
        print("")
        print("Buscando contacto para Eliminar")
        print("")
        # bucar a traves del nombre el contacto a eliminar
        nombre = input_dato_valido(tipo="nombre")
        # verificando si el nombre esta vacio
        if not nombre:
            # como esta vacio lo mandamos al menu
            continue

        # verificando si el nombre no existe en la lista de contactos
        if nombre not in contactos:
            print("El nombre ingresado no consta en su lista de contactos!")
            # como no existe no se puede eliminar por lo que lo mandamos al menu
            continue
        
        # si llegamos hasta aqui es porque si existe, entonces procedemos a eliminar ambos items
        contactos.pop(nombre)
        print(f"El contacto {nombre} ha sido eliminado.")
        

    elif op == "5":
        print("")
        # salir
        print("Ha salido correctamente de la lista de contactos")
        break

    else:
        print("")
        print("Porfavor ingrese una opcion valiada")
