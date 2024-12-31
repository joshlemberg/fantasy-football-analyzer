import requests
from .team import Team

class League:
    # Skeleton for now

    def __init__(self, leagueid):
        self.leagueid = leagueid
        self._rosterid_to_team_map = {} # Safe because it's by reference so no real extra space needed
        self._teams = []
        self._traded_picks = []

    def fetch_teams_and_rosterid_map(self):
        # This runs in O(your mom)
        # call into the api here (lazy loading)
        ownerid_to_team_map = {} # mapping to combine data from users and rosters endpoints so we only have to make 2 total calls
        users = requests.get(f"https://api.sleeper.app/v1/league/{self.leagueid}/users", auth=('user', 'pass')).json()
        rosters = requests.get(f"https://api.sleeper.app/v1/league/{self.leagueid}/rosters", auth=('user', 'pass')).json()

        for user in users:
            new_team = Team(user)
            ownerid_to_team_map[user['user_id']] = new_team
            self._teams.append(new_team)

        for roster in rosters:
            rosterid = roster['roster_id']
            team = ownerid_to_team_map[roster['owner_id']]
            team.rosterid = rosterid
            team.players = roster['players']
            self._rosterid_to_team_map[rosterid] = team
    
    @property
    def teams(self):
        # Lazy loading
        if self._teams == []:
            self.fetch_teams_and_rosterid_map()
        return self._teams
    
    @property
    def rosterid_to_team_map(self):
        # Lazy loading
        if self._rosterid_to_team_map == {}:
            self.fetch_teams_and_rosterid_map()
        return self._rosterid_to_team_map
    
    def print_traded_picks(self):
        traded_picks = requests.get(f"https://api.sleeper.app/v1/league/{self.leagueid}/traded_picks", auth=('user', 'pass')).json()
        #traded_picks = sorted(traded_picks, key=lambda x: x['roster_id'])
        for tp in traded_picks:
            round = tp["round"] 
            year = tp["season"]
            original_owner_name = self.rosterid_to_team_map[tp["roster_id"]].display_name
            tradee_name = self.rosterid_to_team_map[tp["owner_id"]].display_name
            trader_name = self.rosterid_to_team_map[tp["previous_owner_id"]].display_name

            retstr = f"{trader_name} traded Y{year}R{round} "
            if trader_name != original_owner_name:
                retstr += f"(originally owned by {original_owner_name}) "
            retstr += f"to {tradee_name}"
            print(retstr)

    
    def __repr__(self):
        return self.leagueid