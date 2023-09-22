from abc import ABC, abstractmethod
from modules.stats import Stats

#Parent template for any type of buff/debuff/skill
#mostly affect stats directly but amod affects target. Seperated to prevent import loop and easily seperate by
class Modifier():
    def __init__(self,source,value,duration=None):
        self.name = "add_mod_name"
        self.source = source
        self.value=value
        self.combat_value = value
        self.duration = duration
        self.current = duration
        ##regex check on source##

    def __str__(self):
        mystring = f"name: {self.name}, source:{self.source}, value: {self.value}"
        if self.duration is not None:
            mystring += f", duration: {self.duration}, time left: {self.current}"
        return mystring
    
    def count_down(self):
        if self.duration is not None and self.current > 0:
            self.current -= 1
        #if self.current == 0: 
            #print(f"{self.name} expired")

    @abstractmethod
    def resolve_affliction(stats):
        return


    

