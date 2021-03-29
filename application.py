from constants import PLAYERS, TEAMS


def cli(teams):
    print("""
    BASKETBALL TEAM STATS TOOL

    ---- MENU ----
    
    Here are your choices:
      A) Display Team Stats
      B) Quit
    """)

    is_choosing = True

    while is_choosing == True:
        user_choice = input("Enter an option:  ")

        if user_choice == "A":
            is_choosing = False
        elif user_choice == "B":
            print("Thanks you for your visit!")
            exit(0)
        else:
            print("Not ok")

    for team in teams:
        print("{}) {}".format(team["option"], team["name"]))

    input_option = input("Please an option: ")

    print("====")
    print("The input option is {}".format(input_option))
    print("====")


def balance_teams(players):
    number_of_players_per_team = int(len(players) / len(TEAMS))

    start_index = 0
    end_index = number_of_players_per_team
    
    panthers_team = players[0:6]
    bandits_team = players[6:12]
    warriors_team = players[12:18]

    balanced_teams = list()

    for (index, team_name) in enumerate(TEAMS):
        alphabetical_character = chr(65 + index)

        team = {
            "option": alphabetical_character,
            "name": team_name,
            "number_of_players": number_of_players_per_team,
            "players": players[start_index:end_index]
        }

        balanced_teams.append(team)

        start_index += number_of_players_per_team
        end_index += number_of_players_per_team
    
    return balanced_teams
    


def main():
    cleaned_players_data = [{
        'name': player.get('name'),
        'guardians': player.get('guardians'),
        'experience': True if player.get('experience') == 'YES' else False,
        'height': int(player.get('height')[:2])
    } for player in PLAYERS]

    balanced_team = balance_teams(cleaned_players_data)

    cli(balanced_team)


if __name__ == "__main__":
    main()
