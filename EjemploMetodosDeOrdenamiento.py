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
    
        
    