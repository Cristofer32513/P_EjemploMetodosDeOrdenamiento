'''
Created on 14/11/2018

@author: casas
'''
import random
from time import time
from math import log
from builtins import sorted
from tkinter.constants import END

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
    def ordenamientoShellSort(self, datos): 
        contadorComparaciones=0
        contadorIntercambios=0
        contadorRecorridos=0
        
        n=len(datos)
        gap=n//2
        inicio = time()
        while gap > 0:
            for i in range(gap,n):
                temp = datos[i]
                j = i 
                contadorComparaciones+=1
                while  j >= gap and datos[j-gap] >temp:
                    datos[j] = datos[j-gap] 
                    j -= gap
                    contadorIntercambios+=1
                datos[j] = temp 
                contadorRecorridos=1
            gap //= 2
        
        tiempoTotal=time()-inicio
        self.mostrarVector(datos)
        print()
        print()
        self.mostrarDatosDeEficiencia(contadorComparaciones, contadorIntercambios, contadorRecorridos, tiempoTotal) 
    
    
    '''========METODO DE ORDENAMIENTO QUICKSORT=========''' 
    def partition(self, datos, low, high):
        i = ( low-1 )
        pivot = datos[high]
 
        for j in range(low , high):
            if   datos[j] <= pivot:
                i = i+1
                datos[i],datos[j] = datos[j],datos[i]
 
        datos[i+1],datos[high] = datos[high],datos[i+1]
        return ( i+1 )

    def ordenamientoQuickSort(self, arr, low, high):
        if low < high:
            pi = self.partition(arr, low, high)
            self.ordenamientoQuickSort(arr, low, pi-1)
            self.ordenamientoQuickSort(arr, pi+1, high)
            
            
    '''========METODO DE ORDENAMIENTO RADIXSORT========='''      
    def getDigit(self, num, base, digit_num):
        return (num // base ** digit_num) % base  
 
    def makeBlanks(self, size):
        return [ [] for i in range(size) ]  
 
    def split(self, a_list, base, digit_num):
        buckets = self.makeBlanks(base)
        for num in a_list:
            buckets[self.getDigit(num, base, digit_num)].append(num)  
        return buckets
 
    def merge(self, a_list):
        new_list = []
        for sublist in a_list:
            new_list.extend(sublist)
        return new_list
 
    def maxAbs(self, a_list):
        # largest abs value element of a list
        return max(abs(num) for num in a_list)
 
    def split_by_sign(self, a_list):
        # splits values by sign - negative values go to the first bucket,
        # non-negative ones into the second
        buckets = [[], []]
        for num in a_list:
            if num < 0:
                buckets[0].append(num)
            else:
                buckets[1].append(num)
        return buckets
     
    def radixSort(self, a_list, base):
        # there are as many passes as there are digits in the longest number
        passes = int(round(log(self.maxAbs(a_list), base)) + 1) 
        new_list = list(a_list)
        for digit_num in range(passes):
            new_list = self.merge(self.split(new_list, base, digit_num))
        return self.merge(self.split_by_sign(new_list))   
            

    '''========METODO DE ORDENAMIENTO POR INTERCALACION========='''
    def ordenamientoPorIntercalaion(self):
        contadorComparaciones=0
        contadorIntercambios=0
        contadorRecorridos=0
        
        ar3="ArchivoSalida.txt"
        ar1="Archivo1.txt"
        ar2="Archivo2.txt"
        archivo3=open (ar3, "w")
        archivo1=open(ar1, "r")
        archivo2=open(ar2, "r")
        repetir=True
        
        print("  ======================================================DATOS DEL ARCHIVO 1======================================================\n")
        self.mostrarArchivo(ar1)
        print("  ======================================================DATOS DEL ARCHIVO 2======================================================\n")
        self.mostrarArchivo(ar2)
        print()
        print()
        
        lineaArchivo1=archivo1.readline() 
        lineaArchivo2=archivo2.readline()
         
        inicio = time()
        contadorRecorridos+=1
        '''Se realizan comparaciones mientras la bandera no cambie'''
        while(repetir):
            contadorComparaciones+=1
            if(int(lineaArchivo1)<int(lineaArchivo2)):
                contadorIntercambios+=1
                archivo3.write(lineaArchivo1)
                lineaArchivo1=archivo1.readline()
                if(lineaArchivo1==""):
                    archivo3.write("\n")
                    archivo3.write(lineaArchivo2)
                    lineaArchivo2=archivo2.readline()
                    while(lineaArchivo2!=""):
                        archivo3.write(lineaArchivo2)
                        lineaArchivo2=archivo2.readline()
                    repetir=False
            elif(int(lineaArchivo1)>int(lineaArchivo2)):
                contadorIntercambios+=1
                archivo3.write(lineaArchivo2)
                lineaArchivo2=archivo2.readline()
                if(lineaArchivo2==""):
                    archivo3.write("\n")
                    archivo3.write(lineaArchivo1)
                    lineaArchivo1=archivo1.readline()
                    while(lineaArchivo1!=""):
                        archivo3.write(lineaArchivo1)
                        lineaArchivo1=archivo1.readline()
                    repetir=False
            else:
                archivo3.write(lineaArchivo1)
                archivo3.write(lineaArchivo2)
                lineaArchivo1=archivo1.readline()
                if(lineaArchivo1==""):
                    archivo3.write("\n")
                    archivo3.write(lineaArchivo2)
                    lineaArchivo2=archivo2.readline()
                    while(lineaArchivo2!=""):
                        archivo3.write(lineaArchivo2)
                        lineaArchivo2=archivo2.readline()
                    repetir=False
                lineaArchivo2=archivo2.readline()
                if(lineaArchivo2==""):
                    archivo3.write("\n")
                    archivo3.write(lineaArchivo1)
                    lineaArchivo1=archivo1.readline()
                    while(lineaArchivo1!=''):
                        archivo3.write(lineaArchivo1)
                        lineaArchivo1=archivo1.readline()
                    repetir=False
        archivo2.close
        archivo1.close
        #print("Archivos combinados y ordenados correctamente")
        archivo3.close
        tiempoTotal=time()-inicio
        print("  =================================================ORDENAMIENTO POR INTERCALACION================================================\n")
        self.mostrarArchivo(ar3)
        print()
        print()
        self.mostrarDatosDeEficiencia(contadorComparaciones, contadorIntercambios, contadorRecorridos, tiempoTotal) 
       
    def mostrarArchivo(self, ar):
        archivo=open(ar, "r")
        linea=archivo.readline()
        while(linea!=""):
            print(linea+", ", end="")
            linea=archivo.readline()
        print()
        print()
        
        
        
metodos=MetodosDeOrdenamiento()
                       
repetirMenuPrincipal=True
opcion=0
datos=[]

while(repetirMenuPrincipal):
    print("1 = Metodo de ordenamiento Burbuja.")
    print("2 = Metodo de ordenamiento Por Seleccion.")
    print("3 = Metodo de ordenamiento Por Insercion.")
    print("4 = Metodo de ordenamiento ShellSort.")
    print("5 = Metodo de ordenamiento QuickSort.")
    print("6 = Metodo de ordenamiento RadixSort.")
    print("7 = Elegir tamanio del vector a utilizar.")
    print("8 = Salir")
    print("-----------------------------------------")
    opcion=int(input('Elija una opcion...'))
    print()
    print()
    
    if(opcion>=1 and opcion <=8):
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
            if(len(datos)>0):
                print("  ======================================================VECTOR ORIGINAL======================================================\n")
                metodos.mostrarVector(datos)
                print("\n\n")
                print("  =================================================ORDENAMIENTO SHELLSORT================================================\n")
                metodos.ordenamientoShellSort(datos.copy())
            else:
                print("  *No se ha elegido un tamanio para el vector.")
            print()
            print()
        if(opcion==5):
            if(len(datos)>0):
                print("  ======================================================VECTOR ORIGINAL======================================================\n")
                metodos.mostrarVector(datos)
                print("\n\n")
                print("  =================================================ORDENAMIENTO QUICKSORT================================================\n")
                copiaDatos=datos.copy()
                inicio=time()
                metodos.ordenamientoQuickSort(copiaDatos, 0, len(copiaDatos)-1)
                tiempoTotal=time()-inicio
                metodos.mostrarVector(copiaDatos)
                print()
                print()
                metodos.mostrarDatosDeEficiencia(0, 0, 0, tiempoTotal)
            else:
                print("  *No se ha elegido un tamanio para el vector.")
            print()
            print()
        if(opcion==6):
            if(len(datos)>0):
                print("  ======================================================VECTOR ORIGINAL======================================================\n")
                metodos.mostrarVector(datos)
                print("\n\n")
                print("  =================================================ORDENAMIENTO RADIXSORT================================================\n")
                copiaDatos=datos.copy()
                inicio=time()
                sorted=metodos.radixSort(copiaDatos, 10)
                tiempoTotal=time()-inicio
                metodos.mostrarVector(sorted)
                #print(sorted)
                print()
                print()
                metodos.mostrarDatosDeEficiencia(0, 0, 0, tiempoTotal)
                
            else:
                print("  *No se ha elegido un tamanio para el vector.")
            print()
            print()
        if(opcion==7):
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
        if(opcion==8):
            repetirMenuPrincipal=False
    else:
        print("  *"+str(opcion)+" no es una opcion valida, intenta otra vez.")
        print()
        print()
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print()
    print()
print("Usted ha salido.")