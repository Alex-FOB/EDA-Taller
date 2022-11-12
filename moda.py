class Moda:
    __vector = None
    __lista = None
    __max = None
    __resultado = None
    def __init__(self):
        self.__lista = []
        self.__max = 0
    def calcular(self, vector):
        self.__vector = vector
        self.__recorrer()
        return self.__resultado
    def __recorrer(self):
        i = 0
        while i < len(self.__vector):
            cont = 1 #contador de repeticiones
            if(self.__verificar(i)):
                j = i+1
                while j < len(self.__vector):
                    if(self.__vector[j] == self.__vector[i]):
                        cont += 1
                    j += 1
                self.__lista.append(self.__vector[i])
                self.__maximo(self.__vector[i], cont)
            i += 1
    def __verificar(self, pos): #verifica que no se cuente el mismo dato ya analizado
        band = True
        i = 0
        while len(self.__lista) > 0 and band and i < len(self.__lista):
            if(self.__lista[i] == self.__vector[pos]):
                band = False
            i += 1
        return band
    def __maximo(self, dato, rep): #analiza el/los datos que mas se repiten en el vector
        #print('Dato:', dato, 'Cant:', rep)
        if(rep > self.__max):
            self.__max = rep
            self.__resultado = dato