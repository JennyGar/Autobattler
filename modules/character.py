from modules.role import Role
from modules.modifiers.modifier import *
from modules.modifiers.amod import *
from modules.modifiers.pmod import *
from modules.modifiers.tmod import *
from abc import ABC
import re


#debuffs are the ones this char will apply when it does damage
#buffs are the ones applied to this char
class Character(ABC):
    def __init__(self, char_id:int, char_name: str, role: Role, level: int):
        self.char_id = char_id
        self.char_name = char_name
        self.role = role
        self.base_stats = role.get_stats(5)
        #stats with pmods(equipment + support) slightly more storage but easier to process. 
        self.equipped_stats = role.get_stats(5)
        self.combat_stats = role.get_stats(5)
        self.amods= []
        self.pmods = []
        self.tmods= []
        #Removing buffs
        self.level = level

    def __str__(self):
        return f"{self.char_name}, {self.combat_stats}"
    
    #base stats - only from classes base stats (not incl passive buffs)
    #equipped stats - equipment & inherent. "Equipping" skill

    def reset_combat_stats(self):
        self.combat_stats = self.equipped_stats

    def add_amod(self, amod: AMod):
        self.amods.append(amod)
    
    def add_pmod(self, pmod: PMod):
        self.pmods.append(pmod)

    def add_tmod(self, tmod: TMod):
        self.tmods.append(tmod)
    
class Unit(Character):
    def __init__(self, char_id:int, char_name: str, role: Role, level: int,player_id):
        super().__init__(char_id, char_name, role, level)
        self.player_id = player_id

    def equip_item(equip):
        ##Add item to equipment
        ##Add item buffs to buffs
        return None

    def equip_items(equips):
        ##samethings as above but plural
        return None
    
    def add_experience(exp):
        #dothings
        return None
    
    def level_up(levels):
        #dothings
        return None
    
##Maybe Drop table/type at some point
class Enemy(Character):
    def __init__(self, char_id:int, char_name: str, role: Role, level: int, rarity):
        super().__init__(char_id, char_name, role, level)
        self.rarity = rarity