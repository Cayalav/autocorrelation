import numpy as np

def acf(data):
	mean = np.mean(data) #Promedio
	var = data.var() #Calculamos la varianza
	length = len(data) #Longitud

	acf_array = [] #Declaramos array solucón
	for t in np.arange(0,length): #Recorremos
		temp = np.mean((data[:(length-t)] - mean)*(data[t:] - mean))/var #Promedio de todos los puntos generados
		acf_array.append(temp) #Agregamos al final

	acf_array = np.array(acf_array) # Asignamos el array
	return acf_array


def random_arr(n): #Generador Array
  return np.random.randint(15, size=n) 


n = 20  
arr=random_arr(n) #Generaremos un array de 20

result=acf(arr) #Llamamos la función acf 
print(arr)
print(result)