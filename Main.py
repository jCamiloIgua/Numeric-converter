#Menu de opciones de conversion
#Importante
#tipo: Esta varible almacena el tipo de dato a ingresar
#conversor: Es el tipo de dato a convertir

##Segundo Menu para seleccionar el valor de conversion
def switchDatos(opciones):
    ###
    #Seleccion Binario
    if opciones == 1: 
        tipo = "Binario" #Dato a convertir
        menuConvertirBinario()#Llamar las opciones de seleccion
        #Guardar la opcion para convertir
        conver = int(input("Ingrese la opcion que desea convertir: "))
        #Condicionales para seleccionar la conversion
        #Convertir Binario a Octal
        if conver == 1: 
            #Ingresar el dato a convertir
            dato = input("Ingresar el dato a convertir: ")
            #Tipo de dato para convertir
            conversor = "Octal"
            #Validar si es (dato) es correcto a tipo
            validacion = validarDato(dato,tipo)
            if validacion == True:#llama al metodo para la convertir
                print("El resultado es: " ,convertirBinario(dato,conversor))
            else:
                print("El número ingresado no corresponde, a un número binario.")
                #Volver al menu principal
                inicio()
        #Convertir Binario a Hexadecimal
        elif conver == 2:
            #Ingresar el dato a convertir
            dato = input("Ingresar el dato a convertir: ")
            #Tipo de dato para convertir
            conversor = "Hexadecimal"
            #Validar si es (dato) es correcto a tipo
            validacion = validarDato(dato,tipo)
            if validacion == True:#llama al metodo para la convertir
                print("El resultado es: " ,convertirBinario(dato,conversor))
            else:
                print("El número ingresado no corresponde, a un número binario.")
                inicio()
        #Convertir Binario a Decimal
        elif conver == 3:
            #Ingresar el dato a convertir
            dato = input("Ingresar el dato a convertir: ")
            #Tipo de dato para convertir
            conversor = "Decimal"
            #Validar si es (dato) es correcto a tipo
            validacion = validarDato(dato,tipo)
            if validacion == True:#llama al metodo para la convertir
                print("El resultado es: " ,convertirBinario(dato,conversor))
            else:
                print("El número ingresado no corresponde, a un número binario.")
                inicio()
        #Volver al menu principal
        elif conver == 4:
            inicio()
        else:
            return "Opcion no valida"
        
    ###
    #Seleccion Octal
    elif opciones == 2:
        tipo = "Octal" #Dato a convertir
        menuConvertirOctal()
        conver = int(input("Ingrese la opcion que desea convertir: "))
        #Convertir Octal a Binario
        if conver == 1:
            #Ingresar el dato a convertir
            dato = input("Ingresar el dato a convertir: ")
            #Tipo de dato para convertir
            conversor = "Binario"
            #Validar si es (dato) es correcto a tipo
            validacion = validarDato(dato,tipo)
            if validacion == True:#llama al metodo para convertir
                print("El resultado es: " ,convertirOctal(dato,conversor))
            else:
                print("El número ingresado no corresponde, a un número Octal.")
                inicio()
        #Convertir Octal a Hexadecimal
        elif conver == 2:
            #Ingresar el dato a convertir
            dato = input("Ingresar el dato a convertir: ")
            #Tipo de dato para convertir
            conversor = "Hexadecimal"
            #Validar si es (dato) es correcto a tipo
            validacion = validarDato(dato,tipo)
            if validacion == True:#llama al metodo para convertir
                print("El resultado es: " ,convertirOctal(dato,conversor))
            else:
                print("El número ingresado no corresponde, a un número Octal.")
                inicio()
        #Convertir Octal a Decimal
        elif conver == 3:
            #Ingresar el dato a convertir
            dato = input("Ingresar el dato a convertir: ")
            #Tipo de dato para convertir
            conversor = "Decimal"
            #Validar si es (dato) es correcto a tipo
            validacion = validarDato(dato,tipo)
            if validacion == True:#llama al metodo para convertir
                print("El resultado es: " ,convertirOctal(dato,conversor))
            else:
                print("El número ingresado no corresponde, a un número Octal.")
                inicio()
        #Volver al menu principal
        elif conver == 4:
            inicio()
        else:
            return "Opcion no valida"
        
    ###
    #Seleccion Hexadecimal
    elif opciones == 3:
        tipo = "Hexadecimal" #Dato a convertir
        menuConvertirHexadecimal()
        conver = int(input("Ingrese la opcion que desea con1vertir: "))
        #Convertir Hexadecimal a Binario
        if conver == 1:
            #Ingresar el dato a convertir
            dato = input("Ingresar el dato a convertir: ")
            #Tipo de dato para convertir
            conversor = "Binario"
            #Validar si es (dato) es correcto a tipo
            validacion = validarDato(dato,tipo)
            if validacion == True:#llama al metodo para convertir
                print("El resultado es: " ,convertirHexadecimal(dato,conversor))
            else:
                print("El número ingresado no corresponde, a un número Hexadecimal.")
                inicio()
        #Convertir Hexadecimal a Octal
        elif conver == 2:
            #Ingresar el dato a convertir
            dato = input("Ingresar el dato a convertir: ")
            #Tipo de dato para convertir
            conversor = "Octal"
            #Validar si es (dato) es correcto a tipo
            validacion = validarDato(dato,tipo)
            if validacion == True:#llama al metodo para convertir
                print("El resultado es: " ,convertirHexadecimal(dato,conversor))
            else:
                print("El número ingresado no corresponde, a un número Hexadecimal.")
                inicio()
        #Convertir Hexadecimal a Decimal
        elif conver == 3:
            #Ingresar el dato a convertir
            dato = input("Ingresar el dato a convertir: ")
            #Tipo de dato para convertir
            conversor = "Decimal"
            #Validar si es (dato) es correcto a tipo
            validacion = validarDato(dato,tipo)
            if validacion == True:#llama al metodo para convertir
                print("El resultado es: " ,convertirHexadecimal(dato,conversor))
            else:
                print("El número ingresado no corresponde, a un número Hexadecimal.")
                inicio()
        #Volver al menu principal
        elif conver == 4:
            inicio()
        else:
            return "Opcion no valida"
        
    ###
    #Seleccion Decimal
    elif opciones == 4:
        tipo = "Decimal" #Dato a convertir
        menuConvertirDecimal()
        conver = int(input("Ingrese la opcion que desea con1vertir: "))
        #Convertir Decimal a Binario
        if conver == 1:
            #Ingresar el dato a convertir
            dato = input("Ingresar el dato a convertir: ")
            #Tipo de dato para convertir
            conversor = "Binario"
            #Validar si es (dato) es correcto a tipo
            validacion = validarDato(dato,tipo)
            if validacion == True:#llama al metodo para convertir
                print("El resultado es: " ,convertirDecimal(dato,conversor))
            else:
                print("El número ingresado no corresponde, a un número Decimal.")
                inicio()
        #Convertir Decimal a Octal
        elif conver == 2:
            #Ingresar el dato a convertir
            dato = input("Ingresar el dato a convertir: ")
            #Tipo de dato para convertir
            conversor = "Octal"
            #Validar si es (dato) es correcto a tipo
            validacion = validarDato(dato,tipo)
            if validacion == True:#llama al metodo para convertir
                print("El resultado es: " ,convertirDecimal(dato,conversor))
            else:
                print("El número ingresado no corresponde, a un número Decimal.")
                inicio()
        #Convertir Decimal a Hexadecimal
        elif conver == 3:
            #Ingresar el dato a convertir
            dato = input("Ingresar el dato a convertir: ")
            #Tipo de dato para convertir
            conversor = "Hexadecimal"
            validacion = validarDato(dato,tipo)
            #Validar si es (dato) es correcto a tipo
            if validacion == True:#llama al metodo para convertir
                print("El resultado es: " ,convertirDecimal(dato,conversor))
            else:
                print("El número ingresado no corresponde, a un número Decimal.")
                inicio()
        #Volver al menu principal
        elif conver == 4:
            inicio()
        else:
            return "Opcion no valida"
    else:
        print("Opcion ingresada no valida")
        switchDatos()

################################################
#Opciones para el tipo de conversion
def menuConvertirBinario():
    print("Convertir de binario a: ")
    print(" 1. Octal")
    print(" 2. Hexadecimal")
    print(" 3. Decimal")
    print(" 4. Volver al menu anterior")

def menuConvertirOctal():
    print("Convertir de Octal a: ")
    print(" 1. Binario")
    print(" 2. Hexadecimal")
    print(" 3. Decimal")
    print(" 4. Volver al menu anterior")

def menuConvertirHexadecimal():
    print("Convertir de Hexadecimal a: ")
    print(" 1. Binario")
    print(" 2. Octal")
    print(" 3. Decimal")
    print(" 4. Volver al menu anterior")

def menuConvertirDecimal():
    print("Convertir de Decimal a: ")
    print(" 1. Binario")
    print(" 2. Octal")
    print(" 3. Hexadecimal")
    print(" 4. Volver al menu anterior")

#######################################
#Metodo para validar los datos ingresados
def validarDato(dato, tipo):
    #Validar Binario
    if tipo == "Binario":
            numeroBi = str(dato) 
            for digito in numeroBi: #Recorre el digito (Binarios: 1 y 0)
                if digito != '0' and digito != '1':
                    return False
            return True
    #Validar Octal
    elif tipo == "Octal":
        numeroOct = str(dato)
        for digito in numeroOct: #Recorre el digito (Octales: 0 - 7)
            if not digito.isdigit() or int(digito) > 7:
                return False
        return True
    #Validar Hexadecimal
    elif tipo == "Hexadecimal":
        numeroHex = str(dato)
        for digito in numeroHex: #Recorre el digito (Hexa: 0 - 9 y A - F)
            if not (digito.isdigit() or ('A' <= digito <= 'F') or ('a' <= digito <= 'f') ):
                return False
        return True

    #Validar Decimal  
    elif tipo == "Decimal":
        numero = str(dato)
        if numero.count('.') > 1: #No puede tener mas de un punto .
            return False
        if numero.replace('.','').isdigit():#todo el dato sin el punto sean numero para evitar ingreso de letras
            return True
        return False #no es un numero la entrada
    else:
        return False
#Metodos para convertir los datos#######################
#Metodo para convertir valores Binario
def convertirBinario(dato,conversor):
    #Binario a Octal
    if conversor == "Octal":
        """
        -Se añade ceros a la izquierda 
        -Se agrupa el numero binario en paquetes de 3 representan base 8
        - Cada grupo se convierte a octal usando base 2
        """
        tamano=3
        while len(dato) % tamano != 0: #Añadir los "0" a la izquierda para completar el paquete de 3
            dato = '0' + dato 
        Lista = []
        rs = ""
        for i in range(0, len(dato), tamano): #Crear la lista con los paquetes de 3 dijitos
            Lista.append(dato[i:i+tamano])
            
        for j in range(len(Lista)): #Recorrer la lista de paquetes
            decimal = 0
            potencia = 0
            for digito in reversed(Lista[j]): #Convertir de binario a Octal
                decimal += int(digito) * (2 ** potencia)
                potencia += 1
            rs += str(decimal)
        return rs   
    elif conversor == "Decimal":
        #Se llama al metodo con base 2
        return convertirDatoDecimal(dato,2)
    elif conversor == "Hexadecimal":
        hex_dict = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'} 
        while len(dato) % 4 != 0:  # Completar con ceros a la izquierda
            dato = '0' + dato
        hexadecimal = "" #guardar resultado final 
        for i in range(0, len(dato), 4):  # Tomar bloques de 4 bits
            bloque = dato[i:i+4]
            decimal = convertirDatoDecimal(bloque, 2)  # Convertir a decimal usando el metodo
            if decimal >= 10:  # Convertir valores 10-15 en A-F
                hexadecimal += hex_dict[decimal]  # Buscar en el diccionario
            else:
                hexadecimal += str(decimal)
        return hexadecimal
    else:
        return "No se encontro el tipo de convertidor"

#Metodo para convertir valores Octal
def convertirOctal(dato,conversor):
    if conversor == "Binario":  
        octal_a_binario = {#almacenar conversiones
        '0': '000', '1': '001', '2': '010', '3': '011',
        '4': '100', '5': '101', '6': '110', '7': '111'
        }
        binario = ""  # Variable para almacenar el resultado
        # Recorremos cada dígito del número octal
        for digito in dato:
            binario += octal_a_binario[digito]#remplazo con su valor binario
        binario = binario.lstrip('0') # se usa esto para eliminar lo 0 a la izquierda.
        return binario
    elif conversor == "Decimal": 
    #Se llama al metodo con base 8
        return convertirDatoDecimal(dato,8)
    elif conversor == "Hexadecimal": 
        #convertir octal a decimal
        decimal = convertirDatoDecimal(dato, 8)
        hex = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
        hexadecimal = "" #dato convertido
        #Convertir de decimal a hexadecimal
        while decimal > 0:
            residuo = decimal % 16  # Obtener el residuo (dígito hexadecimal)
            if residuo >= 10:
                hexadecimal = hex[residuo] + hexadecimal  # Convertir a A-F
            else:
                hexadecimal = str(residuo) + hexadecimal  # Mantener números 0-9
            decimal //= 16  # Dividir por 16 para seguir con el siguiente dígito
        return hexadecimal if hexadecimal else "0"  # Retorna "0" si el número es 0
    else:
        return "No se encontro el tipo de convertidor"

#Metodo para convertir valores decimal  
def convertirDecimal(dato,conversor):
    dato = float(dato) # convertir dato a decimal

    if conversor == "Binario":#decimal a binario
        p_entera = int(dato) # parte entera del dato
        p_decimal = dato - p_entera #parte decimal
        #convertir parte entera
        binario_entero = "" #guardar binario entero
        if p_entera == 0:
            binario_entero == "0"
        while p_entera > 0:     #residuo division
            binario_entero = str(p_entera % 2) + binario_entero
            p_entera //=2 #dividir el numero por 2 mas pequeño
        #cuando se termine el ciclo la variable binario_entero
        #tiene los valores de los residuos de la parte entera del numero

        #Convertir parte decimal
        binario_decimal = ""#guardar binario decimal
        precision = 10 #numeros de cifras significativas a tomar
        while p_decimal > 0 and len(binario_decimal) < precision:
            p_decimal *=2
            digito = int(p_decimal) #parte entera se obtiene mutiplicar * 2
            binario_decimal += str(digito)
            p_decimal -= digito
        #unir cada parte
        if binario_decimal: #si binario tiene algo se ingreso un numero decimal
            return binario_entero + '.' + binario_decimal
        return binario_entero # se ingreso un entero
    
    elif conversor == "Octal":
        p_entera = int(dato)# parte entera del dato
        p_decimal = dato - p_entera #parte decimal

        residuos = [] #guardar los residuos
        #parte entera a octal
        while p_entera > 0:
            residuos.append(p_entera % 8) #guardar residuo
            p_entera //=8 #dividir el numero por 8
        #Invertir la lista y unir los valores en una cadena
        #si residuos esta vacio se usa el if, para evitar la union de un valor vacio en residuos []
        octal_entero = ''.join(map(str, residuos[::-1])) if residuos else "0"
        #parte decimal a octal
        octal_decimal = "" #guardar los valores decimales
        precision = 10
        while p_decimal > 0 and len(octal_decimal) < precision:
            p_decimal *=8
            digito = int(p_decimal)
            octal_decimal += str(digito)
            p_decimal -= digito
        #union de partes
        if octal_decimal:
            return octal_entero + '.' + octal_decimal
        return octal_entero

    elif conversor == "Hexadecimal":
        dato = float(dato)  # Convertir a flotante
        p_entera = int(dato)  # Parte entera
        hexa_entero = "0"  # Inicializar en caso de que el número sea menor a 1
        hex = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    # Convertir parte entera
    if p_entera > 0:
        residuos = []
        while p_entera > 0:
            hexadecimal = p_entera % 16
            if hexadecimal >= 10:
                residuos.append(hex[hexadecimal])  # Convertir a A-F
            else:
                residuos.append(str(hexadecimal))  # Mantener números 0-9
            p_entera //= 16  # Dividir por 16 para seguir con el siguiente dígito
        hexa_entero = ''.join(residuos[::-1])  # Orden correcto

    # Convertir parte decimal
    p_decimal = dato - int(dato)  # Extraer parte decimal
    hexa_decimal = ""
    precision = 10  # Número de cifras decimales 
    while p_decimal > 0 and len(hexa_decimal) < precision:
        p_decimal *= 16
        digito = int(p_decimal)
        if digito >= 10:
            hexa_decimal += hex[digito]
        else:
            hexa_decimal += str(digito)
        p_decimal -= digito

    # Unir ambas partes
    if hexa_decimal:
        return hexa_entero + '.' + hexa_decimal
    return hexa_entero

#Metodo convertir valores hexadecimal
def convertirHexadecimal(dato,conversor):
    if conversor == "Binario":
        decimalHex = convertirDatoDecimal(dato,16)
        binario = ""
        while decimalHex > 0:
            residuo = decimalHex % 2
            binario = str(residuo) + binario #al inicio el residuo
            decimalHex //= 2 #dividimos el numero entre dos division sin decimales
        return binario
    elif conversor == "Decimal":
        #Se llama al metodo base 16
        return convertirDatoDecimal(dato,16)
    elif conversor == "Octal":
        #convertir hexa a decimal
        decimal = convertirDatoDecimal(dato, 16)
        #decimal a octal
        if decimal == 0:
            return "0" 
        octal = ""#guardar valor
        while decimal > 0:
            octal = str(decimal % 8) + octal  # Obtener el residuo para crear el octal
            decimal //= 8  # Dividir por 8 para seguir con el siguiente dígito
        return octal  
    else:
        return "No se encontro el tipo de convertidor"
##################
#Metodo para convertir binario / octal y hexa a decimal
def convertirDatoDecimal(dato,base):
    hex = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}  # Diccionario para valores hexadecimales
    decimal = 0 #almacena el resultado de la conversion
    potencia = 0
    #Con reversed se recorre los digitos de manera inversa
    for digito in reversed(dato.upper()):#convertir mayusculas
        if(digito.isdigit()): #Binario / octal (1 al 7)numero del 0 al 9 a entero
            valor = int(digito)
        else: #tiene una letra A - F hexadecimal
            valor = hex[digito]#buscar valor diccionario

        decimal += valor * (base ** potencia)#conversion
        potencia +=1#aumentar la potencia
    return decimal


#######################################################
###Convertidor de Numeros Menu principal        
def inicio():
    print("<<Convertidor de Numeros>>")
    print("¿Selecciona el tipo de dato a ingresar?: ")
    print(" 1. Binario")
    print(" 2. Octal")
    print(" 3. Hexadecimal")
    print(" 4. Decimal")
    opciones = int(input("Digite su eleccion: "))
    switchDatos(opciones)#Se envia la seleccion al menu
#llamado del menu de la aplicacion.
inicio()
########################################################3