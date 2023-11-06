import unittest
from statistics_service import StatisticsService
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_search(self):
        player = self.stats.search("Semenko")
        self.assertEqual(player.name, "Semenko")

        player = self.stats.search("Gretzky")
        self.assertEqual(player.name, "Gretzky")

        player = self.stats.search("Selanne")
        self.assertIsNone(player)

    def test_team(self):
        players = self.stats.team("EDM")

        self.assertEqual(len(players), 3)

        players = self.stats.team("PIT")

        self.assertEqual(len(players), 1)

    def test_search_player_not_found(self):
        player = self.stats.search("Kane")
        self.assertIsNone(player)

    def test_team_no_players(self):
        players = self.stats.team("SJS")  # Assuming "SJS" is not in the list
        self.assertEqual(len(players), 0)




