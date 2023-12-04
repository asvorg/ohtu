class TennisGame:
    SCORE_NAMES = ["Love", "Fifteen", "Thirty", "Forty"]

    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.m_score1 = 0
        self.m_score2 = 0

    def won_point(self, player_name):
        if player_name == "player1":
            self.m_score1 += 1
        else:
            self.m_score2 += 1

    def get_score(self):
        if self.m_score1 == self.m_score2:
            return self._get_equal_score()
        elif self.m_score1 >= 4 or self.m_score2 >= 4:
            return self._get_advantage_or_win()
        else:
            return self._get_regular_score()

    def _get_equal_score(self):
        if self.m_score1 >= 3:
            return "Deuce"
        return f"{self.SCORE_NAMES[self.m_score1]}-All"

    def _get_advantage_or_win(self):
        minus_result = self.m_score1 - self.m_score2
        if abs(minus_result) == 1:
            return f"Advantage {self.player1_name if minus_result == 1 else self.player2_name}"
        return f"Win for {self.player1_name if minus_result > 1 else self.player2_name}"

    def _get_regular_score(self):
        return f"{self.SCORE_NAMES[self.m_score1]}-{self.SCORE_NAMES[self.m_score2]}"
