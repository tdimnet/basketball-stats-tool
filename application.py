from constants import PLAYERS, TEAMS


def display_menu():
    print("BASKETBALL TEAM STATS TOOL\n")
    print("---- MENU ----\n")
    print("Here are your choices:")
    print("  A) Display Team Stats")
    print("  B) Quit\n")

    user_choice = input("Enter an option: ")
    print("")

    return user_choice


def display_team(team):

    players_in_team = ", ".join([player["name"] for player in team["players"]])
    # I am sorry, this is not fully visible but I wanted to try using list comprehension within a list of a list
    guardians_in_team = ", ".join( # This is the first level of the list / We loop here accross the players
        [", ".join( # This the second level of the list / We loop here accross the guardians in the player dict
            [guardian for guardian in player["guardians"]]
        )for player in team["players"]]
    )

    print("\nTeam: {} Stats".format(team["name"]))
    print("--------------------")
    print("Total players: {}".format(team["number_of_players"]))
    print("Total experienced: {}".format(team["number_of_experimented_players"]))
    print("Total inexperienced: {}".format(team["number_of_unexperimented_players"]))
    print("Average height: {}\n".format(team["team_average_height"]))

    print("Players on Team:")
    print("  {}".format(players_in_team))
    print("Guardians:")
    print("  {}".format(guardians_in_team))

    


def display_teams_menu(teams):
    is_looking_for_a_team = True

    while is_looking_for_a_team:
        for team in teams:
            print("{}) {}".format(team["option"], team["name"]))

        selected_team = input("\nPlease select an option: ")
        filtered_team = list(filter(lambda team: team['option'] == selected_team, teams))

        if len(filtered_team) != 0:
            display_team(filtered_team[0])

            is_looking_for_a_team = False
        else:
            print("\nPlease choose an existing team\n")

    
def clean_data(players_data):
    return [{
        'name': player.get('name'),
        'guardians': list(player.get('guardians').split(" and ")),
        'experience': True if player.get('experience') == 'YES' else False,
        'height': int(player.get('height')[:2])
    } for player in PLAYERS]


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
            "players": players[start_index:end_index],
            "number_of_experimented_players": 3,
            "number_of_unexperimented_players": 3,
            "team_average_height": 42.5
        }

        balanced_teams.append(team)

        start_index += number_of_players_per_team
        end_index += number_of_players_per_team
    
    return balanced_teams


def main():
    cleaned_players_data = clean_data(PLAYERS)

    # print("=====")
    # print(cleaned_players_data)
    # print("=====")

    balanced_teams = balance_teams(cleaned_players_data)

    is_app_running = True

    while is_app_running:
        user_choice = display_menu()

        if user_choice == "A":
            display_teams_menu(balanced_teams)

            input("\nPress ENTER to continue...\n")
        elif user_choice == "B":
            print("Exit")
            is_app_running = False
        else:
            print("Please choose a valid choice\n")
    


if __name__ == "__main__":
    main()
