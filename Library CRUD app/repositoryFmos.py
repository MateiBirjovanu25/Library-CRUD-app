from repository import RepoCarte,RepoClient,RepoImprumut
from entitati import Carte,Client,Imprumut
from dunno import error_find,error_save,error_delete,error_update,error_imprumut1


class RepoCartef(RepoCarte):
    def __init__(self,nume):
        RepoCarte.__init__(self)
        self.__loadAll(nume)
        self.__numefis=nume
        
     
     
    def __loadAll(self,nume):
        with open(nume,"r") as f:
            for line in f:
                if len(line)==0: continue
                b=line.split(";")
                c=Carte(b[0],b[1],b[2],b[3].rstrip())
                RepoCarte.save(self,c)
    
    
    def __storeAll(self,nume):
        with open(nume,"w") as f:
            for i in RepoCarte.getAll(self):
                line=i.getId()+";"+i.getTitlu()+";"+i.getDescriere()+";"+i.getAutor()
                f.write(line)
                f.write("\n")
    
    def save(self,c):
        """
        Salveaza o carte in repo
        :param c:
        :return:
        """
        RepoCarte.save(self,c)
        self.__storeAll(self.__numefis)


    def find(self,id):
        """
        Gaseste o carte din repo
        :param id:
        :return:
        """
        return RepoCarte.find(self,id)

    def delete(self,id):
        """
        Sterge o carte din repo
        :param id:
        :return:
        """
        RepoCarte.delete(self,id)
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
        RepoCarte.update(self,id, titlu, descriere, autor)
        self.__storeAll(self.__numefis)

    def getAll(self):
        return RepoCarte.getAll(self)






class RepoClientf(RepoClient):
    def __init__(self,nume):
        RepoClient.__init__(self)
        self.__loadAll(nume)
        self.__numefis=nume


    def __loadAll(self,nume):
        with open(nume,"r") as f:
            for line in f:
                if line=="": continue
                b=line.split(";")
                c=Client(b[0],b[1],b[2].rstrip())
                RepoClient.save(self, c)
    
    def __storeAll(self,nume):
        with open(nume,"w") as f:
            for i in RepoClient.getAll(self):
                line=i.getId()+";"+i.getNume()+";"+i.getCnp()
                f.write(line)
                f.write("\n")


    def save(self,c):
        """
        Salveaza in lista clientul c
        :param c:
        :return:
        """
        RepoClient.save(self, c)
        self.__storeAll(self.__numefis)


    def getAll(self):
        """
        Returneaza lista
        :return:
        """
        return RepoClient.getAll(self)

    def find(self,id):
        """
        Gaseste clientul cu id-ul id
        :param id:
        :return:
        """
        return RepoClient.find(self, id)

    def delete(self,id):
        """
        Sterge clientul cu id-ul id
        :param id:
        :return:
        """
        RepoClient.delete(self, id)
        self.__storeAll(self.__numefis)

    def update(self,id,nume,cnp):
        """
        Updateaza clientul 
        :param id:
        :param nume:
        :param cnp:
        :return:
        """
        RepoClient.update(self, id, nume, cnp)
        self.__storeAll(self.__numefis)



class RepoImprumutf(RepoImprumut):
    def __init__(self,nume):
        RepoImprumut.__init__(self)
        self.__loadAll(nume)
        self.__numefis=nume


    def __loadAll(self,nume):
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
                RepoImprumut.save(self, i)
    
    def __storeAll(self,nume):
        with open(nume,"w") as f:
            for i in RepoImprumut.getAll(self):
                line=i.getCarte().getId()+";"+i.getCarte().getTitlu()+";"+i.getCarte().getDescriere()+";"+i.getCarte().getAutor().rstrip()+"---"+i.getClient().getId()+";"+i.getClient().getNume()+";"+i.getClient().getCnp().rstrip()+"---"+i.getStare()
                f.write(line)
                f.write("\n")
    

    def save(self,i):
        """
        Salveaza un imprumut
        :param i:
        :return:
        """
        RepoImprumut.save(self, i)
        self.__storeAll(self.__numefis)


    def delete(self,id):
        """
        Sterge un imprumut
        :param id:
        :return:
        """
        RepoImprumut.delete(self, id)
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
        return RepoImprumut.find(self, id)


    def getAll(self):
        """
        Returneaza lista de imprimuturi
        :return:
        """
        return RepoImprumut.getAll(self)