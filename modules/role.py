##Focusing on buffs for now, debuffs after
from modules.stats import Stats

class Role: 
    def __init__(self,id,name,max_stats: Stats):
        self.id = id
        self.name = name
        self.max_stats = max_stats
        #self.buff_choice_one = buff_choice_one
        #self.debuff_choice_one = debuff_choice_one

    def get_stats(self,level: int) -> Stats:
        ##some calc here to get level relevant stats
        new_stats = self.max_stats
        return new_stats