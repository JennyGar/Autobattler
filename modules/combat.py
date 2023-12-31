from modules.team import Team
from modules.character import *
from dataclasses import dataclass
import random


##Everything being printed rn should go to combat logs. 
##combat -> adds results & info to a combat log file

@dataclass
class CombatDetails:
    target: Character
    damage: int
    targethp: int
    #list of strings
    amodstr: str

##Returns ordered list based on speed for combatants
def decide_order(player_team: Team, enemy_team: Team)->[Character]:
    order_list = []
    for char in player_team.chars: order_list.append(char)
    for char in enemy_team.chars: order_list.append(char)
    order_list = sorted(order_list, key=lambda x: x.equipped_stats.spd, reverse=True)
    list_string = "order list: "
    for x in order_list:
        list_string += f"{x.char_name}"
    return order_list
 
##Decides target based on weighted aggro
def decide_target(enemy_team: Team) -> Character:
    target_list = []
    for char in enemy_team.chars: 
        if char.combat_stats.hp > 0:
            target_list.append(char)
    choice = random.choices(target_list, [(x.combat_stats.aggro) for x in target_list],k=1)
    return choice[0]

##Damage calculations, action modifiers applied to damage after initial calc. 
def deal_damage(character, target)->CombatDetails:
    damage = character.combat_stats.atk - target.combat_stats.defense
    amods = apply_amods(character,target,damage)
    damage = amods[0]
    amodstr = amods[1]
    target.combat_stats.hp -= damage
    if target.combat_stats.hp < 0: target.combat_stats.hp = 0
    dets = CombatDetails(target,damage,target.combat_stats.hp,amodstr)
    return dets

##Action modifiers (After damage calc)
def apply_amods(char: Character, target: Character, damage):
    #Stores list of strings describing amod application
    amodstr = []
    for amod in char.amods:
        #eventually add damage. 
        x = amod.resolve_affliction(char.combat_stats,target.combat_stats,target.tmods,damage)
        amodstr.append(f"{x} {target.char_name}")
    return [damage,amodstr]

##Turn modifiers (Start of Turn)
def apply_tmods(char:Character):
    #start_stats = char.combat_stats.__str__()
    start_stats = char.combat_stats.hp.__str__()
    for tmod in char.tmods:
        tmod.resolve_affliction(char.combat_stats)
        ##TODO: Add function to check all stats affected & show relevant stats. for now only doing hp for ease of show.
        print(f"{tmod.name} resolved on {char.char_name}: {start_stats} -> {char.combat_stats.hp} hp")
    if char.combat_stats.hp <= 0:
        print(f"{char.char_name} lost the last of their health and cannot continue")

#Reduce duration on turn modifiers (End of Turn)
def countdown_tmods(char:Character):
    start_stats = char.combat_stats
    for tmod in char.tmods:
        tmod.count_down()
        tempstring = f"Turns left on {tmod.name} for {char.char_name}: {tmod.current}"
        if tmod.current == 0:
            del tmod
            tempstring += ". It timed out"
        print(tempstring)

##Turn for a character##For logs probably have start turn (char_id) and end turn (char_id)
def combat_turn(character, player_team, enemy_team):
    if character.combat_stats.hp <= 0:
        return
    apply_tmods(character)
    target = decide_target(enemy_team)
    starthp = target.combat_stats.hp.__str__()
    dets = deal_damage(character,target)
    print(f"{character.char_name} attacked {target.char_name} dealing {dets.damage} damage, {starthp} -> {dets.targethp} hp")
    for amod in dets.amodstr:
        print(amod)
    if dets.targethp <= 0:
        print(f"{target.char_name} is no longer able to continue")
    countdown_tmods(character)
    return dets

#0 for continue fight, 1 for player lose, 2 for player win
def check_outcome(player_team: Team, enemy_team: Team):
    allies = []
    enemies = []
    for char in player_team.chars:
        if char.combat_stats.hp < 0: char.combat_stats.hp = 0
        allies.append(char.combat_stats.hp)
    for char in enemy_team.chars:
        if char.combat_stats.hp < 0: char.combat_stats.hp = 0
        enemies.append(char.combat_stats.hp)
    if sum(allies) == 0:
        return 1
    elif sum(enemies) == 0:
        return 2
    else: return 0

def print_players(player_team: Team, enemy_team:Team):
    enemies = "ENEMIES: "
    allies= "ALLIES: "
    for char in enemy_team.chars:
        enemies += f"•{char.char_name} {char.combat_stats.hp}hp  "
    for char in player_team.chars:
        allies += f"•{char.char_name} {char.combat_stats.hp}hp  "
    return [allies,enemies]

def combat(player_team: Team, enemy_team: Team):
    for char in player_team.chars:
        char.reset_combat_stats()
    for char in enemy_team.chars:
        char.reset_combat_stats()
    order_list = decide_order(player_team, enemy_team)
    combat_dets = None
    ongoing = 0
    i=1
    ##TODO: timeout after 15(?) turns & wincon based on total team hp.
    while not ongoing:
        #print(f"_______________\n|---TURN {i}----|\n---------------")
        x = print_players(player_team,enemy_team)
        print(f"{'_'*70}\n|---TURN {i}----| {x[0]}\n|             | {x[1]}\n {'-'*70}")
        for char in order_list:
            if type(char) is Enemy:
                combat_dets = combat_turn(char,enemy_team,player_team)
            else: combat_dets = combat_turn(char, player_team, enemy_team)
            ongoing = check_outcome(player_team,enemy_team)
            if (ongoing): break 
        i +=1
    if ongoing == 1: print("player loses")
    else: print("player wins")
    for char in player_team.chars:
        char.reset_combat_stats()
    for char in enemy_team.chars:
        char.reset_combat_stats()
        
##TODO: Add battle log, most recent battle log for player kept then archived on new battle. 