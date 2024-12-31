import requests
from .team import Team

class League:
    # Skeleton for now

    def __init__(self, leagueid):
        self.leagueid = leagueid
        self._teams = []
        self._traded_picks = []
        return
    
    @property
    def teams(self):
        # This runs in O(your mom)
        if self._teams == []:
            # call into the api here (lazy loading)
            ownerid_to_team_map = {} # mapping to combine data from users and rosters endpoints so we only have to make 2 total calls
            users = requests.get(f"https://api.sleeper.app/v1/league/{self.leagueid}/users", auth=('user', 'pass')).json()
            rosters = requests.get(f"https://api.sleeper.app/v1/league/{self.leagueid}/rosters", auth=('user', 'pass')).json()

            for user in users:
                new_team = Team(user)
                ownerid_to_team_map[user['user_id']] = new_team
                self._teams.append(new_team)

            for roster in rosters:
                team = ownerid_to_team_map[roster['owner_id']]
                team.rosterid = roster['roster_id']
                team.players = roster['players']
        
        return self._teams
    
    def __repr__(self):
        return self.leagueid