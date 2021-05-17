'''
Created on Nov 30, 2020

@author: matei
'''
from entitati import Carte,Client,Imprumut,Raport
from validator import Validare
#from repository import RepoCarte,RepoClient,RepoImprumut
from repositoryF import RepoCarte,RepoClient,RepoImprumut
from repositoryFmos import RepoCartef,RepoClientf,RepoImprumutf 
from service import ServiceCarte,ServiceClient,ServiceImprumut
import unittest
from dunno import error_titlu, error_cnp, error_save, error_delete, error_find,\
    error_update
from _ast import Expression
class Teste(unittest.TestCase):
    def setUp(self):
        unittest.TestCase.setUp(self)
        self.__txtCr="txtcr.txt"
        self.__txtCl="txtcl.txt"
        self.__txtIm="txtim.txt"
        self.fiscr=open(self.__txtCr,"w")
        self.fiscl=open(self.__txtCl,"w")
        self.fisim=open(self.__txtIm,"w")
        self.repoCarte=RepoCartef(self.__txtCr)
        self.repoClient=RepoClientf(self.__txtCl)
        self.repoImprumut=RepoImprumutf(self.__txtIm)
        self.serviceCarte=ServiceCarte([],self.__txtCr)
        self.serviceClient=ServiceClient([],self.__txtCl)
        self.serviceImprumut=ServiceImprumut(self.__txtIm)
        self.__val=Validare()
        self.cr=Carte("1","abc","cab","bca")
        self.cl=Client("1","ion","1111111111111")
        
        
    def tearDown(self):
        unittest.TestCase.tearDown(self)
        self.fiscr.close()
        self.fiscl.close()
        self.fisim.close()
    
    
    def assertNotRaises(self,exception,expression):
        raised=False
        try:
            expression
        except exception:
            raised=True
        self.assertEqual(raised, False)
            
    
    def testCreeazaCarte(self):
        self.assertEqual(self.cr.getId(), "1", "verificam daca id-ul")
        self.assertEqual(self.cr.getTitlu(), "abc", "verificam titlul")
        self.assertEqual(self.cr.getDescriere(), "cab", "verificam descrierea")
        self.assertEqual(self.cr.getAutor(), "bca", "verificam autorul")
        
        
    def testValidareCarte(self):
        self.__val.validareCarte(self.cr)
        self.cr = Carte("1", "", "frumos", "rebreanu")
        with self.assertRaises(error_titlu):
            self.__val.validareCarte(self.cr)
    
    
    def testValidareClient(self):
        self.__val.validareClient(self.cl)
        self.cl=Client("1","ion","")
        with self.assertRaises(error_cnp):
            self.__val.validareClient(self.cl)
        
        
    def testValidareImprumut(self):
        pass
    
    
    def testSalveaza(self):
        self.repoCarte.save(self.cr)
        repc=self.repoCarte.find("1")
        self.assertEqual(repc.getId(), self.cr.getId(), "verificam daca id-urile sunt egale")
        toate=self.repoCarte.getAll()
        self.assertEqual(len(toate), 1, "verificam lungimea")
        with self.assertRaises(error_save):
            self.repoCarte.save(self.cr)
        self.cr=Carte("2", "ion", "frumos", "rebeanu")
        self.repoCarte.save(self.cr)
        self.repoCarte.update("2", "vasile", "urat", "geany")
        repc = self.repoCarte.find("2")
        self.assertEqual(repc.getTitlu(), "vasile", "verificam titlul")
        toate = self.repoCarte.getAll()
        self.assertEqual(len(toate), 2, "verificam lungimea")
        self.repoCarte.delete(self.cr.getId())
        self.assertEqual(len(toate), 1, "verificam lungimea")
        self.repoCarte.update("1", "ion", "frumos", "rebeanu")
        repc=self.repoCarte.find("1")
        self.assertEqual(repc.getDescriere(), "frumos", "verificam descrierea")
    
    def testSaveClient(self):
        self.repoClient.save(self.cl)
        toate=self.repoClient.getAll()
        self.assertEqual(len(toate), 1, "verificam lungimea")
        self.cl=Client("1","vasile","")
        with self.assertRaises(error_save):
            self.repoClient.save(self.cl)
        repc=self.repoClient.find("1")
        self.assertEqual(repc.getNume(), "ion", "verificam numele")
        self.cl=Client("2","tudor","234")
        self.repoClient.save(self.cl)
        toate=self.repoClient.getAll()
        self.assertEqual(len(toate), 2, "verificam lungimea")
        self.repoClient.delete("2")
        toate=self.repoClient.getAll()
        self.assertEqual(len(toate), 1, "verificam lungimea")
        self.repoClient.update("1","ionel","333")
        self.assertEqual(self.repoClient.getAll()[0].getNume(), "ionel", "verificam numele")
    
    
    def testSaveImprumut(self):
        cr=Carte("1","baltagul","ok","sadoveanu")
        cr2=Carte("2","ion","naspa","rebreanu")
        cl=Client("1","ionel","1234567891111")
        cl2=Client("2","tudorel","2234567891111")
        im=Imprumut(cr,cl)
        self.repoImprumut.save(im)
        self.assertEqual(self.repoImprumut.getAll()[0].getCarte().getId(), "1", "verificam id-ul")
        with self.assertRaises(error_save):
            self.repoImprumut.save(im)
        im=Imprumut(cr2,cl2)
        self.repoImprumut.save(im)
        toate=self.repoImprumut.getAll()
        self.assertEqual(len(toate), 2, "verificam lungimea")
        self.repoImprumut.delete("2")
        toate=self.repoImprumut.getAll()
        self.assertEqual(len(toate), 1, "verificam lungimea")
        with self.assertRaises(error_delete):
            self.repoImprumut.delete("3")
    
    
    def testCautareClient(self):
        self.serviceClient.adauga("1","ionas","8934444444444")
        gasit=self.serviceClient.cautare("1")
        self.assertEqual(gasit.getNume(), "ionas", "verificam numele")
        with self.assertRaises(error_find):
            gasit=self.serviceClient.cautare("2")
            
    
    def testStergeClient(self):
        with self.assertRaises(error_delete):
            self.serviceClient.sterge("1")
        self.serviceClient.adauga("1","stefan","1243444444444")
        self.assertEqual(len(self.serviceClient.getClienti()), 1, "verificam lungimea")
        self.serviceClient.sterge("1")
        self.assertEqual(len(self.serviceClient.getClienti()), 0, "verificam lungimea")
    
    
    def testAdaugaClient(self):
        self.serviceClient.adauga("1", "tudor", "1234444444444")
        self.assertEqual(len(self.serviceClient.getClienti()), 1, "verificam lungimea")
        with self.assertRaises(error_save):
            self.serviceClient.adauga("1", "tudor", "1234444444444")
        
    
    def testCautareCarte(self):
        self.serviceCarte.adauga("1", "iona", "ok", "numaistiu")  
        gasit=self.serviceCarte.cautare("1")
        self.assertEqual(gasit.getTitlu(), "iona", "verificam titlul")
        with self.assertRaises(error_find):
            self.serviceCarte.cautare("2")
    
    
    def testCautareCarteTitlu(self):
        self.serviceCarte.adauga("1","ion","ok","liviut")
        kaki=self.serviceCarte.cautareTitlu("ion")
        self.assertEqual(kaki.getAutor(), "liviut", "verificam autorul")
        
        
    def testModificareCarte(self):
        with self.assertRaises(error_update):
            self.serviceCarte.actualizeaza(1, "a", "a", "a")
        self.serviceCarte.adauga("1", "maitreyi", "fain", "eliade")
        self.serviceCarte.actualizeaza("1", "meinkampf", ":(", "H")
        self.assertEqual(self.serviceCarte.getCarti()[0].getTitlu(), "meinkampf", "verificam titlul")
    
    
    def testStergeCarte(self):
        with self.assertRaises(error_delete):
            self.serviceCarte.sterge("1")
        self.serviceCarte.adauga("1", "baltagul", "nasol", "sadoveanu")
        self.assertEqual(len(self.serviceCarte.getCarti()), 1, "verificam lungimea")
        self.serviceCarte.sterge("1")
        self.assertEqual(len(self.serviceCarte.getCarti()), 0, "verificam lungimea")
    
    
    def testAdaugaCarte(self):
        self.serviceCarte.adauga("1", "baltagul", "nasol", "sadoveanu")
        self.assertEqual(len(self.serviceCarte.getCarti()),1,"verificam lungimea")
        with self.assertRaises(error_save):
            self.serviceCarte.adauga("1", "baltagul", "nasol", "sadoveanu")
    
    
    def testAdaugaImprumut(self):
        self.serviceCarte.adauga("1","baltagul","ok","sadoveanu")
        self.serviceClient.adauga("1","ionel","1234444444444")
        self.serviceImprumut.adauga(self.serviceCarte.getCarti()[0],self.serviceClient.getClienti()[0])
        self.assertEqual(len(self.serviceImprumut.getImprumuturi()), 1, "verificam lungimea")
        with self.assertRaises(error_save):
            self.serviceImprumut.adauga(self.serviceCarte.getCarti()[0],self.serviceClient.getClienti()[0])
        self.serviceImprumut.sterge("1")
        self.assertEqual(len(self.serviceImprumut.getImprumuturi()), 0, "verificam lungimea")
        with self.assertRaises(error_delete):
            self.serviceImprumut.sterge("2")
            
            
    def testReturnare(self):
        self.serviceCarte.adauga("1", "baltagul", "ok", "sadoveanu")
        self.serviceClient.adauga("1", "ionel", "1234444444444")
        self.serviceImprumut.adauga(self.serviceCarte.getCarti()[0], self.serviceClient.getClienti()[0])
        self.assertEqual(self.serviceImprumut.getImprumuturi()[0].getStare(), "True", "verificam starea")
        self.serviceImprumut.returneaza("1")
        self.assertEqual(self.serviceImprumut.getImprumuturi()[0].getStare(), "False", "verificam starea")
    
    
    def testRaportCeleMai(self):
        self.serviceCarte.adauga("1", "baltagul", "ok", "sadoveanu")
        self.serviceCarte.adauga("2", "baltagul", "ok", "sadoveanu")
        self.serviceClient.adauga("1", "ionel", "1234444444444")
        self.serviceClient.adauga("2", "ionel", "1234444444444")
        self.serviceImprumut.adauga(self.serviceCarte.getCarti()[0], self.serviceClient.getClienti()[0])
        self.serviceImprumut.adauga(self.serviceCarte.getCarti()[1], self.serviceClient.getClienti()[0])
        self.serviceImprumut.returneaza("2")
        self.serviceImprumut.adauga(self.serviceCarte.getCarti()[1], self.serviceClient.getClienti()[1])
        rez=self.serviceImprumut.celeMaiImprumutate()
        self.assertEqual(rez[0].getNumeCarte(), "baltagul", "verificam titlul cartii")
    
    
    def testClientiOrdonati(self):
        self.serviceCarte.adauga("1", "baltagul", "ok", "sadoveanu")
        self.serviceCarte.adauga("2", "baltagul", "ok", "sadoveanu")
        self.serviceClient.adauga("1", "ionel", "1234444444444")
        self.serviceClient.adauga("2", "jonel", "1234444444444")
        self.serviceClient.adauga("3", "konel", "1234444444444")
        self.serviceImprumut.adauga(self.serviceCarte.getCarti()[0], self.serviceClient.getClienti()[0])
        self.serviceImprumut.adauga(self.serviceCarte.getCarti()[1], self.serviceClient.getClienti()[0])
        self.serviceImprumut.returneaza("1")
        self.serviceImprumut.returneaza("2")
        self.serviceImprumut.adauga(self.serviceCarte.getCarti()[0], self.serviceClient.getClienti()[1])
        self.serviceImprumut.adauga(self.serviceCarte.getCarti()[1], self.serviceClient.getClienti()[1])
        self.serviceImprumut.returneaza("1")
        self.serviceImprumut.adauga(self.serviceCarte.getCarti()[0], self.serviceClient.getClienti()[2])
        rez=self.serviceImprumut.clientiOrdonati()
        self.assertEqual(rez[0].getNumeClient(), "konel", "verificam numele clientului")
    
    
    def testClientiActivi(self):
        self.serviceCarte.adauga("1", "baltagul", "ok", "sadoveanu")
        self.serviceCarte.adauga("2", "baltagul", "ok", "sadoveanu")
        self.serviceClient.adauga("1", "ionel", "1234444444444")
        self.serviceClient.adauga("2", "jonel", "1234444444444")
        self.serviceClient.adauga("3", "konel", "1234444444444")
        self.serviceImprumut.adauga(self.serviceCarte.getCarti()[0], self.serviceClient.getClienti()[0])
        self.serviceImprumut.adauga(self.serviceCarte.getCarti()[1], self.serviceClient.getClienti()[0])
        self.serviceImprumut.returneaza("1")
        self.serviceImprumut.returneaza("2")
        self.serviceImprumut.adauga(self.serviceCarte.getCarti()[0], self.serviceClient.getClienti()[1])
        self.serviceImprumut.adauga(self.serviceCarte.getCarti()[1], self.serviceClient.getClienti()[1])
        self.serviceImprumut.returneaza("1")
        self.serviceImprumut.adauga(self.serviceCarte.getCarti()[0], self.serviceClient.getClienti()[2])
        self.assertEqual(len(self.serviceImprumut.getImprumuturi()), 5, "verificam lungimea")
        rez=self.serviceImprumut.clientiActivi()
        self.assertEqual(len(rez), 0, "verificam lungimea")
        
        
        
        
        
        
        