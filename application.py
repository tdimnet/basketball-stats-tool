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
    # I am sorry, this is not fully visible but I wanted to
    # try using list comprehension within a list of a list
    guardians_in_team = ", ".join(
        [", ".join(
            [guardian for guardian in player["guardians"]]
        )for player in team["players"]]
    )

    print("\nTeam: {} Stats".format(team["name"]))
    print("--------------------")
    print("Total players: {}".format(team["number_of_players"]))
    print("Total experienced: {}".format(
        team["number_of_experimented_players"]))
    print("Total inexperienced: {}".format(
        team["number_of_unexperimented_players"]))
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


def calculate_average_height(players):
    list_of_players = [player["height"] for player in players]
    return round(sum(list_of_players)/len(list_of_players), 1)


def balance_teams(players):
    number_of_players_per_team = int(len(players) / len(TEAMS))

    experienced_players = list(filter(
        lambda player: player['experience'] is True, players))
    number_of_experienced_players_per_team = int(
        len(experienced_players) / len(TEAMS))

    inexperienced_players = list(filter(
        lambda player: player['experience'] is False, players))
    number_of_inexperienced_players_per_team = int(
        len(inexperienced_players) / len(TEAMS))

    start_index_experienced_players = 0
    end_index_experienced_players = number_of_experienced_players_per_team

    start_index_inexperienced_players = 0
    end_index_inexperienced_players = number_of_inexperienced_players_per_team

    balanced_teams = list()

    for (index, team_name) in enumerate(TEAMS):
        alphabetical_character = chr(65 + index)

        players_in_team = experienced_players[start_index_experienced_players:end_index_experienced_players] + inexperienced_players[start_index_inexperienced_players:end_index_inexperienced_players]

        team = {
            "option": alphabetical_character,
            "name": team_name,
            "number_of_players": number_of_players_per_team,
            "players": players_in_team,
            "number_of_experimented_players": number_of_experienced_players_per_team,
            "number_of_unexperimented_players": number_of_inexperienced_players_per_team,
            "team_average_height": calculate_average_height(players_in_team)
        }

        balanced_teams.append(team)

        start_index_experienced_players += number_of_experienced_players_per_team
        end_index_experienced_players += number_of_experienced_players_per_team

        start_index_inexperienced_players += number_of_inexperienced_players_per_team
        end_index_inexperienced_players += number_of_inexperienced_players_per_team

    return balanced_teams


def main():
    cleaned_players_data = clean_data(PLAYERS)

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
