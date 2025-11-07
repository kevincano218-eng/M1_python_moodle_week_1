print ("Bienvenido al inventario")
print ("------------------------")
# PEDIR DATOS AL USUARIO
nombre = input ("Digita el nombre del producto: ")




#se separa los datos numericos para que el ciclo cada vez que ingrese un dato diferente lo pregunte con la etiqueta "try"
# Se reliza condicional "elif" y dentro, "exit" para dar la opcion al usuario de salirse del programa anticipadamente si lo prefiere.
while True:
    
    try:
        precio = int (input ("Para SALIR, digite 0***\nDigita el precio: "))
        if (precio < 0):
            print ("Debes digitar un valor positivo.")
        elif (precio == 0):
            print("Cerrando sistema...")
            exit()
        else:
            break
    except ValueError: 
        print ("Debes digitar un valor numerico.")
        
# se hace otro while para que cumpla con el ciclo especifico de la cantidad y no se tenga que repetir todas las preguntas si se erra algun dato
while True:
    
    try:
        
        cantidad = int (input ("Para SALIR, digite 0***\nDigita la cantidad: "))
        if (cantidad < 0):
            print ("Digite un valor positivo.")
        else:
            break
    except ValueError:
        print ("Debes digite un valor numerico.")

costo_total = precio * cantidad 
# con el "print" se pone un mensaje que resalte las variables establecidas y formen el mensaje 
print (f"Producto seleccionado: {nombre}.\n Precio unitario: ${precio} P/U.\n Cantidad seleccionada: {cantidad}.\n COSTO TOTAL A PAGAR: ${costo_total}")
    