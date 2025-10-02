class Match:
    def __init__(self,name1,name2):
        self.name1 = name1
        self.name2 = name2
    def person(self):
        n1 = self.name1.replace(" ","").lower()
        n2 = self.name2.replace(" ","").lower()
        
        for ch in n1:
            if ch in n2:
                n1 = self.name1.replace(ch,"")
                n2 = self.name2.replace(ch,"")

                count = len(n1) + len(n2)
                if count == 0:
                    return f"Not Compatible. Single forever </3"

                Flames = ["Friendship","Love","Affection","Marriage","Enemy","Sibling"]
                index = 0
                if len(Flames) > 1:
                    index = (index + count - 1) % len(Flames)
                    Flames.pop(index)
                    
                    return Flames[0]
Enter1 = input("Enter your name:\t")
Enter2 = input("Enter crush's name:\t")

a = Match(Enter1,Enter2)

print(f"Relationship:\t{a.person()}")
