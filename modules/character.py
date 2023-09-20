from modules.role import Role
from modules.afflictions import Affliction
from abc import ABC

class Character(ABC):
    def __init__(self, char_id:int, char_name: str, role: Role, buffs: [Affliction], debuffs: [Affliction], level: int):
        self.char_id = char_id
        self.char_name = char_name
        self.role = role
        self.base_stats = role.get_stats(5)
        ##also equipped_stats include inherent
        self.equipped_stats = role.get_stats(5)
        self.combat_stats = role.get_stats(5)
        self.buffs = buffs
        self.debuffs = debuffs
        self.level = level

    def __str__(self):
        return f"{self.combat_stats}"
    
    #base stats - only from classes base stats (not incl passive buffs)
    #equipped stats - equipment & inherent. "Equipping" skill


    def get_ebuffs(buffs):
        ##get buffs with E
        return None
    
    def get_cbuffs(buffs):
        ##get buffs with C
        return None
    
    def get_ibuffs(buffs):
        ##get buffs with I
        return None
    
    def get_sbuffs(buffs):
        ##get buffs with S
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