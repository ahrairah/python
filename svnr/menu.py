# -*- coding: iso-8859-1 -*-
import sys, os
from insurant import Insurant, calculate_cross_sum, calculate_checksum, calculate_weighting


class Menu:
    def __init__(self):
        self.insurant = Insurant()
        self.insurance_numbers = []
        self.choices = {
            "1": self.generate_insurance_number,
            "2": self.show_insurance_numbers,
            "3": self.write_file,
            "4": self.quit
        }

    def display_menu(self):
        print("""Was möchten Sie tun?
        1. Neue Rentenversicherungsnummer generieren
        2. Bereits erstellte Nummern anzeigen
        3. RVNr in Datei schreiben
        4. Programm beenden
        Einfach die entsprechende Nummer angeben.
        """)

    def run(self):
        while True:
            self.display_menu()
            choice = input("Wählen Sie bitte: ")
            action = self.choices.get(choice)
            if action:
                action()
            else:
                print("Diese Option existiert nicht. ".format(choice))

    def quit(self):
        print("Vielen Dank, dass Sie den RvNr-Generator verwendet haben.")
        sys.exit(0)

    def generate_insurance_number(self):
        birthdate = input("Bitte das Geburtsdatum eingeben (TT.MM.YYYY). ")
        self.insurant.set_birthdate(birthdate)
        sex = input("Wählen Sie das Geschlecht. Geben Sie m für mönnlich und w für weiblich ein. ")
        self.insurant.set_sex(sex)
        surname = input("Bitte geben Sie den Namen ein. ")
        self.insurant.set_surname(surname)
        self.insurant.build_number()
        self.insurant.build_string()
        checksum = calculate_checksum(calculate_cross_sum(calculate_weighting(self.insurant.number)))
        insurance_number = self.insurant.string + str(checksum)
        self.insurance_numbers.append(insurance_number)
        print("Die Rentenversicherungsnummer lautet: " + insurance_number)

    def show_insurance_numbers(self):
        print(self.insurance_numbers)

    def check_path(self, path):
        if os.access(path, os.F_OK):
            if os.access(path, os.W_OK):
                return True
            else:
                print("Sie besitzen nicht die nötigen Schreibrechte für das Verzeichnis.")
                return False
        else:
            createDir = input("Das Verzeichnis existiert nicht.\nSoll es angelegt werden? j/n ")
            if createDir == "j":
                os.mkdir(path)
                return True
            return False

    def write_file(self):
        path = input("Bitte geben Sie den Pfad an, in dem die Datei abgelegt werden soll. ")
        if self.check_path(path):
            file = open('{0}/myfile.txt'.format(path), 'w+')
            for insurance_number in self.insurance_numbers:
                file.write(insurance_number + "\n")
            file.close()
        else:
            print("\nAuf den Pfad: {0} kann nicht zugegriffen werden.\n".format(path))




if __name__ == "__main__":
    Menu().run()
