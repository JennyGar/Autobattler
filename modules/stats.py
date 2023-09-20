class Stats:
    def __init__(self,hp,atk,defense,spd,aggro,crit_chance,crit_damage):
        self.hp = hp
        self.atk = atk
        self.defense = defense
        self.spd = spd
        self.aggro = aggro
        self.crit_chance = crit_chance
        self.crit_damage = crit_damage
    
    def __str__(self):
        return f"hp: {self.hp}, atk: {self.atk}, def: {self.defense}, spd: {self.spd}, aggro: {self.aggro}, crit%: {self.crit_chance}, crit dmg: {self.crit_damage}"