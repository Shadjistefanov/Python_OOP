
class Guild:
    def __init__(self, name):
            self.name = name

    players=[]

    def assign_player(self,player):
        if player.guild!=self.name:
            if player.guild=='Unaffiliated':
                self.players.append(player)
                player.guild=self.name
                return f'Welcome player {player.name} to the guild {self.name}'
            else:
                return f'Player {player.name} is in another guild.'
        else:
            return f'Player {player.name} is already in the guild.'

    def kick_player(self,player_name: str):
        for player in self.players:
            if player.name==player_name:
                self.players.remove(player)
                #player.guild='Unaffiliated'
                return f'Player {player_name} has been removed from the guild.'
        return f'Player {player_name} is not in the guild.'

    def guild_info(self) :
        text= f'Guild: {self.name}\n'
        for player in self.players:
            text+=f'{player.player_info()}'
        #text+=f'\n'
        return text
"""
player = p.Player("George", 50, 100)
print(player.add_skill("Shield Break", 20))
print(player.player_info())
guild = Guild("UGT")
print(guild.assign_player(player))
print(guild.guild_info())"""
