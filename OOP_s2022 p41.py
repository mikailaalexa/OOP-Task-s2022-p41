class Balloon:
    def __init__(self, Colour, DefenceItem):
        self.__Health = 100
        self.__Colour = Colour
        self.__DefenceItem = DefenceItem

    def GetDefenceItem(self):
        return self.__DefenceItem

    def ChangeHealth(self, change):
        self.__Health += change

    def CheckHealth(self):
        if self.__Health >= 0:
            return True
        else:
            return False


def Defend(objBalloon):
    strength = int(input("Enter strength of opponent: "))
    objBalloon.ChangeHealth(-strength)

    print("You defended with", objBalloon.GetDefenceItem())

    if objBalloon.CheckHealth() == True:
        print("Health remaining")
    else:
        print("No remaining health")

    return objBalloon


DefenceItem = input("Enter Defence Item: ")
colour = input("Enter colour: ")

Balloon1 = Balloon(colour, DefenceItem)

obj = Defend(Balloon1)
