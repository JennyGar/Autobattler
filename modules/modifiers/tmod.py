from modules.modifiers.modifier import Modifier
from modules.stats import Stats

class TMod(Modifier):
    def __init__(self,source,value,duration=None):
        super().__init__(source,value)
        self.duration = duration
        self.current = duration

class SpeedBuff(TMod):
    def __init__(self,source,value,duration=None):
        super().__init__(source,value,duration)
    
    def resolve_affliction(self, stats: Stats):
        stats.spd += self.value

class Burn(TMod):
    def __init__(self,source,value,duration=None):
        super().__init__(source,value,duration)
        self.name="Burn"
    
    def resolve_affliction(self, stats: Stats):
        stats.hp -= self.value

class DecayingStr(Modifier):
    def __init__(self,source,value,duration=None):
        super().__init__(source,value,duration)

        
    def resolve_affliction(self, stats: Stats):
        stats.str += self.value
        

    def count_down(self):
        if self.duration is not None and self.current > 0:
            self.current-=1
        if self.combat_value > 0:
            self.combat_value -= 1
