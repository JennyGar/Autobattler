#Wrapper class for list of modifier.
from modules.modifiers.modifier import Modifier
from modules.modifiers.amod import AMod
from modules.modifiers.tmod import TMod
from modules.modifiers.pmod import PMod

class Modifiers():
    def __init__(self, mods: [Modifier]):
        self.mods = mods

    def get_action_modifiers(self):
        amods = []
        for mod in self.mods:
            if issubclass(mod.__class__, AMod):
                amods.append(mod)
        return amods

    def get_passive_modifiers(self):
        pmods = []
        for mod in self.mods:
            if issubclass(mod.__class__, PMod):
                pmods.append(mod)
        return pmods

    def get_turn_modifiers(self):
        tmods = []
        for mod in self.mods:
            if issubclass(mod.__class__, TMod):
                tmods.append(mod)
        return tmods