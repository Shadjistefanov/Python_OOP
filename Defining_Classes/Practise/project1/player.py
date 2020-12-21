class Player:
    def __init__(self, name, hp, mp):
            self.name = name
            self.hp = hp
            self.mp = mp
    skills={}
    guild='Unaffiliated'

    def add_skill(self,skill_name, mana_cost):
        if skill_name not in self.skills:
            self.skills[skill_name]=mana_cost
            return f'Skill {skill_name} added to the collection of the player {self.name}'
        return 'Skill already added'

    def player_info(self):
        text= f'Name: {self.name}\nGuild: {self.guild}\nHP: {self.hp}\nMP: {self.mp}\n'
        for skill,mp in self.skills.items():
            text+=f'==={skill} - {mp}\n'
        #text+=f'\n'
        return text
