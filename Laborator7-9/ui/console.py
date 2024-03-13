from service.clientService import ClientService
from service.filmService import FilmService
import datetime


from service.inchiriereService import InchiriereService


class Console:
    def __init__(self, clientService: ClientService):
        self.__clientService=clientService

    def adaugaClient(self):
        try:
            idClient=input("Dati id-ul clientului: ")
            nume=input("Dati numele clientului: ")
            CNP=int(input("Dati CNP: "))
            self.__clientService.adaugaClient(idClient,nume,CNP)
        except KeyError as e:
            print(e)

    def modificaClient(self):
        try:
            idClient = input("Dati id-ul angajatului existent: ")
            numeNou = input("Dati numele nou al clientului: ")
            CNP=int(input("Dati CNP existent: "))
            self.__clientService.modificaClient(idClient, numeNou,CNP)
        except KeyError as e:
            print(e)
    def stergeClient(self):
        try:
            idClient = input("Dati id-ul angajatului existent: ")
            self.__clientService.stergeClient(idClient)
        except KeyError as e:
            print(e)

    '''def gaseste_client_nume(self,listaclienti):
        nume=input("nume:")
        for client in listaclienti:
            if nume==client.getNume():
                print(client)'''

    def cautare_clienti_nume(self,clienti):
        try:
            nume=input("Dati numele pe care il cautati: ")
            for client in clienti:
                if client.getNume().startswith(nume):
                    print(client)
            if client.getNume().startswith(nume) is not True:
                print("Nu exista acest nume!")
        except ValueError as ve:
            print(ve)

    def cautare_clienti_Cnp(self, clienti):
        cnp = input("Dati CNP pe care il cautati: ")
        for client in clienti:
            if str(client.getCnp()).startswith(cnp):
                print(client)


    def afiseaza(self,clienti):
        for client in clienti:
            print(client)
    def print_menu(self):
        print('\x1b[6;30;42m'+"1. Adauga client"+'\x1b[0m')
        print('\x1b[6;30;42m'+"2. Modifica client"+'\x1b[0m')
        print('\x1b[6;30;42m'+"3. Sterge client"+'\x1b[0m')
        print('\x1b[6;30;42m'+"4. Cautare client: "+'\x1b[0m')
        print('\x1b[6;30;42m'+"a. Afiseaza toti clientii"+'\x1b[0m')

        print('\x1b[6;30;42m'+"-> Continua"+'\x1b[0m')
    def meniu(self):
        try:
            while True:
                self.print_menu()
                optiune=input('\x1b[7;30;44m'"Dati optiunea: "+'\x1b[0m')
                if optiune=="1":
                   self.adaugaClient()
                elif optiune=="2":
                    self.modificaClient()
                elif optiune=="3":
                    self.stergeClient()
                elif optiune=="4":
                    print("1. Dupa nume:","\n"
                          "2. Dupa CNP:")
                    suboptiune=input("Dati suboptiunea: ")
                    if suboptiune=="1":
                        self.cautare_clienti_nume(self.__clientService.getAllClient())
                    elif suboptiune=="2":
                        self.cautare_clienti_Cnp(self.__clientService.getAllClient())
                elif optiune=="a":
                    self.afiseaza(self.__clientService.getAllClient())
                elif optiune=="":
                    break
                else:
                    print("Optiune gresita, reincercati!")
        except ValueError as ve:
            print(ve)
class ConsoleFilm:
    def __init__(self, filmService: FilmService, clientService: ClientService, inchiriereService:InchiriereService):
        self.__filmService=filmService
        self.__clientService = clientService
        self.__inchiriereService=inchiriereService


    def adaugaFilm(self):
        try:
            idFilm = input("Dati id-ul filmului: ")
            titlu= input("Dati titlul filmului: ")
            descriere= input("Dati descrierea filmului: ")
            gen= input("Dati genul filmului: ")
            self.__filmService.adaugaFilm(idFilm,titlu,descriere,gen)
        except KeyError as e:
            print(e)

    def modificaFilm(self):
        try:
            idFilm = input("Dati id-ul existent al filmului: ")
            titlu = input("Dati titlul nou a filmului: ")
            descriere = input("Dati descrierea noua a filmului: ")
            gen = input("Dati genul nou a filmului : ")
            self.__filmService.modificaFilm(idFilm,titlu,descriere,gen)
        except KeyError as e:
            print(e)

    def stergeFilm(self):
        try:
            idFilm = input("Dati id-ul filmului existent: ")
            self.__filmService.stergeFilm(idFilm)
        except KeyError as e:
            print(e)

    def cautare_filme_titlu(self, filme):
        try:
            titlu = input("Dati titlul pe care il cautati: ")
            for film in filme:
                if film.gettitlu().startswith(titlu):
                    print(film)
            if film.gettitlu().startswith(titlu) is not True:
                print("Nu exista acest titlu!")
        except KeyError as e:
            print(e)
    def cautare_filme_descriere(self, filme):
        descriere = input("Dati descrierea pe care o cautati: ")
        for film in filme:
            if film.getdescriere().startswith(descriere):
                print(film)
        if film.getdescriere().startswith(descriere) is not True:
            print("Nu exista aceasta descriere!")
    def cautare_filme_gen(self, filme):
        gen = input("Dati genul pe care il cautati: ")
        for film in filme:
            if film.getgen().startswith(gen):
                print(film)
        if film.getgen().startswith(gen) is not True:
            print("Nu exista acest gen!")

    def afiseaza(self, filme):
        for film in filme:
           print(film)

    def inchiriere_film(self,clienti,filme):
        try:
            found=False
            idInchiriere=input("Dati id-ul inchirerii: ")
            idClient=input("Dati id-ul dumneavoastra: ")
            idFilm=input("Dati id-ul filmului: ")
            for client in clienti:
                for film in filme:
                    if idClient==client.getIdClient() and idFilm==film.getIdFilm():
                            data_inc=datetime.datetime.utcnow()
                            data_retur=data_inc+datetime.timedelta((5-data_inc.weekday()%7))
                            #data_inc=data_inc.strftime("%d-%m-%Y %H:%M")
                            #data_retur = data_retur.strftime("%d-%m-%Y %H:%M")
                            self.__inchiriereService.adauga(idInchiriere,idClient,idFilm,data_inc,data_retur)
                            found=True
            if found is False:
                raise KeyError("Nu exista id-ul clientului sau a filmului ")
        except KeyError as ve:
            print(ve)
    def sterge_inre(self,inchirieri):
        try:
            idInchiriere=input("Dati id-ul inchirierii dumneavoastra: ")
            data_inc=str(datetime.datetime.utcnow())
           # data_inc = data_inc.strftime("%d-%m-%Y %H:%M")
            for inc in list(inchirieri):
                if idInchiriere==inc.getIdInchiriere():
                    da=inc.getdataret()
                   # da=da.strftime("%d-%m-%Y %H:%M")
                    if data_inc >= da:
                        self.__inchiriereService.sterge(idInchiriere)
                    else:
                        print("Nu s-a terminat perioada de inchiriere!")
        except KeyError as ve:
            print(ve)

    def mostRentedMovie(self):
        for film in self.__inchiriereService.maxInchiriereFilmId():
            print(film)


    def orderClientsByName(self):
        new_list = self.__inchiriereService.sortClientsByName()
        for e in new_list:
            print(e[1])

    def orderClientsByRentedMovie(self):
        new_list = self.__inchiriereService.sortClientsDupaNRFilme()
        for e in new_list:
            print(e[1])

    def mostActiveClients(self):
        for id_client in self.__inchiriereService.mostActiveClient():
            print(id_client[1])


    def afiseaza_inc(self,inchirieri):
        inchirieri=self.__inchiriereService.getAllInchiriere()
        for inc in inchirieri:
            print(inc)

    def print_menu2(self):
        print('\x1b[6;30;42m'+"1. Adauga film"+'\x1b[0m')
        print('\x1b[6;30;42m'+"2. Modifica film"+'\x1b[0m')
        print('\x1b[6;30;42m'+"3. Sterge film"+'\x1b[0m')
        print('\x1b[6;30;42m'+"4. Cautare film"+'\x1b[0m')
        print('\x1b[6;30;42m'+"5. Inchirire filme "+'\x1b[0m')
        print('\x1b[6;30;42m'+"6. Returneaza filme "+'\x1b[0m')
        print('\x1b[6;30;42m'+"7. Cel mai inchiriat film"+'\x1b[0m')
        print('\x1b[6;30;42m'+"8. Clientii ordonati dupa nume"+'\x1b[0m')
        print('\x1b[6;30;42m'+"9. Clientii ordonati dupa filmele inchiriate"+'\x1b[0m')
        print('\x1b[6;30;42m'+"10. Primi 20% clienti cu cele mai multe filme"+'\x1b[0m')
        print('\x1b[6;30;42m'+"a. Afiseaza toate filmele "+'\x1b[0m')
        print('\x1b[6;30;42m'+"i. Afiseaza toate inchirierile "+'\x1b[0m')
        print('\x1b[7;30;44m'+"x. Iesire"+'\x1b[0m')
    def meniu2(self):
        while True:
            self.print_menu2()
            optiune=input("Dati optiunea: ")
            if optiune=="1":
               self.adaugaFilm()
            elif optiune=="2":
                self.modificaFilm()
            elif optiune=="3":
                self.stergeFilm()
            elif optiune=="4":
                print("1.Cautare dupa titlu: ")
                print("2.Cautare dupa descriere: ")
                print("3.Cautare dupa gen: ")
                while True:
                    suboptiune=input("Dati suboptiunea:")
                    if suboptiune=="1":
                        self.cautare_filme_titlu(self.__filmService.getAllFilme())
                    elif suboptiune=="2":
                        self.cautare_filme_descriere(self.__filmService.getAllFilme())
                    elif suboptiune=="3":
                        self.cautare_filme_gen(self.__filmService.getAllFilme())
                    else:
                        print("Suboptiune gresita, reincercati!")
            elif optiune=="5":
                self.inchiriere_film(self.__clientService.getAllClient(),self.__filmService.getAllFilme())
            elif optiune=="6":
                self.sterge_inre(self.__inchiriereService.getAllInchiriere())
            elif optiune=="7":
                self.mostRentedMovie()
            elif optiune=="8":
                self.orderClientsByName()
            elif optiune=="9":
                self.orderClientsByRentedMovie()
            elif optiune=="10":
                self.mostActiveClients()
            elif optiune=="a":
                self.afiseaza(self.__filmService.getAllFilme())
            elif optiune=="i":
                self.afiseaza_inc(self.__inchiriereService.getAllInchiriere())
            elif optiune=="x":
                print('\x1b[6;30;44m' + "!Multumim ca ai folosit aplicatia noastra!" + '\x1b[0m')
                break
            else:
                print("Optiune gresita, reincercati!")

