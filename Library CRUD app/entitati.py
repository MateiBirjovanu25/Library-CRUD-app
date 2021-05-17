from dunno import error_autor,error_cnp,error_descriere,error_nume,error_titlu

class Carte:
    nr_Carti=0
    def __init__(self,idc,titlu,descriere,autor):
        self.__idc=idc
        self.__titlu=titlu
        self.__descriere=descriere
        self.__autor=autor
    
    def __str__(self):
        return str(self.__idc)+','+str(self.__titlu)+','+str(self.__descriere)+','+str(self.__autor)

    def getId(self):
        return self.__idc
    def getTitlu(self):
        return self.__titlu
    def getDescriere(self):
        return self.__descriere
    def getAutor(self):
        return self.__autor

    def setId(self,a):
        self.__idc=a
    def setTitlu(self,a):
        self.__titlu=a
    def setDescriere(self,a):
        self.__descriere=a
    def setAutor(self,a):
        self.__autor=a






class Client:
    nr_Clienti=0
    def __init__(self,idc,nume,cnp):
        self.__idc=idc
        self.__nume=nume
        self.__cnp=cnp
    
    def __str__(self):
     return str(self.__idc)+','+str(self.__nume)+','+str(self.__cnp)
    
    def getId(self):
     return self.__idc
    def getNume(self):
     return self.__nume
    def getCnp(self):
     return self.__cnp

    def setNume(self,p):
        self.__nume=p

    def setCnp(self,p):
        self.__cnp=p




class Imprumut:
    def __init__(self,car,cli):
        self.__carte=car
        self.__client=cli
        self.__stare="True"

    def getCarte(self):
        return self.__carte
    def getClient(self):
        return self.__client
    def getStare(self):
        return self.__stare
    def setStare(self,a):
        self.__stare=a
    def returnare(self):
        self.__stare="False"


class Raport:
    def __init__(self,nume):
        self.__nrInchirieri=1
        self.__numeCarte=nume
        self.__numeClient=nume
        self.__numeAutor=nume
        self.__nrReturnari=0
    def inc(self):
        self.__nrInchirieri+=1
    
    def inc2(self):
        self.__nrReturnari+=1

    def getNrInchirieri(self):
        return self.__nrInchirieri
    def getNrReturnari(self):
        return self.__nrReturnari
    def getNumeCarte(self):
        return self.__numeCarte
    def getNumeClient(self):
        return self.__numeClient
    def getNumeAutor(self):
        return self.__numeAutor
    
    def setNrInchirieri(self,a):
        self.__nrInchirieri=a
    def setNrReturnari(self,a):
        self.__nrReturnari=a