from modules.modifiers.modifier import Modifier
from modules.stats import Stats
from modules.modifiers.tmod import *



##INSTEAD OF CHARACTER, DIRECTLY ACESS THE MOD LIST AND enemy stats
class AMod(Modifier):
    def __init__(self,source,value,duration=None):
        super().__init__(source,value,duration)

##instead of creating new class for every type of buffs, take
class Drainhp(AMod):
    def __init__(self,source,value,duration=None):
        super().__init__(source,value,duration)
        self.name="Drainhp"

    def resolve_affliction(self, char_stats: Stats, opponent_stats: Stats, opponent_mods: Stats):
        print("resolve affliction has been called")
        char_stats.hp += 2
        opponent_stats.hp -= 2

class ApplyBurn(AMod):
    def __init__(self,source,value,duration=None):
        super().__init__(source,value,duration)
        self.name="ApplyBurn"
    
    def resolve_affliction(self, char_stats: Stats, opponent_stats: Stats, opponent_mods: list):
        print("resolve affliction has been called")
        for x in opponent_mods:
            if x.source=='C123':
                x.current=self.duration
        else: opponent_mods.append(Burn(source='C123',value=self.value,duration=self.duration))