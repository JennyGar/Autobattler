from modules.modifiers.modifier import Modifier
from modules.stats import Stats
from modules.modifiers.tmod import *

class AMod(Modifier):
    def __init__(self,source,value,duration=None):
        super().__init__(source,value,duration)


##return short string of what happened. xxx happened {target}

##instead of creating new class for every type of buffs, take
class Drainhp(AMod):
    def __init__(self,source,value,duration=None):
        super().__init__(source,value,duration)
        self.name="Drainhp"

    def resolve_affliction(self, char_stats: Stats, opponent_stats: Stats, opponent_tmods: Stats, damage: int):
        drained = 0
        if damage >= self.value:
            drained = self.value
        else: drained = damage
        char_stats.hp += drained
        return f"{drained} hp was drained from"

class ApplyBurn(AMod):
    def __init__(self,source,value,duration=None):
        super().__init__(source,value,duration)
        self.name="ApplyBurn"
    
    def resolve_affliction(self, char_stats: Stats, opponent_stats: Stats, opponent_tmods: list, damage: int):
        for x in opponent_tmods:
            if x.name is 'Burn':
                x.current=self.duration
                return f"Burn was refreshed for {self.duration} turns on"
        opponent_tmods.append(Burn(source='C123',value=self.value,duration=self.duration))
        return f"Burn was applied for {self.duration} turns on"