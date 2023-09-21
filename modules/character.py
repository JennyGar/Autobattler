from modules.role import Role
from modules.afflictions import Affliction
from abc import ABC
import re


#debuffs are the ones this char will apply when it does damage
#buffs are the ones applied to this char
class Character(ABC):
    def __init__(self, char_id:int, char_name: str, role: Role, buffs: [Affliction], debuffs: [Affliction], level: int):
        self.char_id = char_id
        self.char_name = char_name
        self.role = role
        self.base_stats = role.get_stats(5)
        ##also equipped_stats include inherent
        self.equipped_stats = role.get_stats(5)
        self.combat_stats = role.get_stats(5)

        ##Maybe change from buffs/debuffs to just self afflictions & afflictions on attack?

        ##on turn start affects. change to afflictions
        self.buffs = buffs
        
        ##on attack affects -> add "affliction" to enemy, & add buff to self. 
        self.debuffs = debuffs
        self.level = level

    def __str__(self):
        return f"{self.combat_stats}"
    
    #base stats - only from classes base stats (not incl passive buffs)
    #equipped stats - equipment & inherent. "Equipping" skill

    def get_ebuffs(self):
        ebuffs = []
        for buff in self.buffs:
            if re.search("E\d+",buff.source) is not None: ebuffs.append(buff)
        return ebuffs
    
    def get_cbuffs(self):
        ebuffs = []
        for buff in self.buffs:
            if re.search("C\d+",buff.source) is not None: ebuffs.append(buff)
        return ebuffs
    
    def get_ibuffs(self):
        ebuffs = []
        for buff in self.buffs:
            if re.search("I\d+",buff.source) is not None: ebuffs.append(buff)
        return ebuffs
    
    def get_sbuffs(self):
        ebuffs = []
        for buff in self.buffs:
            print(buff)
            if re.search("S\d+",buff.source) is not None: ebuffs.append(buff)
        return ebuffs
    
    def resolve_cbuffs(self):
        self.combat_stats = self.equipped_stats
        for buff in self.get_cbuffs(): buff.resolve_affliction(self.combat_stats)
        return None
    
class Unit(Character):
    def __init__(self, char_id:int, char_name: str, role: Role, buffs: [Affliction], debuffs: [Affliction], level: int,player_id):
        super().__init__(char_id, char_name, role, buffs, debuffs, level)
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
    def __init__(self, char_id:int, char_name: str, role: Role, buffs: [Affliction], debuffs: [Affliction], level: int, rarity):
        super().__init__(char_id, char_name, role, buffs, debuffs, level)
        self.rarity = rarity