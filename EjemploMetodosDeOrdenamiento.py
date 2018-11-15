'''
Created on 14/11/2018

@author: casas
'''
class MetodosDeOrdenamiento:
       
    def mostrarVector(self, datos):
        print(datos)
    
    def mostrarDatosDeEficiencia(self, contadorComparaciones, contadorIntercambios,
                                 contadorRecorridos, tiempoTotal):
        print("       DATOS DE EFICIENCIA DEL ALGORITMO");
        print();
        print("    - Cantidad de recorridos realizados: "+str(contadorRecorridos))
        print("    - Cantidad de comparaciones realizadas: "+str(contadorComparaciones))
        print("    - Cantidad de intercambios realizados: "+str(contadorIntercambios))
        print("    - Tiempo total de ejecucion: "+str(float(tiempoTotal)/1000000)+" milisegundos")
    
    def ordenamientoBurbuja0(self, datos):
        contadorComparaciones=0
        contadorIntercambios=0
        contadorRecorridos=0
        tiempoTotal=0
        tiempoInicial=0
        
        aux=0
        #tiempoInicial=System.nanoTime()
        for i in range(0, len(datos)):
            for j in range(i+1, len(datos)):
                contadorComparaciones+=1
                if(datos[i]>datos[(j)]):
                    contadorIntercambios+=1
                    aux=datos[i]
                    datos[i]=datos[j]
                    datos[j]=aux
                
            
            contadorRecorridos+=1
        #tiempoTotal=System.nanoTime()-tiempoInicial
        self.mostrarVector(datos)
        print()
        print()
        self.mostrarDatosDeEficiencia(contadorComparaciones, contadorIntercambios, contadorRecorridos, tiempoTotal);
    
    def ordenamientoBurbuja1(self, datos):
        contadorComparaciones=0
        contadorIntercambios=0
        contadorRecorridos=0
        tiempoTotal=0
        tiempoInicial=0
        
        aux=0;
        #tiempoInicial=System.nanoTime()
        for i in range(2, (len(datos)+1)):
            for j in range(0, (len(datos)+1)-i):
                contadorComparaciones+=1
                if(datos[j]>datos[j+1]):
                    contadorIntercambios+=1
                    aux=datos[j]
                    datos[j]=datos[j+1]
                    datos[j+1]=aux
            contadorRecorridos+=1
        #tiempoTotal=System.nanoTime()-tiempoInicial
        self.mostrarVector(datos)
        print()
        print()
        self.mostrarDatosDeEficiencia(contadorComparaciones, contadorIntercambios, contadorRecorridos, tiempoTotal)
        
    def ordenamientoBurbuja2(self, datos):
        contadorComparaciones=0
        contadorIntercambios=0
        contadorRecorridos=0
        tiempoTotal=0
        tiempoInicial=0
        i=1
        ordenado=False
        aux=0
        #tiempoInicial=System.nanoTime()
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
        #tiempoTotal=System.nanoTime()-tiempoInicial
        self.mostrarVector(datos)
        print()
        print()
        self.mostrarDatosDeEficiencia(contadorComparaciones, contadorIntercambios, contadorRecorridos, tiempoTotal)
    
    def ordenmientoPorSeleccion(self, datos):
        contadorComparaciones=0
        contadorIntercambios=0
        contadorRecorridos=0
        tiempoTotal=0
        tiempoInicial=0
        #tiempoInicial=System.nanoTime()
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
        #tiempoTotal=System.nanoTime()-tiempoInicial;
        self.mostrarVector(datos)
        print()
        print()
        self.mostrarDatosDeEficiencia(contadorComparaciones, contadorIntercambios, contadorRecorridos, tiempoTotal)
    
    
    
edades=[34, 25, 12, 87, 9, 10, 34, 37, 24, 2]

metodos=MetodosDeOrdenamiento()

print("=================VECTOR ORIGINAL======================")
metodos.mostrarVector(edades)
print()
print()
print("===============ORDENAMIENTO BURBUJA===================")
metodos.ordenamientoBurbuja0(edades)

edades=[34, 25, 12, 87, 9, 10, 34, 37, 24, 2]
metodos.ordenamientoBurbuja1(edades)

edades=[34, 25, 12, 87, 9, 10, 34, 37, 24, 2]
metodos.ordenamientoBurbuja2(edades)

edades=[34, 25, 12, 87, 9, 10, 34, 37, 24, 2]
#metodos.ordenamientoBurbuja3(edades)
print();
print();

print("===============ORDENAMIENTO SELECCION====================")
edades=[34, 25, 12, 87, 9, 10, 34, 37, 24, 2]
metodos.ordenmientoPorSeleccion(edades)
