from entitati import Carte,Client,Imprumut,Raport
from validator import Validare
#from repository import RepoCarte,RepoClient,RepoImprumut
from repositoryF import RepoCarte,RepoClient,RepoImprumut
from repositoryFmos import RepoCartef,RepoClientf,RepoImprumutf 
from service import ServiceCarte,ServiceClient,ServiceImprumut

class Test:
    def __init__(self,txtcr,txtcl,txtim):
        self.__txtcr=txtcr
        self.__txtcl=txtcl
        self.__txtim=txtim
    def testCreeazaCarte(self):
        c=Carte(1,"abc","cab","bca")
        assert c.getId()==1
        assert c.getTitlu()=="abc"
        assert c.getDescriere()=="cab"
        assert c.getAutor()=="bca"


    def testValidareCarte(self):
        val = Validare()
        c=Carte(1,"ion","frumos","rebreanu")
        try:
            val.validareCarte(c)
            assert True
        except:
            assert False

        c = Carte(1, "", "frumos", "rebreanu")
        try:
            val.validareCarte(c)
            assert False
        except:
            assert True

    def testValidareClient(self):
        val=Validare()
        c=Client(1,"ion","123")
        try:
            val.validareClient(c)
            assert True
        except:
            False

        c=Client(1,"ion","")
        try:
            val.validareClient(c)
            assert False
        except:
            assert True

    def testValideazaImprumut(self):
        pass

    def testSalveaza(self):
        open(self.__txtcr,"w")
        open(self.__txtcl,"w")
        open(self.__txtim,"w")
        repo = RepoCartef(self.__txtcr)
        c = Carte("1", "ion", "frumos", "rebeanu")
        repo.save(c)

        repc = repo.find("1")
        assert repc.getId() == c.getId()

        toate = repo.getAll()
        assert len(toate) == 1

        c = Carte("1", "ion", "frumos", "rebeanu")
        try:
            repo.save(c)
            assert False
        except:
            assert True

        c = Carte("2", "ion", "frumos", "rebeanu")
        repo.save(c)

        repo.update("2", "vasile", "urat", "geany")
        repc = repo.find("2")
        assert repc.getTitlu() == "vasile"
        toate = repo.getAll()
        assert len(toate) == 2

        repo.delete(c.getId())
        assert len(toate) == 1
        open(self.__txtcr,"w")
        repo=RepoCartef(self.__txtcr)
        c=Carte("1","ion","frumos","rebeanu")
        repo.save(c)


        repc=repo.find("1")
        assert repc.getId()==c.getId()

        toate=repo.getAll()
        assert len(toate)==1

        c=Carte("1","ion","frumos","rebeanu")
        try:
            repo.save(c)
            assert False
        except:
            assert True

        c = Carte("2", "ion", "frumos", "rebeanu")
        repo.save(c)

        repo.update("2","vasile","urat","geany")
        repc=repo.find("2")
        assert repc.getTitlu()=="vasile"
        toate=repo.getAll()
        assert len(toate)==2

        repo.delete(c.getId())
        assert len(toate)==1
        open(self.__txtcr,"w")


    def testSaveClient(self):
        repo=RepoClientf(self.__txtcl)
        c=Client("1","vasile","123")

        repo.save(c)
        toate=repo.getAll()

        assert len(toate)==1

        c = Client("1", "vasile", "")
        try:
            repo.save(c)
            assert False
        except:
            assert True

        repc=repo.find("1")
        assert repc.getNume()=="vasile"

        c=Client("2","tudor","234")
        repo.save(c)

        toate=repo.getAll()
        assert len(toate)==2

        repo.delete("2")

        toate = repo.getAll()
        assert len(toate) == 1

        repo.update("1","ionel","333")
        assert repo.getAll()[0].getNume()=="ionel"
        open(self.__txtcl,"w")

    def testSaveImprumut(self):
        repo=RepoImprumutf(self.__txtim)
        cr=Carte("1","baltagul","ok","sadoveanu")
        cr2=Carte("2","ion","naspa","rebreanu")
        cl=Client("1","ionel","1234567891111")
        cl2=Client("2","tudorel","2234567891111")
        im=Imprumut(cr,cl)
        try:
            repo.save(im)
            assert True
        except:
            assert False
        assert repo.getAll()[0].getCarte().getId()=="1"
        im=Imprumut(cr.getId(),cl2.getId())
        try:
            repo.save(im)
            assert False
        except:
            assert True
        im=Imprumut(cr2,cl2)
        repo.save(im)
        toate=repo.getAll()
        assert len(toate)==2
        repo.delete("2")
        toate = repo.getAll()
        assert len(toate) == 1
        try:
            repo.delete("3")
            assert False
        except:
            assert True
        open(self.__txtim,"w")




    def testCautareClient(self):
        serv=ServiceClient([],self.__txtcl)
        serv.adauga("1","ionas","8934444444444")
        gasit=serv.cautare("1")
        assert gasit.getNume()=="ionas"
        try:
            gasit=serv.cautare("2")
            assert False
        except:
            assert True
        open(self.__txtcl,"w")

    def testStergeClient(self):
        serv = ServiceClient([],self.__txtcl)
        try:
            serv.sterge(1)
            assert False
        except:
            assert True
        serv.adauga("1", "stefan", "1243444444444")
        assert len(serv.getClienti()) == 1
        serv.sterge("1")
        assert len(serv.getClienti()) == 0
        open(self.__txtcl,"w")


    def testAdaugaClient(self):
        serv = ServiceClient([],self.__txtcl)
        serv.adauga("1", "tudor", "1234444444444")
        assert len(serv.getClienti()) == 1
        try:
            serv.adauga("1", "tudor", "1234444444444")
            assert False
        except:
            assert True
        open(self.__txtcl,"w")


    def testCautareCarte(self):
        serv = ServiceCarte([],self.__txtcr)
        serv.adauga("1", "iona", "ok", "numaistiu")
        gasit = serv.cautare("1")
        assert gasit.getTitlu() == "iona"
        try:
            gasit = serv.cautare("2")
            assert False
        except:
            assert True
        open(self.__txtcr,"w")


    def testCautareCarteTitlu(self):
        open(self.__txtcr,"w")
        serv= ServiceCarte([],self.__txtcr)
        serv.adauga("1","ion","ok","liviut")
        kaki=serv.cautareTitlu("ion")
        assert kaki.getAutor()=="liviut"
        open(self.__txtcr,"w")


    def testModificaCarte(self):
        serv = ServiceCarte([],self.__txtcr)
        try:
            serv.actualizeaza(1, "a", "a", "a")
            assert False
        except:
            assert True
        serv.adauga("1", "maitreyi", "fain", "eliade")
        serv.actualizeaza("1", "meinkampf", ":(", "H")
        assert serv.getCarti()[0].getTitlu() == "meinkampf"
        open(self.__txtcr,"w")

    def testStergeCarte(self):
        serv = ServiceCarte([],self.__txtcr)
        try:
            serv.sterge(1)
            assert False
        except:
            assert True
        serv.adauga("1", "baltagul", "nasol", "sadoveanu")
        assert len(serv.getCarti()) == 1
        serv.sterge("1")
        assert len(serv.getCarti()) == 0
        open(self.__txtcr,"w")

    def testAdaugaCarte(self):
        serv = ServiceCarte([],self.__txtcr)
        serv.adauga("1", "baltagul", "nasol", "sadoveanu")
        assert len(serv.getCarti()) == 1
        try:
            serv.adauga("1", "baltagul", "nasol", "sadoveanu")
            assert False
        except:
            assert True
        open(self.__txtcr,"w")

    def testAdaugaImprumut(self):
        serv1=ServiceCarte([],self.__txtcr)
        serv2=ServiceClient([],self.__txtcl)
        serv=ServiceImprumut(self.__txtim)
        serv1.adauga("1","baltagul","ok","sadoveanu")
        serv2.adauga("1","ionel","1234444444444")
        serv.adauga(serv1.getCarti()[0],serv2.getClienti()[0])
        toate=serv.getImprumuturi()
        assert len(toate)==1
        serv.sterge("1")
        toate = serv.getImprumuturi()
        assert len(toate) == 0
        try:
            serv.sterge("2")
            assert False
        except:
            assert True
        open(self.__txtim,"w")

    def testReturnare(self):
        open(self.__txtcr,"w")
        open(self.__txtcl,"w")
        open(self.__txtim,"w")
        serv1 = ServiceCarte([],self.__txtcr)
        serv2 = ServiceClient([],self.__txtcl)
        serv = ServiceImprumut(self.__txtim)
        serv1.adauga("1", "baltagul", "ok", "sadoveanu")
        serv2.adauga("1", "ionel", "1234444444444")
        open(self.__txtim,"w")
        serv.adauga(serv1.getCarti()[0], serv2.getClienti()[0])
        assert serv.getImprumuturi()[0].getStare()=="True"
        serv.returneaza("1")
        assert serv.getImprumuturi()[0].getStare()=="False"
        open(self.__txtcr,"w")
        open(self.__txtcl,"w")
        open(self.__txtim,"w")

    def testRaportCeleMai(self):
        serv1 = ServiceCarte([],self.__txtcr)
        serv2 = ServiceClient([],self.__txtcl)
        serv = ServiceImprumut(self.__txtim)
        serv1.adauga("1", "baltagul", "ok", "sadoveanu")
        serv1.adauga("2", "baltagul", "ok", "sadoveanu")
        serv2.adauga("1", "ionel", "1234444444444")
        serv2.adauga("2", "ionel", "1234444444444")
        serv.adauga(serv1.getCarti()[0], serv2.getClienti()[0])
        serv.adauga(serv1.getCarti()[1], serv2.getClienti()[0])
        serv.returneaza("2")
        serv.adauga(serv1.getCarti()[1], serv2.getClienti()[1])
        rez=serv.celeMaiImprumutate()
        assert rez[0].getNumeCarte()=="baltagul"
        open(self.__txtcr,"w")
        open(self.__txtcl,"w")
        open(self.__txtim,"w")

    def testClientiOrdonati(self):
        serv1 = ServiceCarte([],self.__txtcr)
        serv2 = ServiceClient([],self.__txtcl)
        serv = ServiceImprumut(self.__txtim)
        serv1.adauga("1", "baltagul", "ok", "sadoveanu")
        serv1.adauga("2", "baltagul", "ok", "sadoveanu")
        serv2.adauga("1", "ionel", "1234444444444")
        serv2.adauga("2", "jonel", "1234444444444")
        serv2.adauga("3", "konel", "1234444444444")
        serv.adauga(serv1.getCarti()[0], serv2.getClienti()[0])
        serv.adauga(serv1.getCarti()[1], serv2.getClienti()[0])
        serv.returneaza("1")
        serv.returneaza("2")
        serv.adauga(serv1.getCarti()[0], serv2.getClienti()[1])
        serv.adauga(serv1.getCarti()[1], serv2.getClienti()[1])
        serv.returneaza("1")
        serv.adauga(serv1.getCarti()[0], serv2.getClienti()[2])
        rez=serv.clientiOrdonati()
        assert rez[0].getNumeClient()=="konel"
        open(self.__txtcr,"w")
        open(self.__txtcl,"w")
        open(self.__txtim,"w")

    def testClientiActivi(self):
        serv1 = ServiceCarte([],self.__txtcr)
        serv2 = ServiceClient([],self.__txtcl)
        serv = ServiceImprumut(self.__txtim)
        serv1.adauga("1", "baltagul", "ok", "sadoveanu")
        serv1.adauga("2", "baltagul", "ok", "sadoveanu")
        serv2.adauga("1", "ionel", "1234444444444")
        serv2.adauga("2", "jonel", "1234444444444")
        serv2.adauga("3", "konel", "1234444444444")
        serv.adauga(serv1.getCarti()[0], serv2.getClienti()[0])
        serv.adauga(serv1.getCarti()[1], serv2.getClienti()[0])
        serv.returneaza("1")
        serv.returneaza("2")
        serv.adauga(serv1.getCarti()[0], serv2.getClienti()[1])
        serv.adauga(serv1.getCarti()[1], serv2.getClienti()[1])
        serv.returneaza("1")
        serv.adauga(serv1.getCarti()[0], serv2.getClienti()[2])
        assert len(serv.getImprumuturi())==5
        rez = serv.clientiActivi()
        assert len(rez) == 0
        open(self.__txtcr,"w")
        open(self.__txtcl,"w")
        open(self.__txtim,"w")
        


class Teste:
    def __init__(self,txtcr,txtcl,txtim):
        self.__t=Test(txtcr,txtcl,txtim)
    def testare(self):
        self.__t.testSalveaza()
        self.__t.testSaveClient()
        self.__t.testCautareCarte()
        self.__t.testValidareCarte()
        self.__t.testValidareClient()
        self.__t.testCreeazaCarte()
        self.__t.testModificaCarte()
        self.__t.testStergeClient()
        self.__t.testCautareClient()
        self.__t.testAdaugaClient()
        self.__t.testAdaugaCarte()
        self.__t.testStergeCarte()
        self.__t.testSaveImprumut()
        self.__t.testValideazaImprumut()
        self.__t.testAdaugaImprumut()
        self.__t.testCautareCarteTitlu()
        self.__t.testReturnare()
        self.__t.testRaportCeleMai()
        self.__t.testClientiOrdonati()
        self.__t.testClientiActivi()