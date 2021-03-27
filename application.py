from constants import PLAYERS, TEAMS


def main():
    cleaned_players_data = [{
        'name': player.get('name'),
        'guardians': player.get('guardians'),
        'experience': True if player.get('experience') == 'YES' else False,
        'height': int(player.get('height')[:2])
    } for player in PLAYERS]

    print(cleaned_players_data)


if __name__ == "__main__":
    main()
