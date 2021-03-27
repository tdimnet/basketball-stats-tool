from constants import PLAYERS, TEAMS


def main():
    cleaned_players_data = [{
        'name': player.get('name'),
        'guardians': player.get('guardians'),
        'experience': True if player.get('experience') == 'YES' else False,
        'height': int(player.get('height')[:2])
    } for player in PLAYERS]

    print(cleaned_players_data)


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


if __name__ == "__main__":
    print_menu()
