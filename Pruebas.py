from AFD import AFD
from AFN import AFN
from AFN_Lambda import AFN_Lambda
from AFPD import AFPD
from queue import LifoQueue
from Alfabeto import Alfabeto
from MT import MT
import ast
import random

class ClasePrueba:
    def __init__(self):
        pass
    
    def probarAFD(self):
        # Crear autómatas AFD
        #afd1 = AFD(nombreArchivo='evenA.DFA')
        #afd1 = AFD(nombreArchivo='evenB.DFA')
        #afd1 = AFD(nombreArchivo='testAFD.DFA')
        afd1 = AFD(nombreArchivo='testAFD2.DFA')

        #afd1 = AFD(afd1.alfabeto,afd1.estados,afd1.estadoInicial,afd1.estadosAceptacion,afd1.delta)
        # Procesar cadenas con y sin detalles
    
        cadena = 'aba'
        resultado_sin_detalles = afd1.procesar_cadena(cadena)
        resultado_con_detalles = afd1.procesar_cadena_con_detalles(cadena)
  
        print(f"\n--Procesamiento sin detalles de la cadena '{cadena}': {resultado_sin_detalles}")
        print(f"\n--Procesamiento con detalles de la cadena '{cadena}': {resultado_con_detalles}")
        # Procesar listas de cadenas
        print("\n--Procesamiento de lista de cadenas\n")
        lista_cadenas = ['aba', 'abbaa', 'abbabaabbbbb']
        nombre_archivo = 'resultados_lista_de_cadenas.txt'
        imprimir_pantalla = True
        afd1.procesarListaCadenas(lista_cadenas, nombre_archivo, imprimir_pantalla)
        
        # Generar archivos
        nombre_archivo1 = 'resultado_con_detalles.txt'
        nombre_archivo2 = 'resultado_sin_detalles.txt'
        afd1.exportar(nombre_archivo1)
        afd1.exportar(nombre_archivo2)
        print("\n--AFD\n")
        print(afd1)
        print("\n--AFD Completitud\n")
        print(afd1.verificarCorregirCompletitud())
        print("\n--AFD Imprimir simplificado\n")
        print(afd1.imprimirAFDSimplificado())
        print("\n--AFD Simplificado\n")
        print(afd1.simplificarAFD())
        
        
   

    def ProbarAFN(self):

        afn1 = AFN(nombreArchivo='AFNTest.txt')
        alfabeto = Alfabeto(afn1.alfabeto)
        cadena = 'bbac'
        procesar_cadena_con_detalle = afn1.procesar_cadena_con_detalles(cadena) 
        print(f"\nProcesamiento  de la cadena '{cadena}' con detalle \n")
        print(procesar_cadena_con_detalle)
        print("\nProcesamiento un proesamiento de aceptacion \n")
        procesar_cadena_detalle = afn1.procesar_cadena_con_detalles(cadena)
        
        print("\nProcesamiento  posible de la cadena \n")
        procesamientos_posibles = afn1.computarTodosLosProcesamientos(cadena)

    
        print(f"\nProcesamiento  de lista de cadenas \n")
        lista_cadenas = [alfabeto.generar_cadena_aleatoria(3), alfabeto.generar_cadena_aleatoria(5), alfabeto.generar_cadena_aleatoria(10)]
        nombre_archivo = 'resultados_lista_de_cadenas.txt'
        imprimir_pantalla = True
        afn1.procesarListaCadenas(lista_cadenas, nombre_archivo, imprimir_pantalla)
        nombre_archivo1 = 'resultado_con_detalles.txt'
        nombre_archivo2 = 'procesamientos_posibles.txt'
        afn1.exportar(nombre_archivo1)
        afn1.exportar(nombre_archivo2)
        print("\n--AFN estados inaccesibles\n")
        afn1.estadosInaccesibles

    def simplificacionAFN(self):
        afn1 = AFN(nombreArchivo='AFNTest.txt')
        print("\n--AFN Simplificado\n")
        afn1.imprimirAFNSimplificado()

    def probarAFNtoAFD(self):
         
         #afd1 = AFD(nombreArchivo='evenA.DFA')
         #afn1 = AFN(nombreArchivo='testAFN.NFA')  
         #afn1 = AFN(nombreArchivo='conversionAFNtoAFDTest.txt')
         print("--AFN\n")
         afn1 = AFN(nombreArchivo='AFNTest - copia.txt') 
         cadena = 'dba'  
         #procesar_cadena_afd1 = afd1.procesar_cadena(cadena)
         print(f"AFN procesando cadena {cadena} \n")
         procesar_cadena_afn1 = afn1.procesarCadena(cadena)
         print(procesar_cadena_afn1)
         print("\n--AFN a AFD\n")
         afn_afd = afn1.AFNtoAFD()
         print(afn_afd)
         print("\n--Nuevo AFD procesando cadena con detalle\n")
         afd_nuevo_procesamiento = afn_afd.procesar_cadena_con_detalles(cadena)
         print(f"\n--Procesamiento  de la cadena '{cadena}':\n Procesamiento AFN {procesar_cadena_afn1} \n Procesamiento nuevo AFD con detalle: {afd_nuevo_procesamiento} ")        
         print("\n--Procesamiento de lista de cadenas del nuevo AFD\n")
         lista_cadenas = ['aba', 'abbaa', 'abbabaabbbbb']
         nombre_archivo = 'resultados_lista_de_cadenas.txt'
         imprimir_pantalla = True
         afn_afd.procesarListaCadenas(lista_cadenas, nombre_archivo, imprimir_pantalla)


    def probarComplemento(self):
        afd1 = AFD(nombreArchivo='evenA.DFA')
        afd_complemento = afd1.hallarComplemento()
        print(f"AFD original '{afd1}'\n")
        print(f"\n\nAFD Complemento \n'{afd_complemento}'")

    def probarProductoCartesiano(self):
        # Crear los AFD a partir de los archivos
        afd1 = AFD(nombreArchivo='evenA.DFA')
        afd2 = AFD(nombreArchivo='evenB.DFA')

        # Producto cartesiano con intersección (∩)
        interseccion = afd1.hallarProductoCartesiano(afd1, afd2, 'interseccion')
        print("\n\nProducto Cartesiano con Interseccion:")
        print(interseccion)

        # Producto cartesiano con unión (∪)
        union = afd1.hallarProductoCartesiano(afd1, afd2, 'union')
        print("\n\nProducto Cartesiano con Union:")
        print(union)

        # # Producto cartesiano con diferencia (-)
        diferencia = afd1.hallarProductoCartesiano(afd1, afd2, 'diferencia')
        print("\n\nProducto Cartesiano con Diferencia Simetrica:")
        print(diferencia)

        # Dibujar el AFD resultante del producto cartesiano con intersección (∩)
        print("\n\nDiagrama del Producto Cartesiano de la Diferencia simetrica con la Interseccion:")
        producto_cartesiano = afd1.hallarProductoCartesiano(interseccion, diferencia, 'interseccion')
        print(producto_cartesiano)

    def probarSimplificacion(self):
        afd4 = AFD(nombreArchivo='minTest.DFA')
        print(f"\nAFD original \n")
        print(afd4)
        afd4.simplificarAFD()
        print(f"\nSimplificacion\n")
        print(afd4)
    def generar_cadenas_afn(self,afns):
        #Me gustaría que se generaran cadenas dependiendo del lenguaje de los afns (no todos tienen de lenguaje {a,b}) para poder hacer más pruebas
        cadenas_generadas = []
        for afn in afns:
            for _ in range(1000):
                tamano = random.randint(1, 10)  # Choose the size randomly
                cadena = ''.join(random.choices(['a', 'b'], k=tamano))  # Generate a random string
                print(cadena)
                cadenas_generadas.append(cadena)
        return cadenas_generadas
    
    def validarAFNtoAFD(self):
         afn1 = AFN(nombreArchivo='testAFN.NFA') 
         afd2 = AFD(nombreArchivo='evenA.DFA')
         afn3 = AFN(nombreArchivo='testAFN.NFA')  
         afn4 = AFN(nombreArchivo='conversionAFNtoAFDTest.txt')
         afn5 = AFN(nombreArchivo='AFNTest - copia.txt') 
         afns =[afn1,afd2,afn3,afn4,afn5]
         lista_cadenas = clase_prueba.generar_cadenas_afn(afns)
         imprimir_pantalla = True
         print("Procesamiento AFN")
         contador_si_afn, contador_no_afn = afn1.procesarListaCadenas(lista_cadenas, 'resultados_AFN_cedenas_aleatorias.txt', imprimir_pantalla)
         print("AFN a AFD")
         afn_afd = afn1.AFNtoAFD()
         contador_si_afd, contador_no_afd = afn_afd.procesarListaCadenas(lista_cadenas, 'resultados_AFNtoAFD_cedenas_aleatorias.txt', imprimir_pantalla)
         print("Cantidad de cadenas aceptadas AFN :\n", contador_si_afn)
         print("Cantidad de cadenas rechazadas AFN:\n", contador_no_afn)
         print("Cantidad de cadenas aceptadas nuevo AFD :\n", contador_si_afd)
         print("Cantidad de cadenas rechazadas nuevo AFD:\n", contador_no_afd)

    def probarAFNLambda(self):
    # Crear autómatas AFN-λ
        #firstAFNL = AFN_Lambda(nombreArchivo="firstAFNLtest.NFE")
        secondAFNL = AFN_Lambda(nombreArchivo="secondAFNLtest.NFE")
        lambdaClosureAFNL = AFN_Lambda(nombreArchivo="lambdaClausuraTest.NFE")
        #toStringTestAFNL = AFN_Lambda(nombreArchivo="toStringTestAFNL")

        # Calcular la λ-clausura de un estado
        lambdaClosureState = lambdaClosureAFNL.calcularLambdaClausura(states=['s0'])
        print("Lambda clausura de 's0':", lambdaClosureState)

        # Calcular la λλ-clausura de un conjunto de estados
        lambdaClosureStates = lambdaClosureAFNL.calcularLambdaClausura(states=["s0", "s3"])
        print("Lambda clausura de ['s0', 's3']:", lambdaClosureStates)
        
        # Procesar cadenas mostrando solo un procesamiento de aceptación
        print("Procesamiento de '01112012' en secondAFNL:")
        result = secondAFNL.procesarCadena("01112012", True)
        print("Aceptada:", result)

        # Procesar cadenas mostrando todos los procesamientos posibles
        print("Procesar cadenas mostrando todos los procesamientos posibles en AFN-λ")
        result = secondAFNL.procesarCadenaConDetalles("102")
        print("Aceptada:", result)

        # # Consultar los procesamientos de aceptación, abortados y de rechazo
        print("Consultar los procesamientos de aceptación, abortados y de rechazo AFN-λ")
        result = secondAFNL.procesarCadena("2")
        print("Aceptada:", result)

        # # Procesar listas de cadenas
        # cadenas = ["0111012", "2", "11"]
        # for cadena in cadenas:
        #     print("Procesamiento de", cadena, "en secondAFNL:")
        #     result = secondAFNL.procesarCadena(cadena, True)
        #     print("Aceptada:", result)

        # # Generar archivos
        # with open("toStringTestAFNL.NFE", "w") as file:
        #     file.write(toStringTestAFNL.__str__())

    def probarAFPD(self):
        afpd1 = AFPD(nombreArchivo='AFPD_Test.txt')
        alfabeto = Alfabeto(afpd1.alfabetoCinta)
        cadena = alfabeto.generar_cadena_aleatoria(5)
        print("Procesamiento con detalle\n")
        afpd1.procesarCadenaConDetalles(cadena)
        print("Procesamiento de lista de cadenas\n")
        afpd1.procesarListaCadenas([alfabeto.generar_cadena_aleatoria(7),alfabeto.generar_cadena_aleatoria(2),alfabeto.generar_cadena_aleatoria(3)], "ResultadosAFPD.txt", True)
    
    def probarAFPDProductoCartesianoAFD(self):
        afd1 = AFD(nombreArchivo='AFDParAParB.txt')
        afpd2 = AFPD(nombreArchivo='AFPD_Test.txt')
        
        #print(afd1.alfabeto,afpd2.alfabetoCinta)
        #print(afpd2.delta)
        afd_resultado = afpd2.hallarProductoCartesiano(afd1, afpd2, 'Y')
        print(afd_resultado)
    def probarMT(self):
        #prueba usando TM de palindromes pares

        Turing = MT(nombreArchivo="MT.tm")  
        print(Turing.procesarCadenaConDetalles("ababa"))
        print(Turing.procesarCadena("ababa"))
        print(Turing.procesarFuncion("aabbaa"))
        Turing.procesarListaCadenas(["aaaa", "aabbaa", "ababa"], "resultadosTM.txt", True)
        print(Turing)
        
# Llamar a la función para probar el producto cartesiano

# Crear instancia de la clase ClasePrueba y ejecutar los método correspondiente
clase_prueba = ClasePrueba()
#-------------AFD-----------------
#clase_prueba.probarAFD()
#clase_prueba.probarComplemento()
#clase_prueba.probarSimplificacion()
#clase_prueba.probarProductoCartesiano()
#-------------AFN-----------------
#clase_prueba.ProbarAFN()
#clase_prueba.simplificacionAFN()
#clase_prueba.probarAFNtoAFD()
#clase_prueba.validarAFNtoAFD() #validacion con mas de 5000 cadenas
<<<<<<< Updated upstream
#------------AFNL--------------

=======
<<<<<<< HEAD
#------------
#clase_prueba.probarProductoCartesiano()
#clase_prueba.probarSimplificacion()
=======
#------------AFNL--------------

>>>>>>> d9d067194e04a1ff05b2f68403d06e6c8d123088
>>>>>>> Stashed changes

#clase_prueba.probarAFNLambda()
#-------------AFPD-----------------
#clase_prueba.probarAFPD()
<<<<<<< Updated upstream
clase_prueba.probarAFPDProductoCartesianoAFD()
=======
<<<<<<< HEAD
#clase_prueba.probarAFPDProductoCartesianoAFD()
#--------------MT------------------
clase_prueba.probarMT()
=======
clase_prueba.probarAFPDProductoCartesianoAFD()
>>>>>>> d9d067194e04a1ff05b2f68403d06e6c8d123088
>>>>>>> Stashed changes
