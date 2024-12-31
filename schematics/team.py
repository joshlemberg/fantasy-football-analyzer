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
        return "\n\nTEAM NAME: {0}\nPlayer List: {1}".format(self.display_name, self.players)
    

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
        self._players = list
