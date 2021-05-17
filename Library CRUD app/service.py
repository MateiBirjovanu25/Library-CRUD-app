#from repository import RepoCarte,RepoClient,RepoImprumut
from repositoryF import RepoCarte,RepoClient,RepoImprumut
from repositoryFmos import RepoCartef,RepoClientf,RepoImprumutf
from entitati import Carte,Client,Imprumut,Raport
from dunno import error_find,error_imprumut1,error_imprumut2
from validator import Validare
import string,random

class ServiceCarte:
    def __init__(self,repo,fis):
        self.__repo=RepoCartef(fis)
        self.__lista=repo

    def adauga(self,idc,titlu,descriere,autor):
        """
        Adauga o carte in lista din repo
        :param idc:
        :param titlu:
        :param descriere:
        :param autor:
        :return:
        """
        c=Carte(idc,titlu,descriere,autor)
        val = Validare()
        val.validareCarte(c)
        self.__repo.save(c)

    def sterge(self,id):
        """
        Sterge o carte din lista din repo
        :param id:
        :return:
        """
        gasit=0
        for i in self.__lista:
            if i.getCarte().getId()==id:
                if i.getStare()==True:
                    gasit=1
        if gasit == 1:
            raise error_imprumut2
        else:
            self.__repo.delete(id)

    def actualizeaza(self,id,titlu,descriere,autor):
        """
        Actualizeaza o carte din lista din repo
        :param id:
        :param titlu:
        :param descriere:
        :param autor:
        :return:
        """
        carte=Carte(id,titlu,descriere,autor)
        val = Validare()
        val.validareCarte(carte)
        self.__repo.update(id,titlu,descriere,autor)

    def cautare(self,id):
        """
        Cauta o carte din lista din repo
        :param id:
        :return:
        """
        return self.__repo.find(id)

    def cautareTitlu(self,titlu):
        """
        Cauta o carte din lista din repo dupa titlu
        :param titlu:
        :return:
        """
        for i in self.__repo.getAll():
            if i.getTitlu()==titlu:
                return i
        raise error_find

    def cautareNume(self,nume):
        """
                Cauta o carte dupa nume
                :param nume:
                :return:
                """
        a=[]
        for i in self.__repo.getAll():
            if nume in i.getTitlu() or nume in i.getAutor():
                a.append(i)
        if len(a)==0:
            raise error_find
        else:
            return a


    def getCarti(self):
        """
        Returneaza lista de carti din lista din repo
        :return:
        """
        return self.__repo.getAll()

    def generareCarte(self):
        """
        Genereaza o carte random
        :return:
        """
        letters = string.ascii_lowercase
        digits = string.digits
        id = ''.join(random.choice(digits) for i in range(3))
        titlu = ''.join(random.choice(letters) for i in range(5))
        descriere = ''.join(random.choice(letters) for i in range(10))
        autor = ''.join(random.choice(letters) for i in range(5))
        return Carte(id,titlu,descriere,autor)

    def adaugareRandom(self,nr):
        """
        Salveaza "nr" carti generate random
        :param nr:
        :return:
        """
        for i in range(1,nr+1):
            k=self.generareCarte()
            val = Validare()
            val.validareCarte(k)
            self.__repo.save(k)






class ServiceClient:
    def __init__(self,repo,fis):
        self.__repo=RepoClientf(fis)
        self.__lista=repo

    def adauga(self,idc,nume,cnp):
        """
        Adauga un client in lista din repo
        :param idc:
        :param nume:
        :param cnp:
        :return:
        """
        c=Client(idc,nume,cnp)
        val = Validare()
        val.validareClient(c)
        self.__repo.save(c)

    def sterge(self,id):
        """
        Sterge un client din lista din repo
        :param id:
        :return:
        """

        gasit = 0
        for i in self.__lista:
            if i.getClient().getId() == id:
                if i.getStare()==True:
                    gasit = 1
        if gasit == 1:
            raise error_imprumut2
        else:
            self.__repo.delete(id)


    def actualizeaza(self,id,nume,cnp):
        """
        Actualizeaza un client din lista din repo
        :param id:
        :param nume:
        :param cnp:
        :return:
        """
        client=Client(id,nume,cnp)
        val = Validare()
        val.validareClient(client)
        self.__repo.update(id,nume,cnp)

    def cautare(self,id):
        """
        Cauta un client in lista din repo
        :param id:
        :return:
        """
        return self.__repo.find(id)

    def cautareNume(self,nume):
        """
        Cauta un client dupa nume
        :param nume:
        :return:
        """
        a=[]
        for i in self.__repo.getAll():
            if nume in i.getNume():
                a.append(i)
        if len(a)==0:
            raise error_find
        else:
            return a

    def getClienti(self):
        """
        Returneaza lista de clienti
        :return:
        """
        return self.__repo.getAll()

    def generareClient(self):
        """
        Genereaza un client random
        :return:
        """
        letters = string.ascii_lowercase
        digits = string.digits
        id = ''.join(random.choice(digits) for i in range(3))
        nume = ''.join(random.choice(letters) for i in range(5))
        cnp = ''.join(random.choice(digits) for i in range(13))
        return Client(id,nume,cnp)

    def adaugareRandom(self,nr):
        """
        Salveaza "nr" clienti random
        :param nr:
        :return:
        """
        for i in range(1,nr+1):
            k=self.generareClient()
            val = Validare()
            val.validareClient(k)
            self.__repo.save(k)




class ServiceImprumut:
    def __init__(self,fis):
        self.__repo=RepoImprumutf(fis)
    def adauga(self,carte,client):
        """

        :param carte:
        :param client:
        :return:
        """
        im=Imprumut(carte,client)
        self.__repo.save(im)
    def sterge(self,id):
        """

        :param id_carte:
        :return:
        """
        self.__repo.delete(id)

    def returneaza(self,id):
        """

        :param id:
        :return:
        """
        imprumut=self.__repo.find(id)
        rodie=0
        for i in imprumut:
            if i.getStare()=="True":
                self.__repo.update(i.getCarte().getId())
                rodie=1
        if rodie==0:
            raise error_imprumut1

    def getImprumuturi(self):
        """

        :return:
        """
        return self.__repo.getAll()

    def celeMaiImprumutate(self):
        """
        raport ce returneaza cartile cu cele mai multe inchirieri
        :return:
        """
        listaRaportCeleMai={}
        for i in self.__repo.getAll():
            IdCarte=int(i.getCarte().getId())
            if IdCarte in listaRaportCeleMai:
                listaRaportCeleMai[IdCarte].inc()
            else:
                listaRaportCeleMai[IdCarte]=Raport(i.getCarte().getTitlu())

        rez=list(listaRaportCeleMai.values())
        #rez=sorted(rez,key=lambda x:x.getNrInchirieri(),reverse=True)
        for i in range(0,len(rez)-1):
            for j in range(i,len(rez)):
                if rez[i].getNrInchirieri()<rez[j].getNrInchirieri()  :
                    rez[i],rez[j]=rez[j],rez[i]

        max=rez[0].getNrInchirieri()
        a=[]
        for i in rez:
            if i.getNrInchirieri()==max:
                a.append(i)
        return a


    def clientiOrdonati(self):
        """
        raport ce returneaza lista clientilor ce au carti inchiriate in ordine alfabetica si in ordinea cartilor inchiriate
        :return:
        """
        listaRaportClient={}
        for i in self.__repo.getAll():
            IdClient=int(i.getClient().getId())
            if i.getStare()=="True":
                if IdClient in listaRaportClient:
                    listaRaportClient[IdClient].inc()
                else:
                    listaRaportClient[IdClient]=Raport(i.getClient().getNume())
        rez = list(listaRaportClient.values())

        for i in range(0,len(rez)-1):
            for j in range(i,len(rez)):
                if rez[i].getNrInchirieri()<rez[j].getNrInchirieri()  :
                    rez[i],rez[j]=rez[j],rez[i]

        for i in range(0,len(rez)-1):
            for j in range(i,len(rez)):
                if rez[i].getNumeClient()<rez[j].getNumeClient()  :
                    rez[i],rez[j]=rez[j],rez[i]

        return rez

    def clientiActivi(self):
        """
        raport ce returneaza primii 20% din clienti in ordinea activitatii
        :return:
        """
        listaRaport={}
        for i in self.__repo.getAll():
            idClient=int(i.getClient().getId())
            if idClient in listaRaport:
                listaRaport[idClient].inc()
            else:
                listaRaport[idClient] = Raport(i.getClient().getNume())

        rez=list(listaRaport.values())


        for i in range(0,len(rez)-1):
            for j in range(i,len(rez)):
                if rez[i].getNumeClient()<rez[j].getNumeClient()  :
                    rez[i],rez[j]=rez[j],rez[i]
        
        for i in range(0,len(rez)-1):
            for j in range(i,len(rez)):
                if rez[i].getNrInchirieri()<rez[j].getNrInchirieri()  :
                    rez[i],rez[j]=rez[j],rez[i]

        a=[]
        for i in range(0,int(len(rez)/5)):
            a.append(rez[i])

        return a
    
    def celMaiScriitor(self,service):
        """
        raport ce returneaza 
        :return:
        """
        listaRaport={}
        for i in self.__repo.getAll():
            autor=i.getCarte().getAutor()
            if autor in listaRaport:
                if i.getStare()=="True":
                    listaRaport[autor].inc()
                elif i.getStare()=="False":
                    listaRaport[autor].inc2()
            else:
                listaRaport[autor]=Raport(i.getCarte().getAutor())
                if i.getStare()=="True":
                    listaRaport[autor].setNrInchirieri(1)
                    listaRaport[autor].setNrReturnari(0)
                elif i.getStare()=="False":
                    listaRaport[autor].setNrInchirieri(0)
                    listaRaport[autor].setNrReturnari(1)
        
        
        a=list(listaRaport.values())
        rez=[]
        rezf=[]
        lista=[]
        lista2=[]
        for i in a:
            if i.getNrInchirieri()!=0:
                rez.append(i)
        
        for i in self.getImprumuturi():     #lista = lista cu carti din imprumuturi
            lista.append(i.getCarte())
        """
        for i in lista:
            print(i.getAutor())
        """

        for k in service.getCarti():   
            ananas=0
            for j in lista:
                if k.getTitlu()==j.getTitlu():
                    ananas=1
            if ananas==0:
                lista2.append(k.getAutor())
               

        for i in rez:
            if i.getNumeAutor() in lista2:
                rezf.append(i.getNumeAutor())
        
        return rezf












