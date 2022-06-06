import numpy as np
import matplotlib.pyplot as plt

#Método para dar formato a la tabla.
def formatearDatos(listxt):
        nueva_lista=[]
        lista_aux=[]
        datos = listxt.shape #Método de numpy para las dimensiones de la tabla.
        num_filas = datos[0] #Guardamos el número de filas.
        num_colum = datos[1] #Guardamos el número de columas.
        for i in range(0,num_filas): 
            lista_aux=[] #Creamos una lista que tendrá los datos de cada fila.
            for j in range(0,num_colum): #Hacemos un for que recorra todas las columnas.
                dato_format= str(listxt[i,j]) #Guardamos un solo dato en dato_format del numpy.array que entra y lo convertimos a string
                if dato_format[0].isalpha(): #Preguntamos si el elemento es un string.
                    lista_aux.append(str(listxt[i,j])) #Si lo es, lo guarda en la lista auxiliar.
                elif dato_format[0].isnumeric() or dato_format[0] =="-": #si es número o si empienumero negativo.
                    if len(dato_format) ==1: #Si es un único número.
                        lista_aux.append(float(listxt[i,j])) # Guarda en la lista auxiliar como float.
                    elif dato_format[2] =="/": #Pregunta fecha, formato dia/mes/año.
                        lista_aux.append(str(listxt[i,j])) #guarda en la lista auxiliar como string.
                    else:
                        lista_aux.append(float(listxt[i,j])) # Lo demas se guarda como float en lista auxiliar.
                else:
                    print("no entro en ninguno")
            nueva_lista.append(lista_aux) #Después de acabar el for interno, guardamos en nueva_lista la lista que se formó.
        listxt = nueva_lista #Reemplazamos el numpy array que entro con una lista de listas.
        return listxt #Retornamos la lista de listas.


#Método para verificar si la dirección del archivo es correcta.
def verificarRuta(txt): 
    try:
        txt = open(txt) #Abrimos el archivo, esto nos generara un error si no existe un archivo en esta dirección.
        listxt = np.loadtxt(txt,delimiter=",",dtype=str) # Utilizamos el método loadtxt para convertir el txt en un array de numpy.
        listxt= formatearDatos(listxt) #Mandamos el array de numpy a darle formato.
        return listxt #Devolvemos la lista de listas.
    except:
        print("ruta no valida")

#Método para crear la leyenda con los datos.
def CrearLeyenda(nombres,datos):
    salida =[]
    for i in range(0,len(nombres)): #Ciclo para iterar en los nombres.
        salida.append("{}--{}".format(nombres[i],str(datos[i]))) #Ingresamos en salida el nombre con el dato.
    return salida

#Método para crear la leyenda con los porcentajes
def CrearLeyendaPorcentajes(nombres,datos,total):
    salida =[]
    porcentajes=[]
    for i in range(0,len(datos)):#Ciclo para iterar en los datos.
        porcentajes.append((datos[i]/total)*100) #Ingresamos los porcentajes de datos.
    for i in range(0,len(nombres)): #Ciclo para iterar en los nombres.
        salida.append("{}--{}".format(nombres[i],str('%.1f'%porcentajes[i] + "%"))) #Ingresamos en salida el nombre con el porcentaje.
    return salida

#Primer tipo de dato.
class DatosG: 
    def __init__(self,txt): #Constructor de la clase, le entra la dirección de el archivo.
        self.listxt = verificarRuta(txt) #verificar la dirección y retorna una lista de listas con formarto aplicado.
        self.columnas= self.listxt[0] #Creamos una variable columnas que guardará el nombre de las columnas.
    
    def __str__(self): #Método para cuando se imprima un objeto de esta clase nos brinde información.
        formato= "Estructura de datos numero 1\nDimensiones de la tabla: {}\n"\
            "Nombre de las columnas {}".format((len(self.listxt),len(self.listxt[0])),self.listxt[0]) #Diseñamos un estilo para imprimir.
        return formato 


    #Método para verificar si un objeto de esta clase es igual a otra instancia de esta clase.
    def __eq__(self,another): 
        if isinstance(another,DatosG): #Preguntamos si el objeto el cual comparamos es un objeto de esta clase.
            if self.listxt == another.listxt: #Preguntamos si la listas internas de cada objetos son iguales.
                return True
            else: #Si no son iguales.
                return False
        else: #Si no es un objeto de esta clase.
            return False
        
    #Método para comparar con mayor igual que.
    def __ge__(self,another):
        if isinstance(another,DatosG):#Preguntamos si la entrada es un objeto de la clase MultiGrafics.
            n1 = (len(self.listxt),len(self.listxt[0]))#Guardamos las dimensiones del primer objeto.
            n2 = (len(another.listxt),len(another.listxt[0]))#Guardamos las dimensiones del segundo objeto.
            r1 = n1[0]*n1[1]#Guardamos el total de datos que existen en la tabla  1.
            r2 = n2[0]*n2[1]#Guardamos el total de datos que existen en la tabla 2.
            if r1 >= r2:
                return True
            else:
                return False
        else:
            print("no se pueden comparar")#Si se esta comparando con un objeto de una clase diferente.

    #Método para comparar con menor igual que >=.
    def __le__(self,another):
        if isinstance(another,DatosG):#Preguntamos si la entrada es un objeto de la clase MultiGrafics
            n1 = (len(self.listxt),len(self.listxt[0]))#Guardamos laas dimensiones de el primer objeto.
            n2 = (len(another.listxt),len(another.listxt[0]))#Guardamos las dimensiones del segundo objeto.
            r1 = n1[0]*n1[1]#Guardamos el total de datos que existen en la tabla  1.
            r2 = n2[0]*n2[1]#Guardamos el total de datos que existen en la tabla 2.
            if r1 <= r2:#Si los datos en la tabla 1 son menores o iguales a los de la tabla 2
                return True
            else:
                return False
        else:
            print("no se pueden comparar")

    def mostarData(self): #Método para mostrar en un string toda la tabla.
        return str(self.listxt)
    def listaDatos(self):  #Método para devoler la lista de listas.
        return self.listxt
    def nombreColumnas(self):#Método para devolver la lista de columnas.
        return self.columnas
 
    #Método para devolver las dimensiones de la tabla.    
    def dimensiones(self):
        salida = (len(self.listxt),len(self.listxt[0])) #Creamos una tupla con el número de filas y el número de columnas.
        return salida #retornamos esa tupla
    
    #Método para calcular cuantos datos de un valor espeficico hay en una columna.
    def cantidadDeEn(self,valor,columna):
        columnas = list(self.listxt[0]) #Guardamos los nombre de las columnas en esta variable.
        pos=0 
        contador =0
        if columna in columnas:
            pos = columnas.index(columna) #Guardamos la posición de esa columna en pos.
            for i in self.listxt: #Ciclo para saber cuantas veces esta el valor en esa columna.
                if i[pos] == valor: #Si el valor que está en la tabla es igual a el valor ingresado.
                    contador +=1
                else: #Si no es igual
                    continue
            return contador #Retornamos contador, el valor de contador será las veces que esta el dato en la columna.
        else:
            print("La columna no existe en la tabla") 
  
    #Método para tomar los valores de una columna sin repetir.
    def colSinRepetir(self,colum): 
        result=[]
        for i in self.listxt[1:]: #Hacemos un ciclo en la tabla a partir de la fila numero 1.
            if i[1] not in result: #Preguntamos si el valor no esta en la lista result.
                result.append(i[colum]) #Guardamos el dato en la lista result.
            else:
                continue 
        return result #Devolvemos la lista con los valores sin repetir.

#Segundo tipo de dato.
class MultGrafics(DatosG): 

    #Metodo constructor.
    def __init__(self, inicializador): 
        if isinstance(inicializador,DatosG): #Preguntamos si el objeto que entra es de tipo DatosG.
            self.obj = inicializador #Guardamos el objeto en self.obj.
            self.listxt = self.obj.listxt #Guardamos la lista de listas del objeto que entra en self.listxt.
        elif isinstance(inicializador,str): #Preguntamos si la entrada es un string.
            super().__init__(inicializador) #Si es un string utilizamos el metodo super para iniciar el objeto.
    
    #Método para imprimir
    def __str__(self):
        formato= "Estructura de datos numero 2\ndimensiones de la tabla: {}\n"\
            "nombre de las columnas {}".format((len(self.listxt),len(self.listxt[0])),self.listxt[0]) #Estilo de impresión.
        return formato 

    #Método para saber si 2 objetos son iguales
    def __eq__(self, another):
        if isinstance(another,MultGrafics): #Preguntamos si el objeto el cual comparamos es un objeto de esta clase.
            if self.listxt == another.listxt: #Preguntamos si las listas internas de cada objeto son iguales.
                return True
            else: #Si no son iguales.
                return False
        else: #Si no es un objeto de esta clase.
            return False

    #Método para comparar con mayor igual que.
    def __ge__(self,another):
        if isinstance(another,MultGrafics):#si la entrada es un objeto de la clase MultiGafics.
            n1 = (len(self.listxt),len(self.listxt[0])) #dimensiones del primer objeto.
            n2 = (len(another.listxt),len(another.listxt[0])) #dimensiones del segundo objeto.
            r1 = n1[0]*n1[1] #Guardamos el total de datos que existen en la tabla  1.
            r2 = n2[0]*n2[1] #Guardamos el total de datos que existen en la tabla 2.
            if r1 >= r2: 
                return True
            else:
                return False
        else:
            print("No se pueden comparar.")

    #Método para comparar con menor igual.
    def __le__(self,another): 
        if isinstance(another,MultGrafics): #si la entrada es un objeto de la clase MultiGrafics

            n1 = (len(self.listxt),len(self.listxt[0])) #dimensiones de el primer objeto.
            n2 = (len(another.listxt),len(another.listxt[0])) #dimensiones del segundo objeto.
            r1 = n1[0]*n1[1] #Guardamos el total de datos que existen en la tabla  1.
            r2 = n2[0]*n2[1] #Guardamos el total de datos que existen en la tabla 2.
            if r1 <= r2:#Si los datos en la tabla 1 son menores o iguales a los de la tabla 2
                return True
            else:
                return False
        else:
            print("No se pueden comparar.")

     #Método gráfica simple con matplotlib.       
    def graficar(self,x,y,labels): 
        fig,ax = plt.subplots() #múltiples gráficas en una sola visualización
        for i in range(0,len(x)): #ciclo para ingresar todos los puntos en la gráfica
            ax.scatter(i-(1/2),y[i],60,marker="*") #Formato para que no se peguen los puntos 
        ax.set_title("Grafico de puntos")
        leyenda = CrearLeyenda(x,y) #Le damos un cuadro de informacion a la leyenda.
        ax.legend(leyenda) #Ingresamos la leyenda a la tabla.
        ax.set_xticklabels([]) #Ingresamos una lista vacía a las etiquetas de las x 
        ax.set_xlabel(labels[1]) #nombre de x
        ax.set_ylabel(labels[0]) #nombre de y
        plt.show() #Mostramos la gráfica.

     #Método gráfica de barras con matplotlib.
    def graficarBarras(self,x,y,labels):
        fig,ax = plt.subplots() #múltiples gráficas en una sola visualización.
        for i in range(0,len(x)): #ciclo para ingresar todos los puntos en la gráfica.
            ax.bar(i-(0.60/2),y[i],0.60) #Formato para que no se peguen las barras.
        ax.set_title("Grafico de barras.") #Titulo
        leyenda = CrearLeyenda(x,y)#Le damos un cuadro de informacion a la leyenda.
        ax.legend(leyenda) #Ingresamos la leyenda a la tabla.
        ax.set_xticklabels([])#Ingresamos una lista vacía a las etiquetas de las x.
        ax.set_xlabel(labels[1])#nombre de x.
        ax.set_ylabel(labels[0])#nombre de y.
        plt.show()#Mostramos la gráfica.

    #Método gráfica de porcentaje.
    def graficaPortentaje(self,porsentaje,nombres):
        plt.pie(porsentaje,autopct="%0.1f %%") #Formato para crear la gráfica con porcentajes.
        leyenda = CrearLeyendaPorcentajes(nombres,porsentaje,self.dimensiones()[0]-1) #formato para la leyenda de porcentajes.
        plt.legend(leyenda,ncol=1,loc="upper right",bbox_to_anchor=(1.5,1)) #leyenda de la tabla.
        plt.show() #Mostramos la gráfica.
