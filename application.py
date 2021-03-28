from constants import PLAYERS, TEAMS


def print_menu():
    print("""
    BASKETBALL TEAM STATS TOOL

    ---- MENU----
    
    Here are your choices:
      A) Display Team Stats
      B) Quit
    """)

    user_choice = input("Enter an option:  ")

    print("====")
    print("The user choice is {}".format(user_choice))
    print("====")

    return user_choice


def balance_teams(players):
    number_of_players_per_team = int(len(players) / len(TEAMS))
    
    panthers_team = players[0:6]
    bandits_team = players[6:12]
    warriors_team = players[12:18]

    print("+++++")
    print(panthers_team)
    print("+++++")
    print("+++++")
    print(bandits_team)
    print("+++++")
    print("+++++")
    print(warriors_team)
    print("+++++")
    


def main():
    cleaned_players_data = [{
        'name': player.get('name'),
        'guardians': player.get('guardians'),
        'experience': True if player.get('experience') == 'YES' else False,
        'height': int(player.get('height')[:2])
    } for player in PLAYERS]

    balance_teams(cleaned_players_data)


if __name__ == "__main__":
    main()
