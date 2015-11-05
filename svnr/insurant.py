from random import randint
import string


class Insurant:
    def __init__(self):
        self.birthdate = ""
        self.surname = ""
        self.sex = True
        self.area_number = "09"
        self.serial_number = ""
        self.number = ""
        self.letter_position = ""
        self.string = ""

    def set_birthdate(self, birthdate):
        self.birthdate = birthdate

    def set_surname(self, surname):
        self.surname = surname
        self.set_letter_position()

    def set_sex(self, sex):
        if sex == "m":
            self.sex = True
        elif sex == "w":
            self.sex = False
        self.set_serial_number()

    def set_serial_number(self):
        if self.sex:
            self.serial_number = randint(0, 49)
        else:
            self.serial_number = randint(50, 99)
        if self.serial_number < 10:
            self.serial_number = "0" + str(self.serial_number)

    def extract_date(self):
        day = self.birthdate[:2]
        month = self.birthdate[3:5]
        year = self.birthdate[8:]
        date = [day, month, year]
        return date

    def build_number(self):
        date = self.extract_date()
        self.number = self.area_number + date[0] + date[1] + date[2] + str(self.letter_position) + '{}'.format(
            self.serial_number)

    def build_string(self):
        date = self.extract_date()
        self.string = self.area_number + date[0] + date[1] + date[2] + self.surname[:1] + '{}'.format(
            self.serial_number)

    def set_letter_position(self):
        if self.surname[:1].isupper():
            self.letter_position = string.ascii_uppercase.index(self.surname[:1]) + 1
        else:
            self.letter_position = string.ascii_lowercase.index(self.surname[:1]) + 1
        if self.letter_position < 10:
            self.letter_position = "0" + str(self.letter_position)


def calculate_weighting(number):
    number = [int(i) for i in str(number)]
    weighting = [2, 1, 2, 5, 7, 1, 2, 1, 2, 1, 2, 1]
    number = [a * b for a, b in zip(number, weighting)]
    number = int(''.join(map(str, number)))
    return number


def calculate_cross_sum(number):
    number = int(number)
    qs = 0
    while number:
        qs += number % 10
        number //= 10
    return qs


def calculate_checksum(number):
    number %= 10
    return number