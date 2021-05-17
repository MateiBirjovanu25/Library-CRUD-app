from entitati import Carte,Client,Imprumut
from dunno import error_find,error_save,error_delete,error_update,error_imprumut1
class RepoCarte:
    def __init__(self):
        self.__lista=[]
     
    
    
    def save(self,c):
        """
        Salveaza o carte in repo
        :param c:
        :return:
        """
        gasit=0
        for i in self.__lista:
            if i.getId()==c.getId():gasit=1

        if gasit==0:
            self.__lista.append(c)
        else: raise error_save

    def find(self,id):
        """
        Gaseste o carte din repo
        :param id:
        :return:
        """
        for i in self.__lista:
            if i.getId()==id:
                return i
        raise error_find

    def delete(self,id):
        """
        Sterge o carte din repo
        :param id:
        :return:
        """
        gasit=0
        for i in self.__lista:
            if i.getId()==id:
                self.__lista.remove(i)
                gasit=1
                break
        if gasit==0: raise error_delete

    def update(self,id,titlu,descriere,autor):
        """
        Updateaza o carte din repo
        :param id:
        :param titlu:
        :param descriere:
        :param autor:
        :return:
        """
        gasit=0
        for i in self.__lista:
            if i.getId()==id:
                i.setTitlu(titlu)
                i.setDescriere(descriere)
                i.setAutor(autor)
                gasit=1
        if gasit==0: raise error_update

    def getAll(self):
        return self.__lista







class RepoClient:
    def __init__(self):
        self.__lista=[]
    def save(self,c):
        """
        Salveaza in lista clientul c
        :param c:
        :return:
        """
        gasit=0
        for i in self.__lista:
            if i.getId()==c.getId():
                gasit=1
        if gasit==0:
            self.__lista.append(c)
        else: raise error_save
    def getAll(self):
        """
        Returneaza lista
        :return:
        """
        return self.__lista

    def find(self,id):
        """
        Gaseste clientul cu id-ul id
        :param id:
        :return:
        """
        for i in self.__lista:
            if i.getId()==id:
                return i
        raise error_find

    def delete(self,id):
        """
        Sterge clientul cu id-ul id
        :param id:
        :return:
        """
        gasit=0
        for i in self.__lista:
            if i.getId()==id:
                self.__lista.remove(i)
                gasit=1
                break
        if gasit==0: raise error_delete

    def update(self,id,nume,cnp):
        """
        Updateaza clientul 
        :param id:
        :param nume:
        :param cnp:
        :return:
        """
        gasit=0
        for i in self.__lista:
            if i.getId()==id:
                i.setNume(nume)
                i.setCnp(cnp)
                gasit=1
        if gasit==0: raise error_update



class RepoImprumut:
    def __init__(self):
        self.__lista=[]
        self.__listaPerm=[]

    def save(self,i):
        """
        Salveaza un imprumut
        :param i:
        :return:
        """
        gasit=0
        for j in self.__lista:
            if j.getCarte().getId()==i.getCarte().getId():
                if j.getStare()=="True":
                    gasit=1
        if gasit==0:
            self.__lista.append(i)
        else:
            raise error_save

    def delete(self,id):
        """
        Sterge un imprumut
        :param id:
        :return:
        """
        gasit=0
        for i in self.__lista:
            if i.getCarte().getId()==id:
                self.__lista.remove(i)
                gasit=1
        if gasit==0:raise error_delete

    def find(self,id):
        """
        gaseste un imprumut
        :param id:
        :return:
        """
        a=[]
        for i in self.__lista:
            if i.getCarte().getId() == id:
                a.append(i)
        if len(a)!=0: return a
        else:
            raise error_find




    def getAll(self):
        """
        Returneaza lista de imprimuturi
        :return:
        """
        return self.__lista


    