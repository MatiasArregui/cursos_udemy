def traductor(oracion):
    # dividir oracion en palabras
    listaOracion = oracion.split()
    # recorrer palabras y convertirlas con el traductor
    listaNueva = []
    for x in listaOracion:  
        palabra = ""
        # comienza con vocal, solamente agregar "yay"
        if x[0] in "aeiou":
            palabra = x + "yay"
            listaNueva.append(palabra)
        else:
            # comienza con consonante, mover al final esta y agregar ay   
            # x = x[1:] + x[0] + "ay"
            palabra = x[1:] + x[0] + "ay"
            listaNueva.append(palabra)
 
    # unir palabras en una oracion
    oracion =" ".join(listaNueva)
    # generar cadena final
    print(oracion.lstrip(" "))
    
    
def traductor2(oracion):
    # dividir oracion en palabras
    listaOracion = oracion.split()
    # recorrer palabras y convertirlas con el traductor
    for x in range(len(listaOracion)):  
        # comienza con vocal, solamente agregar "yay"
        if listaOracion[x][0] in "aeiou":
            listaOracion[x] = listaOracion[x] + "yay"
        else:
            # comienza con consonante, mover al final esta y agregar ay   
            listaOracion[x] = listaOracion[x][1:] + listaOracion[x][0] + "ay"
 
    # unir palabras en una oracion
    oracion =" ".join(listaOracion)
    # generar cadena final
    print(oracion.lstrip(" "))


# obtener oracion del usuario
oracion = input("Ingresa la oracion: ").strip().lower()
traductor2(oracion)

