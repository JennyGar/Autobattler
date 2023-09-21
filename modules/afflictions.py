from abc import ABC, abstractmethod
from modules.stats import Stats

#Parent template for buffs and debuffs
#afflictions affect stats directly to accomodate for different types. Tying to char also creates import loop issue.
class Affliction():
    def __init__(self, source,value,duration=None):
        self.duration = duration
        self.current = duration
        self.source = source
        self.value=value
        self.combat_value = value
        ##regex check on source##

    def __str__(self):
        return f"duration: {self.duration}, source:{self.source}, time left:{self.current}, value: {self.value}"
    
    def count_down(self):
        if self.duration is not None and self.current > 0:
            self.current -= 1

    @abstractmethod
    def resolve_affliction(stats):
        return
    
class SpeedBuff(Affliction):
    def __init__(self,source,value,duration=None):
        super().__init__(source, value,duration)
    
    def resolve_affliction(self, stats: Stats):
        print(self.value)
        stats.spd += self.value

class DecayingStr(Affliction):
    def __init__(self,source,value,duration=None):
        super().__init__(source,value,duration)

        
    def resolve_affliction(self, stats: Stats):
        print("resolve affliction has been called")
        print(self.value)
        stats.str += self.value

    def count_down(self):
        if self.duration is not None and self.current > 0:
            self.current-=1
        if self.combat_value > 0:
            self.combat_value -= 1

    

