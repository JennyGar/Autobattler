from modules.modifiers.modifier import Modifier


#Passive modifiers from equip & support
class PMod(Modifier):
    def __init__(self,source,value,duration=None):
        super().__init__(source,value,duration)