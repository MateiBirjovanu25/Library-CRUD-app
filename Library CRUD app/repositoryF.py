from entitati import Carte,Client,Imprumut
from dunno import error_find,error_save,error_delete,error_update,error_imprumut1


class RepoCarte:
    def __init__(self,nume):
        self.__lista=self.__loadAll(nume)
        self.__numefis=nume
     
     
    def __loadAll(self,nume):
        rez=[]
        with open(nume,"r") as f:
            for line in f:
                if len(line)==0: continue
                b=line.split(";")
                c=Carte(b[0],b[1],b[2],b[3].rstrip())
                rez.append(c)
        return rez
    
    def __storeAll(self,nume):
        with open(nume,"w") as f:
            for i in self.__lista:
                line=i.getId()+";"+i.getTitlu()+";"+i.getDescriere()+";"+i.getAutor()
                f.write(line)
                f.write("\n")
    
    def save(self,c):
        """
        Salveaza o carte in repo
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

        self.__storeAll(self.__numefis)


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
        self.__storeAll(self.__numefis)

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
        self.__storeAll(self.__numefis)

    def getAll(self):
        return self.__lista







class RepoClient:
    def __init__(self,nume):
        self.__lista=self.__loadAll(nume)
        self.__numefis=nume


    def __loadAll(self,nume):
        rez=[]
        with open(nume,"r") as f:
            for line in f:
                if line=="": continue
                b=line.split(";")
                c=Client(b[0],b[1],b[2].rstrip())
                rez.append(c)
        return rez
    
    def __storeAll(self,nume):
        with open(nume,"w") as f:
            for i in self.__lista:
                line=i.getId()+";"+i.getNume()+";"+i.getCnp()
                f.write(line)
                f.write("\n")


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
        self.__storeAll(self.__numefis)


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
        self.__storeAll(self.__numefis)

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
        self.__storeAll(self.__numefis)



class RepoImprumut:
    def __init__(self,nume):
        self.__lista=self.__loadAll(nume)
        self.__listaPerm=[]
        self.__numefis=nume


    def __loadAll(self,nume):
        rez=[]
        with open(nume,"r") as f:
            for line in f:
                if line=="": continue
                b=line.split("---")
                cr=b[0].split(";")
                cl=b[1].split(";")
                carte=Carte(cr[0],cr[1],cr[2],cr[3])
                client=Client(cl[0],cl[1],cl[2])
                i=Imprumut(carte,client)
                i.setStare(b[2].rstrip())
                rez.append(i)
        return rez
    
    def __storeAll(self,nume):
        with open(nume,"w") as f:
            for i in self.__lista:
                line=i.getCarte().getId()+";"+i.getCarte().getTitlu()+";"+i.getCarte().getDescriere()+";"+i.getCarte().getAutor().rstrip()+"---"+i.getClient().getId()+";"+i.getClient().getNume()+";"+i.getClient().getCnp().rstrip()+"---"+i.getStare()
                f.write(line)
                f.write("\n")
    

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
        self.__storeAll(self.__numefis)


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
        self.__storeAll(self.__numefis)

    def update(self,id):
        """
        modifica starea unei inchirieri
        """
        rez=self.find(id)
        for i in rez:
             i.setStare("False")
        self.__storeAll(self.__numefis)

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


    