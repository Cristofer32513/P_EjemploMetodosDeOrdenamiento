'''
Created on 14/11/2018

@author: casas
'''
import timeit
import random
from pip._vendor.distlib.compat import raw_input
class MetodosDeOrdenamiento:
       
    def mostrarVector(self, datos):
        cont=1;
        for i in range(0, len(datos)):
            if(cont==15):
                print("  "+datos[i]+",    ")
                cont=0
            else:
                print("  "+datos[i]+",    ")
                cont+=1;
    
    def mostrarDatosDeEficiencia(self, contadorComparaciones, contadorIntercambios,
                                 contadorRecorridos, tiempoTotal):
        print("       DATOS DE EFICIENCIA DEL ALGORITMO");
        print();
        print("    - Cantidad  de  recorridos  realizados:    "+str(contadorRecorridos))
        print("    - Cantidad de comparaciones realizadas:    "+str(contadorComparaciones))
        print("    - Cantidad  de intercambios realizados:    "+str(contadorIntercambios))
        print("    - Tiempo     total     de    ejecucion:    "+str(tiempoTotal)+" segundos")
        print("    - Tiempo     total     de    ejecucion:    "+str(tiempoTotal*1000)+" milisegundos")
    
    def ordenamientoBurbuja0(self, datos):
        contadorComparaciones=0
        contadorIntercambios=0
        contadorRecorridos=0        
        aux=0
        for i in range(0, len(datos)):
            for j in range(i+1, len(datos)):
                contadorComparaciones+=1
                if(datos[i]>datos[(j)]):
                    contadorIntercambios+=1
                    aux=datos[i]
                    datos[i]=datos[j]
                    datos[j]=aux
                
            
            contadorRecorridos+=1
        tiempoTotal=timeit.timeit()
        self.mostrarVector(datos)
        print()
        print()
        self.mostrarDatosDeEficiencia(contadorComparaciones, contadorIntercambios, contadorRecorridos, tiempoTotal);
    
    def ordenamientoBurbuja1(self, datos):
        contadorComparaciones=0
        contadorIntercambios=0
        contadorRecorridos=0
        
        aux=0;
        for i in range(2, (len(datos)+1)):
            for j in range(0, (len(datos)+1)-i):
                contadorComparaciones+=1
                if(datos[j]>datos[j+1]):
                    contadorIntercambios+=1
                    aux=datos[j]
                    datos[j]=datos[j+1]
                    datos[j+1]=aux
            contadorRecorridos+=1
        tiempoTotal=timeit.timeit()
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
        tiempoTotal=timeit.timeit()
        self.mostrarVector(datos)
        print()
        print()
        self.mostrarDatosDeEficiencia(contadorComparaciones, contadorIntercambios, contadorRecorridos, tiempoTotal)
    
    def ordenamientoPorSeleccion(self, datos):
        contadorComparaciones=0
        contadorIntercambios=0
        contadorRecorridos=0
        
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
        tiempoTotal=timeit.timeit()
        self.mostrarVector(datos)
        print()
        print()
        self.mostrarDatosDeEficiencia(contadorComparaciones, contadorIntercambios, contadorRecorridos, tiempoTotal)
    
    def ordenamientoPorInsercion(self, datos):
        contadorComparaciones=0
        contadorIntercambios=0
        contadorRecorridos=0
        
        for i in range(1, len(datos)):
            valor=datos[i]
            j=i-1
            while(j>=0):
                contadorComparaciones+=1;
                if(valor<datos[j]):
                    contadorIntercambios+=1
                    datos[j+1]=datos[j]
                    datos[i]=valor
                    j-=1
                else:
                    break
            contadorRecorridos+=1
        tiempoTotal=timeit.timeit();
        self.mostrarVector(datos)
        print()
        print()
        self.mostrarDatosDeEficiencia(contadorComparaciones, contadorIntercambios, contadorRecorridos, tiempoTotal)
    
    def ordenamientoPorInsercion2(self, datos):
        contadorComparaciones=0
        contadorIntercambios=0
        contadorRecorridos=0
        
        i=0
        j=0
        aux=0
        
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
        tiempoTotal=timeit.timeit()
        self.mostrarVector(datos)
        print()
        print()
        self.mostrarDatosDeEficiencia(contadorComparaciones, contadorIntercambios, contadorRecorridos, tiempoTotal)

    
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
    opcion=raw_input("Elija una opcion...")
    print()
    print()
    
    if(int(opcion)>=1 and int(opcion) <=5):
        if(int(opcion)==1):
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
                    opcionBurbuja=raw_input("    Elija una opcion...\n    ")
                    print()
                
                    if(opcionBurbuja>=1 and opcionBurbuja <=4):                
                        if(opcionBurbuja==1):
                            print("  ======================================================VECTOR ORIGINAL======================================================\n")
                            metodos.mostrarVector(datos)
                            print("\n\n")
                            print("  ===================================================ORDENAMIENTO BURBUJA 0==================================================\n")
                            metodos.ordenamientoBurbuja0(datos.clone())
                        if(opcionBurbuja==2):
                            print("  ======================================================VECTOR ORIGINAL======================================================\n")
                            metodos.mostrarVector(datos)
                            print("\n\n")
                            print("  ===================================================ORDENAMIENTO BURBUJA 1==================================================\n")
                            metodos.ordenamientoBurbuja1(datos.clone())
                        if(opcionBurbuja==3):
                            print("  ======================================================VECTOR ORIGINAL======================================================\n")
                            metodos.mostrarVector(datos)
                            print("\n\n")
                            print("  ===================================================ORDENAMIENTO BURBUJA 2==================================================\n")
                            metodos.ordenamientoBurbuja2(datos.clone())
                        if(opcionBurbuja==4):
                            print("  ======================================================VECTOR ORIGINAL======================================================\n")
                            metodos.mostrarVector(datos)
                            print("\n\n")
                            print("  ===================================================ORDENAMIENTO BURBUJA 3==================================================\n")
                            metodos.ordenamientoBurbuja3(datos.clone())
                        repetirMenuMetodoburbuja=False
                    else:
                        print("    *"+opcionBurbuja+" no es una opcion valida, intenta otra vez.")
                    print()
                    print()
            else:
                print("  *No se ha elegido un tamanio para el vector.")
            print()
            print()
        if(int(opcion)==2):
            if(len(datos)>0):
                print("  ======================================================VECTOR ORIGINAL======================================================\n")
                metodos.mostrarVector(datos)
                print("\n\n")
                print("  =================================================ORDENAMIENTO POR SELECCION================================================\n")
                metodos.ordenamientoPorSeleccion(datos.clone())
            else:
                print("  *No se ha elegido un tamanio para el vector.")
            print()
            print()
        if(int(opcion)==3):
            if(len(datos)>0):
                print("  ======================================================VECTOR ORIGINAL======================================================\n")
                metodos.mostrarVector(datos)
                print("\n\n")
                print("  =================================================ORDENAMIENTO POR INSERCION================================================\n")
                metodos.ordenamientoPorInsercion(datos.clone())
            else:
                print("  *No se ha elegido un tamanio para el vector.")
            print()
            print()
        if(int(opcion)==4):
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
                opcionVector=raw_input("  Elija una opcion...\n  ")
                print()
            
                if(opcionVector>=1 and opcionVector <=4):                
                    if(opcion==1):
                        datos=[]
                        print("  Creando vector...")
                        for i in range(0,len(datos)):
                            datos.insert(i, random.randint(1,101))
                    if(opcion==2):
                        datos=[]
                        print("  Creando vector...")
                        for i in range(0,len(datos)):
                            datos.insert(i, random.randint(1,101))
                    if(opcion==3):
                        datos=[];
                        print("  Creando vector...")
                        for i in range(0,len(datos)):
                            datos.insert(i, random.randint(1,101))
                    if(opcion==4):
                        datos=[];
                        print("  Creando vector...");
                        for i in range(0,len(datos)):
                            datos.insert(i, random.randint(1,101))
                    repetirMenuTamanioVector=False
                    print()
                    print("  El vector ha sido creado y llenado.")
                    print()
                    print("  *NOTA: El vector a utilizar en los metodos sera el mismo mientras que no se escoja un tamanio diferente.")
                else:
                    print("    *"+opcion+" no es una opcion valida, intenta otra vez.")
                print()
                print()
        if(int(opcion)==5):
            repetirMenuPrincipal=False
        print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print()
        print()
    else:
        print("  *"+opcion+" no es una opcion valida, intenta otra vez.")
        print()
        print()
print("Usted ha salido.")