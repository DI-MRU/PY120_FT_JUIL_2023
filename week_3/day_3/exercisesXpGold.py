class Character:
    def __init__(self, name) -> None:
        self.name = name
        self.life = 70
        self.attack = 20
    
    def basic_attack(self, other_class):
        print(f"{self.name} attacks {other_class.name}\n")
        other_class.life -= 5
        
class Support(Character):
    def __init__(self, name) -> None:
        super().__init__(name)

    def rest(self):
        print(f"{self.name} rested, HP +10 ATK - 2\n")
        self.life += 10
        self.attack -= 2

    def animal_help(self):
        self.attack += 5
        print(f"{self.name} receives Backup, ATK +5\n")
    
    def slash(self, other_class):
        dmg = int(0.75 * self.life + 0.75 * self.attack)
        other_class.life -= dmg
        print(f"{self.name} used slashed again {other_class.name}")

class Warrior(Character):
    def __init__(self, name) -> None:
        super().__init__(name)

    def life_steal(self, other_class):
        other_class.life -= 2 * self.attack
        self.life += 0.5 * self.attack
        print(f"{self.name} stole {other_class.name}'s HP and afflicted Dmg, HP Increase\n")

    def berserk(self):
        self.attack += 2
        self.life += 2
        print(f"{self.name} went berserk ATK +2, HP +2\n")
    
    def roar(self, other_class):
        other_class.attack -= 3
        print(f"{other_class.name} was intimidated. ATK -3\n")

class Mage(Character):
    def __init__(self, name) -> None:
        super().__init__(name)

    def fire_ball(self, other_class):
        other_class.life -= 12
        print(f"{other_class.name} got burnt HP -12\n")

    def summon(self, other_class):
        other_class.life -= 5
        print(f"{self.name} summoned a undead troops\n")

    def wisdom(self):
        self.attack += 5
        print(f"{self.name} used wisdom ATK +5\n")

class Assassin(Character):
    def __init__(self, name) -> None:
        super().__init__(name)
    
    def smoke_bomb(self):
        self.attack += 5
        print(F"{self.name} became invisible\n")
    
    def back_slash(self, other_class):
        other_class.life -= 7
        print(f"{self.name} has back slashed {other_class.name}\n")
    
    def shadowTwinBlades(self, other_class):
        dmg = self.attack * 2 + (self.life/5)
        other_class.life -= dmg
        self.life += 3
        print(f"{self.name} got lucky and found a blade\n")

    def shadow_rush(self, other_class):
        dmg = (self.life / self.attack) + self.attack*2
        other_class.life -= dmg
        print(f"{self.name} dashed towards {other_class.name}\n")

class Marksman(Character):
    def __init__(self, name) -> None:
        super().__init__(name)
    
    def snipe(self, other_class):
        other_class.life -= 25
        print(f"Headshot\n")
    
    def teabag(self, other_class):
        self.attack += 10
        other_class.life -= 2
        print(f"{self.name} tea Bagged {other_class.name}\n")
    
    def rapsody(self, other_class):
        other_class.life -= 5 * 5 + (self.attack - 5)
        print(f"5 arrow a la suive\n")

if __name__ == "__main__":
    # Characters
    support = Support("Belerick")
    warrior = Warrior("Hilda")
    mage = Mage("Merlin")
    assasin = Assassin("Scarlet")
    marksman = Marksman("Granger")

    #skills
    marksman.rapsody(mage)
    marksman.snipe(assasin)
    assasin.back_slash(marksman)
    assasin.shadow_rush(marksman)
    assasin.back_slash(support)
    assasin.shadowTwinBlades(mage)
    support.slash(assasin)
    assasin.shadow_rush(mage)
    support.basic_attack(warrior)
    support.slash(assasin)

    print(f"Status:")
    for characters in [support,warrior,mage,assasin,marksman]:
        print(f"{characters.name} : HP : {characters.life} : ATK : {characters.attack}")
