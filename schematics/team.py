from .player import Player

class Team:
    def __init__(self, data):
        self.avatar = data.get('avatar')
        self.display_name = data.get('display_name')
        self.is_bot = data.get('is_bot')
        self.is_owner = data.get('is_owner')
        self.league_id = data.get('league_id')
        self.metadata = data.get('metadata', {})
        self.settings = data.get('settings')
        self.user_id = data.get('user_id')

        # Properties
        self._rosterid = -1
        self._players = []

    def __repr__(self):
        return "\n\nTEAM NAME: {0}\nRoster ID: {1}\nPlayer List: {2}".format(self.display_name, self._rosterid, self.players)
    

    # Roster ID
    @property
    def rosterid(self):
        return self._rosterid # What if it is not set yet?
    
    @rosterid.setter
    def rosterid(self, value):
        self._rosterid = value

    
    # Players
    # TODO: make a player class, for now just use player IDs
    @property
    def players(self):
        return self._players
    
    @players.setter
    def players(self, list):
        new_player_list = []
        for playerid in list:
            new_player = Player(playerid)
            new_player_list.append(new_player)
        self._players = new_player_list

