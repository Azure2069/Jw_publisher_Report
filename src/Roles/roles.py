from enum import Enum

class Roles(str, Enum):
    elder = "elder"
    publisher = "publisher"
    regular_pioneer = "regular pioneer"
    auxiliary_pioneer = "auxiliary pioneer"
    pioneer_elder="pioneer_elder"
    admin="admin"


class Gender(str, Enum):
    male="male"
    female="female"


def add():
    pass