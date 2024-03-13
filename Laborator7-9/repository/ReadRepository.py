import datetime

from Domain.filme import Filme
from Domain.client import Client
from Domain.inchiriere import Inchiriere
from repository.repository import Repository

class FilmeReadRepository(Repository):
    def __init__(self, file_name):
        super().__init__()
        self.__file_name = file_name
        self.__load_data()


    def adauga(self, film):
        super().adauga(film)
        self.save()

    def modifica(self, film):
        super().modifica(film)
        self.save()

    def sterge(self, film):
        super().sterge(film)
        self.save()
    def __load_data(self):
        with open(self.__file_name) as f:
            lc = []
            for line in f:
                ls = line.strip()
                lc.append(ls)
            try:
                for i in range(0,len(lc)):
                    array=lc[i].split(',')
                    crt = Filme(array[0],array[1],array[2],array[3])
                    super().adauga(crt)
            except IndexError as ie:
                print('\x1b[6;30;41m' + "!Eroare la incarcarea datelor dumneavoastra!" + '\x1b[0m')

    def save(self):
        f = open(self.__file_name, "w")
        lista_filme = super().getAll()
        for film in lista_filme:
            id = film.getIdFilm()
            titlu = film.gettitlu()
            descriere = film.getdescriere()
            gen=film.getgen()
            linie = str(id) + "," + titlu + "," + descriere+","+gen+ "\n"
            f.write(linie)
        f.close()
    def save_memory(self, film):
        super().adauga(film)


class ClientiReadRepository(Repository):
    try:
        print('\x1b[7;30;44m'+"______Welcome to the movie. Please sign in!_____"+'\x1b[0m')
        def __init__(self, file_name):
            super().__init__()
            self.__file_name = file_name
            self.__load_data()
        def adauga(self,client):
            super().adauga(client)
            self.save()
        def modifica(self,client):
            super().modifica(client)
            self.save()
        def sterge(self, client):
            super().sterge(client)
            self.save()
        def __load_data(self):
            try:
                with open(self.__file_name) as f:
                    lc = []
                    for line in f:
                        ls = line.strip()
                        lc.append(ls)
                    try:
                        for i in range(0, len(lc)):
                            array = lc[i].split(',')
                            crt = Client(array[0], array[1], array[2])
                            super().adauga(crt)
                    except IndexError as ie:
                        print('\x1b[6;30;41m' + "!Eroare la incarcarea datelor dumneavoastra!" + '\x1b[0m')

            except IOError:
                print("Eroare la deschiderea fisierului"+self.__file_name)
    except ValueError as ve:
        print(ve)

    def save(self):
        f=open(self.__file_name,"w")
        lista_clienti=super().getAll()
        for client in lista_clienti:
            id=client.getIdClient()
            nume=client.getNume()
            cnp=client.getCnp()
            linie=str(id)+","+nume+","+str(cnp)+"\n"
            f.write(linie)
        f.close()

    def save_memory(self, client):
        super().adauga(client)
class InchirieriReadRepository(Repository):

    def __init__(self,file_name):
        super().__init__()
        self.__file_name=file_name
        self.__load_data()

    def adauga(self, inc):
        super().adauga(inc)
        self.save()

    def modifica(self, inchiriere):
        super().modifica(inchiriere)
        self.save()

    def sterge(self, inchiriere):
        super().sterge(inchiriere)
        self.save()
    def __load_data(self):
        with open(self.__file_name) as f:
            lc = []
            for line in f:
                ls = line.strip()
                lc.append(ls)
            try:
                for i in range(0, len(lc)):
                    array = lc[i].split(',')
                    crt = Inchiriere(array[0], array[1], array[2],array[3],array[4])
                    super().adauga(crt)
            except IndexError as ie:
                print('\x1b[7;30;44m' + "!Eroare la incarcarea datelor dumneavoastra!" + '\x1b[0m')
    def save(self):
        f = open(self.__file_name, "w")
        lista_inchirieri = super().getAll()
        for inc in lista_inchirieri:
            idInchirere=inc.getIdInchiriere()
            idClient = inc.getIdClient()
            idFilm =inc.getIdFilm()
            data_inc = datetime.datetime.utcnow()
            data2=data_inc+datetime.timedelta((5-data_inc.weekday()%7))
            linie = str(idInchirere) + "," + str(idClient) + "," + str(idFilm) +","+str(data_inc)+","+str(data2)+"\n"
            f.write(linie)
        f.close()
