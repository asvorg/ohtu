from player_reader import PlayerReader
from statistics_service import StatisticsService

def main():
    stats = StatisticsService(
        PlayerReader("https://studies.cs.helsinki.fi/nhlstats/2021-22/players.txt")
    )

    # järjestetään kaikkien tehopisteiden eli maalit+syötöt perusteella
    print("Top point getters:")
    for player in stats.top(10, "points"):  # Use string "points" here
        print(player)

    # metodi toimii samalla tavalla kuin yo. kutsu myös ilman toista parametria
    for player in stats.top(10):
        print(player)

    # järjestetään maalien perusteella
    print("Top point goal scorers:")
    for player in stats.top(10, "goals"):  # Use string "goals" here
        print(player)

    # järjestetään syöttöjen perusteella
    print("Top by assists:")
    for player in stats.top(10, "assists"):  # Use string "assists" if applicable
        print(player)

if __name__ == "__main__":
    main()
