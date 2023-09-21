from modules.character import *
from modules.role import Role
from modules.stats import Stats
from modules.team import Team
import modules.combat as Combat
from modules.afflictions import *
import random


mybuff = SpeedBuff('C1234',5,4)
#print(mybuff)
mybuff.count_down()
#print(mybuff)
##Test roles
airmage = Role(1,'airmage1',Stats(20,17,8,15,.75,.2,30))
fighter = Role(2,'fighter2',Stats(30,15,10,10,1.2,0,0))
airmage2 = Role(4,'airmage3',Stats(20,18,7,14,1,.2,30))
fighter2 = Role(5,'fighter4',Stats(30,13,11,12,.75,0,0))
airmage3 = Role(6,'airmage5',Stats(20,16,8,16,1,.2,30))
fighter3 = Role(7,'fighter6',Stats(30,12,12,9,1.5,0,0))


#Test characters
char1 = Unit(1,'ally1',airmage,[mybuff],[],level=5,player_id=3)
char2 = Unit(2,'ally2',fighter,[],[],level=5,player_id=3)
char3 = Unit(3,'ally3',airmage2,[],[],level=5,player_id=3)
char4 = Enemy(4,'enemy4',fighter2,[],[],level=5,rarity="normal")
char5 = Enemy(5,'enemy5',airmage3,[],[],level=5,rarity="normal")
char6 = Enemy(6,'enemy6',fighter3,[],[],level=5,rarity="normal")


print(char1)
#mybuff.resolve_buff(char1.combat_stats)
char1.resolve_cbuffs()
print(char1)
#Test teams
player_one_team = Team([char1,char2,char3])
player_two_team = Team([char4,char5,char6])

choices = Combat.decide_target(player_two_team)
choice_list = []

#Combat.combat(player_one_team,player_two_team)

##Can just do if is unit() or if is monster()
""" print(type(player_one_team))

for char in player_one_team.chars:
    if type(char) is Unit:
        print("aaa")
    else:
        print("noo")

turn_list = Combat.decide_order(player_one_team,player_two_team)
for char in turn_list:
    print(f"{char}\n")
 """

##Resolving buffs if I had them. Works. 
""" for buff in mychar.buffs:
    buff.resolve_buff(mychar.combat_stats) """##