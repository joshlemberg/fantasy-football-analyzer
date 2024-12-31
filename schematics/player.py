import requests
import json

class Player:
    def __init__(self, playerid):
        self.playerid = playerid
        self._playername = ""


        # NOTE: What this does is cool. It's a class-attribute so it is
        #       shared amongst instances. So if it is undefined the 
        #       first time it will pick up here and add it, and then be
        #       accesssible from any instance of this class. Super useful.
        if not hasattr(Player, "player_data"):
            with open("playerdata.json") as f:
                Player.player_data = json.load(f)
        
    def __repr__(self):
        return self.playername

    # TODO: expand to function that sets everything we need in one go
    @property
    def playername(self):
        if self.playerid.isalpha():
            # This means it is a defense
            self._playername = str(self.playerid)
        elif self._playername == "":
            self._playername = Player.player_data[self.playerid]["full_name"]
        return self._playername

    def pull_new_players_data(filename="playerdata.json"):
        # Should this be here? or maybe in league or something?
        """
        Gets new player data for all players.
        This is a large request so only do it when necessary

        Args:
            filename: The name of the file to store the JSON data.
        """
        try:
            url = "https://api.sleeper.app/v1/players/nfl"
            response = requests.get(url)
            response.raise_for_status()  # Raise an exception for bad status codes

            # Get the JSON data from the response
            data = response.json()

            # Write the JSON data to the file
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=4)  # Indent for better readability

            print(f"Data from {url} successfully stored in {filename}")

        except requests.exceptions.RequestException as e:
            print(f"Error fetching data from {url}: {e}")