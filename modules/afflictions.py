from abc import ABC, abstractmethod
from modules.stats import Stats

#Parent template for buffs and debuffs
#afflictions affect stats directly to accomodate for different types
class Affliction:
    def __init__(self,duration,source):
        self.duration = duration
        self.current = duration
        self.source = source
        ##regex check on source##

    def __str__(self):
        return f"duration: {self.duration}, source:{self.source}, time left:{self.current}, value: {self.value}"
    
    def count_down(self):
        self.current -= 1

    @abstractmethod
    def resolve_affliction(stats):
        return

class SpeedBuff(Affliction):
    def __init__(self,duration,source,value):
        super().__init__(duration,source)
        self.value=value
    
    def resolve_buff(self, stats: Stats):
        print(self.value)
        stats.spd += self.value

class DecayingStr(Affliction):
    def __init__(self, duration, source, value):
        super().__init__(duration,source)
        self.value=value
        self.combat_value = value
        
    def resolve_affliction(self, stats: Stats):
        print(self.value)
        stats.str += self.value

    def count_down(self):
        self.current-=1
        if self.combat_value > 0:
            self.combat_value -= 1

    

