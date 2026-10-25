#Cifrado de Cesar
def Cifrado_Cesar(Texto, Shift):
            Abecedario = 'abcdefghijklmnopqrstuvwxyz'
            cifrado = Abecedario[Shift:] + Abecedario[:Shift]
            tabla = str.maketrans(Abecedario, cifrado)
            Texto_cifrado = Texto.translate(tabla)
            return Texto_cifrado

# DESCIFRADO DE TEXTO
def Descifrado_Cesar(Texto, Shift):
            Abecedario = 'abcdefghijklmnopqrstuvwxyz'
            cifrado = Abecedario[Shift:] + Abecedario[:Shift]
            tabla = str.maketrans(cifrado, Abecedario)
            Texto_descifrado = Texto.translate(tabla)
            return Texto_descifrado


#Menu de opciones
while True:
    print ('Elije la opcion deseada')
    print ('1.Cifrar un texto'  \
    '  2.Descifrar un texto    ')
    print ('3.Salir del programa')
    Respuesta = input ('Ingrese la opcion deseada: ')   

    #Cifrado de texto

    if Respuesta == '1':
        print ('Cifrado de texto')
        Texto = input ('Ingrese el texto a cifrar: ')
        Shift = int(input ('Ingrese el desplazamiento: '))
        Texto_cifrado = Cifrado_Cesar(Texto, Shift)
        print ('Texto cifrado:', Texto_cifrado)

    
    elif Respuesta == '2':
        print ('Descifrado de texto')
        Texto = input ('Ingrese el texto a descifrar: ')
        Shift = int(input ('Ingrese el desplazamiento: '))
        Texto_descifrado = Descifrado_Cesar(Texto, Shift)
        print ('Texto descifrado:', Texto_descifrado)


    elif Respuesta == '3':
        print ('Saliendo del programa')
        break

else:
    print ('Opcion no valida')