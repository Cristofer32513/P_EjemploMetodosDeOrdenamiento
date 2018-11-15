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
        contadorComparaciones=0, contadorIntercambios=0, contadorRecorridos=0
        tiempoTotal=0, tiempoInicial=0
        
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
        self.__mostrarVector(datos)
        print()
        print()
        self.__mostrarDatosDeEficiencia(contadorComparaciones, contadorIntercambios, contadorRecorridos, tiempoTotal);
    
        
    