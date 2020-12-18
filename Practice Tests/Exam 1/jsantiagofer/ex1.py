# (a)
super_athletes =  BaseballPlayers.union(BasketBallPlayers.union(FootballPlayers)) 

# (b)
True if (FootballPlayers.union(BaseballPlayers)).isEmpty() else False

# (c)
True if (FootballPlayers.union(BasketBallPlayers)).isMember("Tom") is True and BaseballPlayers.isMember("Tom") is False else False

# (d)
True if L.first_index(X) != L.last_index(X) else False

# (e)
Bag<Integer> B1 = new StaticBag<Integer>(10)
Bag<Integer> B2  = new DynamicBag<Integer>(10)
B1 = (StaticBag)B2

''' 
*** Error in Third Line of code? 
* I do not think there is an error since the difference between the static bag and dynamic bag is that
* the static bag has a MAX_SIZE, while the dynamic bag does not. However, since they both have the same
* initial size (10), it is possible to convert from dynamic to static. Additionally, they also share the same 
* ' Father ' class or interface (BAG). I am only unsure if this conversion can be done with this much ease
* (through a parenthesis operation)
***
'''