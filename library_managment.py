from codecs import StreamWriter
from enum import Enum
from abc import ABC, abstractmethod
from unicodedata import name

class BookFormat(Enum):
  HARDCOVER, PAPERBACK, AUDIO_BOOK, EBOOK, NEWSPAPER, MAGAZINE, JOURNAL = 1, 2, 3, 4, 5, 6, 7


class BookStatus(Enum):
  AVAILABLE, RESERVED, LOANED, LOST = 1, 2, 3, 4

class ReservationStatus(Enum):
    WAITING, PENDING, CANCELED, NONE = 1, 2, 3, 4


class AccountStatus(Enum):
    ACTIVE, CLOSED, CANCELED, BLACKLISTED, NONE = 1, 2, 3, 4, 5


class Address(ABC):

    def __init__(self, street, city, state, zip_code, country) -> None:
       self.__street_address = street
       self.__city = city
       self.__state = state
       self.__zip_code = zip_code
       self.__country = country

class Person(ABC):
    def __init__(self, name, address, email, phone) -> None:
       self.__name = name
       self.__email = email
       self.__address = address
       self.__phone = phone

class Constants:
    def __init__(self) -> None:

        self.MAX_BOOKS_ISSUED_TO_A_USER = 5
        self.MAX_LENDIN_DAYS = 10

class Account(ABC):
  def __init__(self, id, password, person, status=AccountStatus.Active):
    self.__id = id
    self.__password = password
    self.__status = status
    self.__person = person

  def reset_password(self):
    None