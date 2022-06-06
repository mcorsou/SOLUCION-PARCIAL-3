from modulo1 import funciones
obj =0 #Variable global: Este será nuestro objeto, lo iniciamos arbitrariamente en cero.

#Método principal.
def main():
    global obj #Utilizamos la palabra global para indicar que modificaremos el valor de objeto y este se guarde. 
    bandera =True
    while bandera: #Ciclo para pedir los datos.
        entrada = input("Ingrese la direccion del archivo:= ") #Ingresamos la dirección del archivo.
        try:
            x = open(entrada) #Abrimos el archivo, esto generará error si la dirección del archivo es erronea.
            obj= funciones.DatosG(entrada) #Creamos un objeto de la clase DatosG.
            bandera = False
            menu() 
            break
        except:
            print("Ruta no valida.")

#Método para mostrar el menú.
def menu():
    bandera1 = True
    while bandera1: #Ciclo para mostrar el menu.
        formato = "1. Mostar columnas.\n2. Información.\n3. Dimension de la tabla.\n4. Graficar cantidad de personas respecto a municipio.\n"\
            "5. Graficar en barras.\n6. Graficar en porcentaje.\n7. Salir.\nOpción := "
        print("Menú".center(50,"*"))
        entrada = input(formato) #Guardamos la opción en entrada.
        if entrada =="1":
            print("Las columnas en la tabla son: {}".format(obj.nombreColumnas())) #Utilizamos el método nombreColumnas de la libreria.
        elif entrada =="2":
            print("Información general de la tabla:= {}".format(obj)) #Utilizamos el método __str__.
        elif entrada =="3":
            print("La dimension de la tabla es:= {}".format(obj.dimensiones())) #Utilizamos el método dimensiones.
        elif entrada == "4":

            titulos = obj.nombreColumnas() #método nombreColumnas de nuestra libreria.
            x = obj.colSinRepetir(1) #método de la libreria.
            y =[]
            for i in x:
                y.append(obj.cantidadDeEn(i,titulos[1])) #métodos de la  libreria

            obj2 = funciones.MultGrafics(obj)#Creamos un objeto de la segunda estructura de datos.
            labels = ["Número de personas",titulos[1]]
            obj2.graficar(x,y,labels)   #Graficamos con el método creado en nuestra libreria.
        
        elif entrada=="5":
             titulos = obj.nombreColumnas() #Utilizamos el método nombreColumnas.
             x = obj.colSinRepetir(1) #método de la libreria.
             y =[]
             for i in x:
                y.append(obj.cantidadDeEn(i,titulos[1])) #método de la libreria.

             obj2 = funciones.MultGrafics(obj) #Creamos un objeto de la segunda estructura de datos.
             labels = ["Número de personas",titulos[1]]
             obj2.graficarBarras(x,y,labels) #Graficamos con el método creado en nuestra libreria.

        elif entrada=="6":
            titulos = obj.nombreColumnas() #Utilizamos el método nombreColumnas de nuestra libreria.
            x = obj.colSinRepetir(1) #método de la libreria.
            y =[]
            for i in x:
                y.append(obj.cantidadDeEn(i,titulos[1])) #método de la libreria.
            obj2 = funciones.MultGrafics(obj)#Creamos un objeto de la segunda estructura de datos.
            obj2.graficaPortentaje(y,x) #Graficamos con el método creado en nuestra libreria.

        elif entrada=="7": #Opción para cerrar el programa
            bandera1 =False
            break
        else:
            print("Opción no valida, revisa el menu.")

main() #Llamamos a la función principal.
print("Fin del programa".center(50,"*"))
