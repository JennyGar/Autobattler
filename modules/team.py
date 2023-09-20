from modules.character import Character

##I want to add more here, like a support which is why this exists. Should be type of character and not actually character.
class Team:
    def __init__(self, chars: [Character]):
        self.chars = chars

    def __str__(self):
        mystring = ""
        for i in range(len(self.chars)):
            mystring += f"Character{i+1}: {self.chars[i]}\n"
        return mystring