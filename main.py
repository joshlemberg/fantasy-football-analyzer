from schematics.league import League

if __name__ == '__main__':
    print("hello world and welcome to the fantasy football analyzers")
    league_id_default = 1132795140495564800
    l = League(league_id_default)
    print(l.teams)


