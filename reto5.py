try:  
    import os#para interactuar con el SO
    import time#Para hacer una pausa entre Reto1 y Reto 2
    import math#Funciones matematicas RETO4
    #FUNCIONES
    #FUNCIÓN PARA LIMPIAR PANTALLA, PRIMERO VALIDA SOBRE QUE SISTEMA OPERATIVO ESTÁ CORRIENDO EL PROGRAMA
    '''Se definen el usuario y contraseña según RF02
    y se almacenan como str teniendo en cuenta que un
    usuario o contraseña pueden ser alfanuméricos'''
    idGroup="51675"
    secret="57615"
    matCoor= []#RF02 Reto 3
    def clear():
        if os.name == "posix":#Unix/Linux/MacOS/BSD
            os.system ("clear")
        elif os.name in ("ce", "nt", "dos"):#DOS/Windows
            os.system ("cls")
    #RETO1
    def reto1():
        clear()
        #RF01
        #Se imprime el mensaje de bienvenida solicitado en RF01
        print("=====================================================================")
        print('"Bienvenido al sistema de ubicación para zonas públicas WIFI"')
        print("=====================================================================")
        #RF02
        '''Se definen el usuario y contraseña según RF02
        y se almacenan como str teniendo en cuenta que un
        usuario o contraseña pueden ser alfanuméricos'''
        idGroup=str("51675")
        secret=str("57615")
        resultado = ""
        #Captura de datos de entrada: usuario
        idtyped=input("Ingrese usuario: ")
        print("")
        #Validación de usuario
        if idGroup == idtyped:
            #Captura de datos de entrada: contraseña
            secretTyped=str(input("Ingrese contraseña: "))
            print("")
            #Validación de contraseña
            if secret == secretTyped:
                #RF03
                #Cálculo de capcha, se almacena como str para facilitar la contatenación
                capchaSub1=""
                for i in [3,2,1]:
                    capchaSub1=capchaSub1+str(idGroup[len(idGroup)-i])
                #capchaSub2=str((5%6)+(1**3))
                capchaSub2=str(((int(idGroup[0])+int(idGroup[2]))-int(idGroup[4]))+int(idGroup[1]))
                capcha=capchaSub1+"+"+capchaSub2
                #Captura de datos de entrada: capcha convertido a int
                capchaTyped=(input("ingrese el resultado de la operación "+capcha+" = "))
                print("")
                #Validación de capcha
                if capchaTyped == str((int(capchaSub1)+int(capchaSub2))):
                    #Almacena mensaje de confirmación para RF04
                    #Datos de salida RF03
                    resultado="Sesión iniciada"
                else:
                    print("=====================================================================")
                    #Datos de salida RF03
                    print("Error")
            else:
                print("=====================================================================")
                #Datos de salida RF02
                print("Error")
        else:
            print("=====================================================================")
            #Datos de salida RF01
            print("Error")
        #RF04
        #Se valida mensaje de confirmación
        if resultado == "Sesión iniciada":
            print("=====================================================================")
            #Datos de salida RF04
            print("Se espera un mensaje de confirmación de inicio de sesión con éxito.")
            print("\n")
            print(resultado)
            print("...")
            time.sleep(2)
            reto2(idGroup)
            
        #INICIA EL RETO2
        #PAUSA ANTES DE LIMPIAR PANTALLA PARA QUE EL USUARIO PUEDA LEER LA CONFIRMACION DE INICIO DE SESIÓN
        
    #RETO 2
    def reto2(idGroup):
        clear()
        contErrores = 0
        disparadorCoordenadas = False
        disparadorUbicacionActual = False
        ubicacionActual = None #RETO CUATRO
        RedDestino = None #RETO CUATRO
        distanciaDestino = None #RETO CUATRO
        tMoto = 0 #RETO CUATRO
        transporte = "Moto"
        ubicaciones = ["trabajo","casa","parque"]
        tipoCoordenada = ["Latitud","Longitud"]
        rangoMatriz = [[1.998,1.740],#Latitud Superior,Inferior
                    [-75.689,-75.950]]#Longitud Oriental, Occidental
        #RETO 4 RF1 MATRIZ
        redesMatriz = [[1.811,-75.820,58],
                    [1.919,-75.843,1290],
                    [1.875,-75.877,110],
                    [1.938,-75.764,114]]# Latitud, Longitud, Promedio usuarios

        #Lista original menú
        menu=[". Cambiar contraseña",
                ". Ingresar coordenadas actuales",
                ". Ubicar zona wifi más cercana",
                ". Guardar archivo con ubicación cercana",
                ". Actualizar registros de zonas wifi desde archivo",
                ". Elegir opción de menú favorita",
                ". Cerrar sesión"]
        opcion=""
        def validarOpcion(opcion,tipo):
            if tipo == 1:
                indexValidar = ["1","2","3","4","5","6","7"]
            elif tipo == 6:
                indexValidar = ["1","2","3","4","5"]
            if opcion in indexValidar:
                return True
        #Funcion principal para navegar por el menú
        def seleccionOpcion():
            nonlocal opcion
            nonlocal contErrores
            nonlocal disparadorCoordenadas
            nonlocal disparadorUbicacionActual #RF01 RETO 5
            nonlocal ubicacionActual
            nonlocal RedDestino
            nonlocal distanciaDestino
            opcion=input("Elija una opción: ")
            if validarOpcion(opcion,1):
                contErrores = 0
                #RF01 RETO3 Cambiar contraseña
                if (menu[(int(opcion))-1])[2:] == "Cambiar contraseña":
                    if cambiarContraseña():
                        print("\n")
                        printMenu(menu)
                    #¿las solicitudes de contraseña se evaluan con un texto exacto?
                    #CUAL DEBE SER LA SALIDA SI LA NUEVA CONTRASEÑA ES IGUAL A LA ANTERIOR
                    #QUE PASA SI SE REORDENÓ EL MENÚ, EL RF01 SIGUE EVALUANDO LA OPCION 1?
                elif (menu[(int(opcion))-1])[2:] == "Ingresar coordenadas actuales":
                    print("\n")
                    if disparadorCoordenadas == True:
                        if actualizarCoordenada():
                            print("\n")
                            printMenu(menu)   
                    elif ingresaCoordenada():
                        disparadorCoordenadas = True
                        print("\n")
                        printMenu(menu)
                #RETO 4 RF02 UBICAR WIFI CERCANA
                elif (menu[(int(opcion))-1])[2:] == "Ubicar zona wifi más cercana":
                    print("\n")
                    if disparadorCoordenadas == True:
                        printcoordenadas()
                        ubicacionActual = input("Por favor elija su ubicación actual (1,2 ó 3) para calcular la distancia a los puntos de conexión: ")
                        if ubicacionActual in ["1","2","3"]:
                            distanciaDestino, RedDestino = Caldistancia(ubicacionActual)
                            calculaTiempo(distanciaDestino, RedDestino, ubicacionActual)
                        else:
                            print("Error ubicación")
                            exit()
                    else:
                        print("Error sin registro de coordenadas")
                        exit()
                elif (menu[(int(opcion))-1])[2:] == "Guardar archivo con ubicación cercana":
                    #RF01 RETO 5
                    if (disparadorCoordenadas == True and disparadorUbicacionActual == True): #Opción 2 #Opción 3
                            guardarArchivoWifi(ubicacionActual,RedDestino,distanciaDestino,transporte,tMoto)
                            #(actual,zonawifi1,distancia,mediotransporte,tiempopromedio)
                    else:
                        print("Error de alistamiento")
                        exit()
                elif (menu[(int(opcion))-1])[2:] == "Actualizar registros de zonas wifi desde archivo":
                    actualizarRedesWifi()
                #RF02 Elegir opción favorita
                elif opcion == "6":
                    print("\n")
                    opcion=input('Seleccione opción favorita: ')
                    if validarOpcion(opcion,6):
                        adivinanza()
                    else:
                        clear()
                        print("Error\n")
                #RF05 El programa permite al usuario salir del menú.
                elif opcion == "7":
                    print("Hasta pronto")
                    #print(menu[opcion-1])
                    #print((menu[(int(opcion))-1])[2:])
                    exit()
                else:
                    #RF04 Seleccion opciones 1 a 5
                    print("\nUsted ha elegido la opción "+opcion+"\n")
                    exit()
            else:
                #RF03 contador de errores menu principal
                clear()
                print("Error\n")
                contErrores += 1
                if contErrores > 3:
                    exit()
                else:
                    printMenu(menu)
        #RF02 Funcion para ordenar meno de favoritos
        def ordenarFavoritos():
            nonlocal opcion
            nonlocal menu
            favorito = menu.pop(((int(opcion))-1))
            #menu.remove(favorito)
            menu.insert(0,favorito)
            clear()
            printMenu(menu)
        #RF02 Confirmacion de cambio de favorito
        def adivinanza():
            ad1 = input('Para confirmar por favor responda: Me llaman el cuarto primo: ')
            if ad1 == idGroup[(len(idGroup)-2)]:
                print('\n')
                ad2 = input('Para confirmar por favor responda: Soy el tercer primo: ')
                if ad2 == idGroup[(len(idGroup)-1)]:
                    ordenarFavoritos()
                else:
                    print('\nError\n')
                    printMenu(menu)
            else:
                print('\nError\n')
                printMenu(menu)
        #RF01 Funcion para imprimir menu
        def printMenu(menu):
            for i in range(0, len(menu)):
                print(str(i+1)+menu[i])
                #print("{}{}".format(i+1,menu[i]))
            print("\n")
            #RF02
            seleccionOpcion()
        #RF01 RETO 3 Cambiar contraseña
        def cambiarContraseña():
            global secret
            temp = input("Ingrese su contraseña actual: ")
            if temp == secret:
                temp = input("Ingrese nueva contraseña: ")
                if temp == secret:
                    print('\nError\n')
                    exit()
                else:
                    secret = temp
                    return True
            else:
                print('\nError\n')
                exit()
            #print((menu[(int(opcion))-1])[2:])
        #RF02 RETO 3 Ingresar coordenadas iniciales
        def ingresaCoordenada():
            nonlocal ubicaciones
            nonlocal tipoCoordenada
            nonlocal rangoMatriz
            for i in range(3):#Filas
                matCoor.append([])
                for j in range(2):#Columnas
                    try:
                        coordenada = float(input(f"Ingrese {tipoCoordenada[j]} de {ubicaciones[i]}: "))
                    except ValueError:
                        print("Error")
                        exit()
                    if coordenada <= rangoMatriz[j][0] and coordenada >= rangoMatriz[j][1]:
                        matCoor[i].append(coordenada)
                    else:
                        print("Error coordenada")
                        exit()
            for i in range(3):
                print (matCoor[i])
            return True
        #RF03 RETO 3 Actualizar coordenadas
        def actualizarCoordenada():
            nonlocal ubicaciones
            nonlocal tipoCoordenada
            nonlocal rangoMatriz
            printcoordenadas()
            print("-Coordenada ubicada más al sur")
            print("-Coordenada ubicada más al oriente")
            fila = input("Presione 1,2 ó 3 para actualizar la respectiva coordenada. Presione 0 para regresar al menú")
            if fila in ("1","2","3"):
                fila = int(fila)-1
                #Validacion de coordenadas según RF02 reto 3
                for j in range(2):#Columnas
                        try:
                            coordenada = float(input(f"Ingrese {tipoCoordenada[j]} de {ubicaciones[fila]}: "))
                        except ValueError:
                            print("Error")
                            exit()
                        if coordenada <= rangoMatriz[j][0] and coordenada >= rangoMatriz[j][1]:
                            #matCoor[fila].append(coordenada)
                            matCoor[fila][j]= coordenada
                        else:
                            print("Error coordenada")
                            exit()
                for i in range(3):#temporal
                    print (matCoor[i])
                return True
            elif fila == "0":
                return True
            else:
                print("Error actualización")
                exit()
        #RF03 RETO 3 Actualizar coordenadas
        def printcoordenadas():
            global matCoor
            for i in range(3):
                print(f"coordenada [latitud,longitud] {i+1} :  ['{matCoor[i][0]}', '{matCoor[i][1]}']")
        #RF02 RETO 4 Calcular distancia de ubicacion actual
        def Caldistancia(ubicacion):
            #print("calculando distancias "+ubicacion)
            ubicacion= int(ubicacion)-1
            r= 6372.795477598*1000 #Radio en metros
            
            distancia = list()
            for i in range(4):
                dLat= math.radians(redesMatriz[i][0])-math.radians(matCoor[ubicacion][0])
                Dlon= math.radians(redesMatriz[i][1])-math.radians(matCoor[ubicacion][1])
                distancia.append(2*r*math.asin(math.sqrt(math.pow(math.sin(dLat/2),2)+(math.cos(math.radians(matCoor[ubicacion][0]))*math.cos(math.radians(redesMatriz[i][0]))*math.pow(math.sin(Dlon/2),2)))))
            disTemporal = distancia #copia temporal lista
            disMenor= min(distancia) #Busca menor
            indiceMenor= distancia.index(disMenor) #busca indice menor
            disTemporal.remove(disMenor) #Remueve menor de lista temporal
            disMenor2 = min(disTemporal) #busca segundo menor
            indiceMenor2= distancia.index(disMenor2) #busca indice de segundo menor
            disMenor = "{0:.0f}".format(disMenor)
            disMenor2 = "{0:.0f}".format(disMenor2)
            print("Zonas wifi cercanas con menos usuarios")
            if redesMatriz[indiceMenor][2] <= redesMatriz[indiceMenor2][2]:
                print("La zona wifi 1: ubicada en ['{}','{}'] a {} metros , tiene en promedio {} usuarios".format(redesMatriz[indiceMenor][0],redesMatriz[indiceMenor][1],disMenor,redesMatriz[indiceMenor][2]))
                print("La zona wifi 2: ubicada en ['{}','{}'] a {} metros , tiene en promedio {} usuarios".format(redesMatriz[indiceMenor2][0],redesMatriz[indiceMenor2][1],disMenor2,redesMatriz[indiceMenor2][2]))
                indice1 = indiceMenor
                indice2 = indiceMenor2
                dit1= disMenor
                dit2= disMenor2
            else:
                print("La zona wifi 1: ubicada en ['{}','{}'] a {} metros , tiene en promedio {} usuarios".format(redesMatriz[indiceMenor2][0],redesMatriz[indiceMenor2][1],disMenor2,redesMatriz[indiceMenor2][2]))
                print("La zona wifi 2: ubicada en ['{}','{}'] a {} metros , tiene en promedio {} usuarios".format(redesMatriz[indiceMenor][0],redesMatriz[indiceMenor][1],disMenor,redesMatriz[indiceMenor][2]))
                indice1 = indiceMenor2
                indice2 = indiceMenor
                dit1= disMenor2
                dit2= disMenor
            zonaWifiDestino= input("Elija 1 o 2 para recibir indicaciones de llegada")
            #RF03 RETO 4
            if zonaWifiDestino == "1":
                return dit1, indice1
            elif zonaWifiDestino == "2":
                return dit2, indice2
            else:
                print("Error zona wifi")
                exit()
        #RF03 RETO 4 CALCULAR RECORRIDO
        def calculaTiempo(distancia, RedDestino, ubicacionActual):
            nonlocal tMoto
            nonlocal disparadorUbicacionActual
            disparadorUbicacionActual = True
            velPie = 0.483 #Velocidades en m/s
            velmoto = 19.44 #Velocidades en m/s
            ubicacionActual = int(ubicacionActual)-1
            #DIRECCION
            if matCoor[ubicacionActual][0] < redesMatriz[RedDestino][0]: #LATITUD
                y = "norte"
            else:
                y= "sur"
            if matCoor[ubicacionActual][1] < redesMatriz[RedDestino][1]: #LONGITUD
                x = "occidente"
            else:
                x = "oriente"
            tPie = (int(distancia)/velPie)/60
            tMoto = (int(distancia)/velmoto)/60
            print(f"Para llegar a la zona wifi dirigirse primero al {x} y luego hacia el {y}")
            print(f"-Tiempo en moto {tMoto}\n-Tiempo a pie {tPie}")
            regresoMenu= input("Presione 0 para salir")
            if  regresoMenu == "0":
                clear()
                printMenu(menu)
            else:
                print("Error")
                exit()            
        def guardarArchivoWifi(actual,zonawifi1,distancia,mediotransporte,tiempopromedio):
            informacion = {
                'actual': matCoor[int(actual)-1],
                'zonawifi1': redesMatriz[int(zonawifi1)],
                'recorrido': [distancia, mediotransporte,
                            tiempopromedio]
                }
            print(informacion)
            exportar = input("¿Está de acuerdo con la información a exportar? Presione 1 para confirmar, 0 para regresar al menú principal")
            if exportar == "1":
                print("Exportando archivo")
                with open('ruta.txt', 'a') as archivo:
                    archivo.write("\n"+str(informacion))
                exit()
            elif exportar == "0":
                clear()
                printMenu(menu)
        def actualizarRedesWifi():
            fuenteDatos = open("Acceso_universal.csv","r")#abrir archivo lectura
            redesDatosGov=fuenteDatos.readlines()
            fuenteDatos.close()
            nonlocal redesMatriz
            for i in range(1,5):
                redesMatriz[i-1][0]=float((redesDatosGov[i][(redesDatosGov[i].index(',"')+2):(redesDatosGov[i].index('",'))]))
                redesMatriz[i-1][1]=float((redesDatosGov[i][(redesDatosGov[i].index('","')+3):(redesDatosGov[i].index('",2'))]))
                temp = (redesDatosGov[i].split(","))
                #print (temp)
                redesMatriz[i-1][2]= int(temp[16])
            print("\n")
            for i in redesMatriz:
                print(i)
            respuesta = input("Datos de coordenadas para zonas wifi actualizados, presione 0 para regresar al menú principal: ")
            if respuesta == "0":
                print("\n")
                printMenu(menu)
            else:
                print("Error")
                exit()
            
        #INICIO RETO 2
        printMenu(menu)
    #==========INICIO DEL PROGRAMA==========
    reto1()
    #reto2("51675")
except Exception:
    pass