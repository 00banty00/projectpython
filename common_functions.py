from dataclasses import dataclass


class car:
    def __init__(self,window,tyre,engine):
        self.window = window
        self.tyre = tyre
        self.engine = engine

    def driving(self):
        print("the engine is {}".format(self.engine))


nexon = car(6,5,"petrol")

nexon.driving()



@dataclass
class Person:
    name:str
    age:int

@dataclass
class Employee(Person):
    department:str
    detail:Person

person1 = Person("kumar",30)
person1.age
emp1 = Employee("DE",12,"abc","m")

emp1.name
emp1.age
emp1.detail.age



@dataclass
class Address:
    street:str
    city:str
    zip_code:int


@dataclass
class Employee():
    name:str
    age:int
    address:Address


address = Address("ABC street","patna",801105)

emp = Employee("st1","patna",12345,"Manish",30,address)

emp2 = Employee("Manish",30,address)

emp2.address.city



class laptop:
    def __init__(self,keyboard,mouse,cpu):
        self.keyboard = keyboard
        self.mouse = mouse
        self.cpu = cpu

    def display_info(self):
        print(F"the laptop has {self.keyboard}, {self.mouse} and {self.cpu}")


macbook = laptop("big keyboard","touch mouse","M1 Chip")

macbook.display_info()
macbook.cpu




# Logging 

"""
this is used to log error
"""


# basicConfig(**kwargs) method:
"""
this is used to config the logging system.

1. file name
2. filemode: a- append, w- write
3. level: 
4. Format:
5. datefmt:
"""

# getLoggger():- this returns a logger with the specified name or, if name is none, return a logger which is the root logger of the hirearchy

"""
info(msg) - this will log a msg with level INFO on this logger

warning(msg) - this will log a msg with level WARNING on this logger

error(msg) - this will log a msg with level ERROR on this logger

critical(msg) - this will log a msg with level CRITICAL on this logger

exception(msg) - this will log a msg with level EXCEPTION on this logger

"""

from logging import *

log_format = "%(asctime)s // %(message)s // %(lineno)d"
basicConfig(filename= 'runlog.log',level=debug,filemode='w',format=log_format)
logger = getLogger('chandan')

logger.debug("this is debug")
logger.info("this is info")
logger.warning("this is warning")
logger.error("this is error")
critical("this is critical")






