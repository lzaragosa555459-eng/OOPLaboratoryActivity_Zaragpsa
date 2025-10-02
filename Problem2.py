import random


class roll:
    def __init__(self,Player,Winning):
        self.Player = Player
        self.Winning = Winning
    def match(self):
        getMatch = set(self.Player) & set (self.Winning)
        count = len(getMatch)

        print("Winning Number:",self.Winning)
        print("Player Number:",self.Player)
        print("Matches:",count)
        if count == 6:
            prize = 1000000
            print(f"Prize: P{prize:,} (Jackpot)")
        else:
            prize = count * 1000
            print(f"Prize: P{prize:,}")


Enter = list(map(int, input("Enter your six numbers: ").split()))


random1 = random.randint(1,60)
random2 = random.randint(1,60)
random3 = random.randint(1,60)
random4 = random.randint(1,60)
random5 = random.randint(1,60)
random6 = random.randint(1,60)


list_random = [random1,random2,random3,random4,random5,random6]
a = roll(Enter,list_random)
print(a.match())
