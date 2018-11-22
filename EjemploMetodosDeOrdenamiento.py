'''
Created on 14/11/2018

@author: casas
'''
import random
from time import time

class MetodosDeOrdenamiento:
    
    '''
    PYTHON NO TIENE LA MISMA LOGICA
    PARA PODER DARLE EL MISMO FORMATO
    QUE EN JAVA
    '''   
    def mostrarVector(self, datos):
        cont=1
        for i in range(0, len(datos)):
            if(int(cont)==15):
                print("  "+str(datos[i])+",    ")
                cont=1
            else:
                print("  "+str(datos[i])+",    ", end="")
                cont+=1
    
    def mostrarDatosDeEficiencia(self, contadorComparaciones, contadorIntercambios,
                                 contadorRecorridos, tiempoTotal):
        print("       DATOS DE EFICIENCIA DEL ALGORITMO")
        print()
        print("    - Cantidad  de  recorridos  realizados:    "+str(contadorRecorridos))
        print("    - Cantidad de comparaciones realizadas:    "+str(contadorComparaciones))
        print("    - Cantidad  de intercambios realizados:    "+str(contadorIntercambios))
        print("    - Tiempo     total     de    ejecucion:    "+str(tiempoTotal)+" segundos")
        print("    - Tiempo     total     de    ejecucion:    "+str(tiempoTotal*1000)+" milisegundos")
    
    '''=======METODO DE ORDENAMIENTO BURBUJA======='''
    def ordenamientoBurbuja0(self, datos):
        contadorComparaciones=0
        contadorIntercambios=0
        contadorRecorridos=0        
        aux=0
        inicio=time()
        for i in range(0, len(datos)):
            for j in range(i+1, len(datos)):
                contadorComparaciones+=1
                if(datos[i]>datos[(j)]):
                    contadorIntercambios+=1
                    aux=datos[i]
                    datos[i]=datos[j]
                    datos[j]=aux
            contadorRecorridos+=1
        tiempoTotal=time()-inicio
        self.mostrarVector(datos)
        print()
        print()
        self.mostrarDatosDeEficiencia(contadorComparaciones, contadorIntercambios, contadorRecorridos, tiempoTotal)
    
    def ordenamientoBurbuja1(self, datos):
        contadorComparaciones=0
        contadorIntercambios=0
        contadorRecorridos=0
        aux=0
        
        inicio=time()
        for i in range(2, (len(datos)+1)):
            for j in range(0, (len(datos)+1)-i):
                contadorComparaciones+=1
                if(datos[j]>datos[j+1]):
                    contadorIntercambios+=1
                    aux=datos[j]
                    datos[j]=datos[j+1]
                    datos[j+1]=aux
            contadorRecorridos+=1
        tiempoTotal=time()-inicio
        self.mostrarVector(datos)
        print()
        print()
        self.mostrarDatosDeEficiencia(contadorComparaciones, contadorIntercambios, contadorRecorridos, tiempoTotal)
        
    def ordenamientoBurbuja2(self, datos):
        contadorComparaciones=0
        contadorIntercambios=0
        contadorRecorridos=0
        i=1
        ordenado=False
        aux=0
        
        inicio=time()
        while(i<len(datos) and not ordenado):
            i+=1
            ordenado=True
            for j in range(0, (len(datos)+1)-i):
                contadorComparaciones+=1
                if(datos[j]>datos[j+1]):
                    contadorIntercambios+=1
                    ordenado=False
                    aux=datos[j]
                    datos[j]=datos[j+1]
                    datos[j+1]=aux
            contadorRecorridos+=1
        tiempoTotal=time()-inicio
        self.mostrarVector(datos)
        print()
        print()
        self.mostrarDatosDeEficiencia(contadorComparaciones, contadorIntercambios, contadorRecorridos, tiempoTotal)
    
    def ordenamientoBurbuja3(self, datos):
        contadorComparaciones=0
        contadorIntercambios=0
        contadorRecorridos=0
        i=1
        ordenado=False
        aux=0
        
        inicio=time()
        while(i<len(datos) or not ordenado):
            i+=1
            ordenado=True
            for j in range(0, (len(datos)+1)-i):
                contadorComparaciones+=1
                if(datos[j]>datos[j+1]):
                    contadorIntercambios+=1
                    ordenado=False
                    aux=datos[j]
                    datos[j]=datos[j+1]
                    datos[j+1]=aux
            contadorRecorridos+=1
        tiempoTotal=time()-inicio
        self.mostrarVector(datos)
        print()
        print()
        self.mostrarDatosDeEficiencia(contadorComparaciones, contadorIntercambios, contadorRecorridos, tiempoTotal)
    
    '''=======METODO DE ORDENAMIENTO POR SELECCION======='''
    def ordenamientoPorSeleccion(self, datos):
        contadorComparaciones=0
        contadorIntercambios=0
        contadorRecorridos=0
        
        inicio=time()
        for i in range(0, len(datos)):
            menor=i
            for j in range(i+1, len(datos)):
                contadorComparaciones+=1
                if(datos[j]<datos[menor]):
                    menor=j
            aux=datos[i]
            datos[i]=datos[menor]
            datos[menor]=aux
            contadorIntercambios+=1
            contadorRecorridos+=1
            contadorIntercambios+=1
        tiempoTotal=time()-inicio
        self.mostrarVector(datos)
        print()
        print()
        self.mostrarDatosDeEficiencia(contadorComparaciones, contadorIntercambios, contadorRecorridos, tiempoTotal)
    
    '''=======METODO DE ORDENAMIENTO POR INSERCION======='''
    '''
    ESTE ES EL QUE PRESENTO PRITS EN PYTHON,
    ES UN POCO MAS TARDADO PERO REALIZA MENOS
    INTERCAMBIOS
    '''
    def ordenamientoPorInsercion(self, datos):
        contadorComparaciones=0
        contadorIntercambios=0
        contadorRecorridos=0
        
        inicio=time()
        for i in range(1, len(datos)):
            valor=datos[i]
            j=i-1
            while(j>=0):
                contadorComparaciones+=1
                if(valor<datos[j]):
                    contadorIntercambios+=1
                    datos[j+1]=datos[j]
                    datos[j]=valor
                    j-=1
                else:
                    break
            contadorRecorridos+=1
        tiempoTotal=time()-inicio
        self.mostrarVector(datos)
        print()
        print()
        self.mostrarDatosDeEficiencia(contadorComparaciones, contadorIntercambios, contadorRecorridos, tiempoTotal)
    
    '''
    ESTE ES EL QUE PRESENTO PRITS EN JAVA ADAPTADO
    A PYTHON, ES MENOS TARDADO PERO REALIZA MAS
    INTERCAMBIOS
    '''
    def ordenamientoPorInsercion2(self, datos):
        contadorComparaciones=0
        contadorIntercambios=0
        contadorRecorridos=0
        i=0
        j=0
        aux=0
        
        inicio=time()
        for i in range(1, len(datos)):
            aux=datos[i]
            j=i-1
            contadorComparaciones+=1
            while(j>=0 and aux<datos[j]):
                contadorIntercambios+=1
                datos[j+1]=datos[j]
                j-=1
            datos[j+1]=aux
            contadorRecorridos+=1
        tiempoTotal=time()-inicio
        self.mostrarVector(datos)
        print()
        print()
        self.mostrarDatosDeEficiencia(contadorComparaciones, contadorIntercambios, contadorRecorridos, tiempoTotal) 
    
    '''========METODO DE ORDENAMIENTO SELLSORT========='''
    '''def ordenamientoSellSort(self, datos):
        contadorComparaciones=0
        contadorIntercambios=0
        contadorRecorridos=0
        salto=0
        aux=0
        i=0
        cambios=True
        
        inicio=time()
        for salto=(len(datos)/2) in range(salto>0);salto/=2){
            cambios=True
            while(cambios)
                cambios=False
                contadorRecorridos+=1
                for i=salto in range(0, len(datos))
                    contadorComparaciones+=1
                    if(datos[i-salto]>datos[i]):
                        contadorIntercambios+=1
                        aux=datos[i]
                        datos[i]=datos[i-salto]
                        datos[i-salto]=aux
                        cambios=True
        tiempoTotal=time()-inicio
        System.out.println();
        System.out.println();
        mostrarDatosDeEficiencia(contadorComparaciones, contadorIntercambios, contadorRecorridos, tiempoTotal);
    }'''
        
    def ordenamientoQuickSort(self, lista):
        izquierda=[]
        centro=[]
        derecha=[]
        if(len(lista)>1):
            pivote=lista[0]
            for i in lista:
                if(i<pivote):
                    izquierda.append(i)
                elif (i==pivote):
                    centro.append(i);
                elif (i>pivote):
                    derecha.append(i);
            return self.ordenamientoQuickSort(izquierda)+centro+self.ordenamientoQuickSort(derecha)
        else:
            return lista
    
metodos=MetodosDeOrdenamiento()
                       
repetirMenuPrincipal=True
opcion=0
datos=[]

while(repetirMenuPrincipal):
    print("1 = Metodo de ordenamiento burbuja.")
    print("2 = Metodo de ordenamiento por seleccion.")
    print("3 = Metodo de ordenamiento por insercion.")
    print("4 = Elegir tamanio del vector a utilizar.")
    print("5 = Salir")
    print("-----------------------------------------")
    opcion=int(input('Elija una opcion...'))
    print()
    print()
    
    if(opcion>=1 and opcion <=5):
        if(opcion==1):
            if(len(datos)>0):
                repetirMenuMetodoburbuja=True
                opcionBurbuja=0     
                
                while(repetirMenuMetodoburbuja):
                    print("  Utilizar metodo...")
                    print()
                    print("    1 = Burbuja 0.")
                    print("    2 = Burbuja 1.")
                    print("    3 = Burbuja 2.")
                    print("    4 = Burbuja 3.")
                    print("    -----------------------------------------")
                    opcionBurbuja=int(input("    Elija una opcion...\n    "))
                    print()
                
                    if(opcionBurbuja>=1 and opcionBurbuja <=4):                
                        if(opcionBurbuja==1):
                            print("  ======================================================VECTOR ORIGINAL======================================================\n")
                            metodos.mostrarVector(datos)
                            print("\n\n")
                            print("  ===================================================ORDENAMIENTO BURBUJA 0==================================================\n")
                            metodos.ordenamientoBurbuja0(datos.copy())
                        if(opcionBurbuja==2):
                            print("  ======================================================VECTOR ORIGINAL======================================================\n")
                            metodos.mostrarVector(datos)
                            print("\n\n")
                            print("  ===================================================ORDENAMIENTO BURBUJA 1==================================================\n")
                            metodos.ordenamientoBurbuja1(datos.copy())
                        if(opcionBurbuja==3):
                            print("  ======================================================VECTOR ORIGINAL======================================================\n")
                            metodos.mostrarVector(datos)
                            print("\n\n")
                            print("  ===================================================ORDENAMIENTO BURBUJA 2==================================================\n")
                            metodos.ordenamientoBurbuja2(datos.copy())
                        if(opcionBurbuja==4):
                            print("  ======================================================VECTOR ORIGINAL======================================================\n")
                            metodos.mostrarVector(datos)
                            print("\n\n")
                            print("  ===================================================ORDENAMIENTO BURBUJA 3==================================================\n")
                            metodos.ordenamientoBurbuja3(datos.copy())
                        repetirMenuMetodoburbuja=False
                    else:
                        print("    *"+str(opcionBurbuja)+" no es una opcion valida, intenta otra vez.")
                    print()
                    print()
            else:
                print("  *No se ha elegido un tamanio para el vector.")
            print()
            print()
        if(opcion==2):
            if(len(datos)>0):
                print("  ======================================================VECTOR ORIGINAL======================================================\n")
                metodos.mostrarVector(datos)
                print("\n\n")
                print("  =================================================ORDENAMIENTO POR SELECCION================================================\n")
                metodos.ordenamientoPorSeleccion(datos.copy())
            else:
                print("  *No se ha elegido un tamanio para el vector.")
            print()
            print()
        if(opcion==3):
            if(len(datos)>0):
                print("  ======================================================VECTOR ORIGINAL======================================================\n")
                metodos.mostrarVector(datos)
                print("\n\n")
                print("  =================================================ORDENAMIENTO POR INSERCION================================================\n")
                metodos.ordenamientoPorInsercion(datos.copy())
            else:
                print("  *No se ha elegido un tamanio para el vector.")
            print()
            print()
        if(opcion==4):
            repetirMenuTamanioVector=True
            opcionVector=0
            
            while(repetirMenuTamanioVector):
                print("Realizar pruebas con...")
                print()
                print("  1 = 1,000 datos.")
                print("  2 = 10,000 datos.")
                print("  3 = 100,000 datos.")
                print("  4 = 1,000,000 datos.")
                print("  -----------------------------------------")
                opcionVector=int(input("  Elija una opcion...\n  "))
                print()
            
                if(opcionVector>=1 and opcionVector <=4):                
                    if(opcionVector==1):
                        datos=[]
                        print("  Creando vector...")
                        for i in range(0,1000):
                            datos.insert(i, random.randint(1,100))
                    if(opcionVector==2):
                        datos=[]
                        print("  Creando vector...")
                        for i in range(0,10000):
                            datos.insert(i, random.randint(1,100))
                    if(opcionVector==3):
                        datos=[]
                        print("  Creando vector...")
                        for i in range(0,100000):
                            datos.insert(i, random.randint(1,100))
                    if(opcionVector==4):
                        datos=[]
                        print("  Creando vector...")
                        for i in range(0,1000000):
                            datos.insert(i, random.randint(1,100))
                    repetirMenuTamanioVector=False
                    print()
                    print("  El vector ha sido creado y llenado.")
                    print()
                    print("  *NOTA: El vector a utilizar en los metodos sera el mismo mientras que no se escoja un tamanio diferente.")
                else:
                    print("    *"+str(opcion)+" no es una opcion valida, intenta otra vez.")
                print()
                print()
        if(opcion==5):
            repetirMenuPrincipal=False
    else:
        print("  *"+str(opcion)+" no es una opcion valida, intenta otra vez.")
        print()
        print()
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print()
    print()
print("Usted ha salido.")