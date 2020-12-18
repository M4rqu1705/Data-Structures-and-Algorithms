#!/usr/bin/env python
# -*- coding: utf-8 -*-

def partA(BaseballPlayers, BasketballPlayers, FootballPlayers):
    # deportistas = BaseballPlayers.intersection(BasketballPlayers.intersection(FootballPlayers))
    return BaseballPlayers.intersection(BasketballPlayers.intersection(FootballPlayers))

def partB(BaseballPlayers, BasketballPlayers, FootballPlayers):
    # FootballPlayers.intersection(BasketballPlayers).isEmpty()
    return len(FootballPlayers.intersection(BasketballPlayers)) == 0

def partC(BaseballPlayers, BasketballPlayers, FootballPlayers):
    # FootballPlayers.union(BasketballPlayers).difference(BaseballPlayers).contains("Tom")
    # OR
    # FootballPlayers.union(BasketballPlayers).contains("Tom") && !BaseballPlayers.contains("Tom")

    return "Tom" in FootballPlayers.union(BasketballPlayers).difference(BaseballPlayers)

def partD(L, X):
    # If the first index of the element is the same as the last, the element appears just once
    # L.fistIndex(X) != L.lastIndex(X)
    return L.index(X) != len(L) - 1 - L[::-1].index(X)

def partE(B1, B2):
    # There are no errors in the 3rd line of the code since B2 has as much capacity as the dynamic bag
    # Additionally, the DynamicBag was implemented with the static bag through object composition. However, the DynamicBag had additional criteria for the add add method, and such.
    return False


# My tests
if __name__ == "__main__":
    BkP = {"Joe", "Molly", "Tom"}
    BbP = {"Joe", "Robin"}
    FbP = {"Joe", "John", "Holly", "Tom"}

    print("All the players that practice EVERY sport are:")
    print(partA(BbP, BkP, FbP))
    print()

    print("Is the set of students that practice BOTH Football and Basketball empty?")
    print(partB(BbP, BkP, FbP))
    print()

    print("Is 'Tom' playing both football and basketball, but not baseball?")
    print(partC(BbP, BkP, FbP))
    print()

    L = [1,2,3,4,5,4]
    print(f"Is '1' repeated?: {partD(L, 1)}")
    print(f"Is '4' repeated?: {partD(L, 4)}")
