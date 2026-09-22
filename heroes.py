from abc import ABC
from interfaces import IFly


class Being(ABC):
    pass


class SuperHero(Being):
    pass


class HumanHero(SuperHero):
    pass


class Batman(HumanHero, IFly):
    def fly(self):
        print("I am flying with my bat wings")

    def land(self):
        print("I am landing with my bat wings")

    def super_intelligence(self):
        print("I am using my intelligence to beat you")