from modules.team import Team
from modules.character import *
from dataclasses import dataclass
import random

@dataclass
class CombatDetails:
    target: Character
    damage: int
    debuff_applied: Affliction
    targethp: int


##To make it simple... probably no slowing during combat for now. 
def decide_order(player_team: Team, enemy_team: Team)->[Character]:
    order_list = []
    for char in player_team.chars: order_list.append(char)
    for char in enemy_team.chars: order_list.append(char)
    order_list = sorted(order_list, key=lambda x: x.equipped_stats.spd, reverse=True)
    return order_list
 
##Tried with larger quantities, appeared to be accurate
def decide_target(enemy_team: Team):
    target_list = []
    for char in enemy_team.chars: 
        if char.combat_stats.hp > 0:
            target_list.append(char)
    choice = random.choices(target_list, [x.combat_stats.aggro for x in target_list],k=1)
    return choice[0]

##Will add more complications such as crits and potentially damage types later
def deal_damage(character, target)->CombatDetails:
    damage = character.combat_stats.atk - target.combat_stats.defense
    target.combat_stats.hp -= damage
    if target.combat_stats.hp < 0: target.combat_stats.hp = 0
    ##Add debuff to target, return debuff too
    dets = CombatDetails(target,damage,0,target.combat_stats.hp)
    return dets

def resolve_debuffs(char : Character):
    return NotImplemented



##TODO
def combat_turn(character, player_team, enemy_team):
    ##TODO Resolve buffs
    target = decide_target(enemy_team)
    dets = deal_damage(character,target)
    ##for combat buffs on character, duration --
    print(f"{character.char_name} attacked {target.char_name} dealing {dets.damage} damage, leaving them with {dets.targethp} hp")
    return dets

#0 for continue fight, 1 for player lose, 2 for player win
def check_outcome(player_team: Team, enemy_team: Team):
    allies = []
    enemies = []
    for char in player_team.chars:
        allies.append(char.combat_stats.hp)
    for char in enemy_team.chars:
        enemies.append(char.combat_stats.hp)
    if sum(allies) == 0:
        return 1
    elif sum(enemies) == 0:
        return 2
    else: return 0



##TODO. Maybe just make combat details a class/struct for easier reading.
#Return array of combat dets 
def combat(player_team: Team, enemy_team: Team):
    order_list = decide_order(player_team, enemy_team)
    combat_dets = None
    ongoing = 0
    i=1
    while not ongoing:
        print(f"_______________\n|---TURN {i}----|\n---------------")
        for char in order_list:
            if type(char) is Enemy:
                combat_dets = combat_turn(char,enemy_team,player_team)
            else: combat_dets = combat_turn(char, player_team, enemy_team)
            ongoing = check_outcome(player_team,enemy_team)
            if (ongoing): break 
        i +=1
    if ongoing is 1: print("player loses")
    else: print("player wins")
        
##Add battle log, most recent battle log for player kept then archived on new battle. 

##Combat Start:
##Input team 1 & team 2
##Order by speed
##for x in order: 
    ##Turn(x)



##Turn:
##Resolve HP Combat Buffs
##Resolve HP Combat Debuffs 
##Choose Target -> weighted rng based on enemy aggro. 
##Damage(target)
    ##Check target hp
    ## if 0, target dead & combat_aggro set to 0
        ##check other team still has a char with 1 or more hp.
        ## Win/lose if not. 
##Buff countdown -1
##Debuff countdown -1
##Reset combat buffs & reapply non hp ones