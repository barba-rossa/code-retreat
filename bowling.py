class BowlingGame:
    """Simple Bowling game scorer.

    Implements roll(pins) and score() for standard ten-pin bowling.
    """

    def __init__(self):
        self.rolls = []

    def roll(self, pins: int) -> None:
        if not isinstance(pins, int):
            raise TypeError("pins must be an int")
        if pins < 0 or pins > 10:
            raise ValueError("pins must be between 0 and 10")
        self.rolls.append(pins)

    def score(self) -> int:
        """Calculate and return the total score for the game."""
        score = 0
        roll_index = 0
        rolls = self.rolls
        for frame in range(10):
            # strike
            if roll_index < len(rolls) and rolls[roll_index] == 10:
                score += 10 + self._strike_bonus(roll_index)
                roll_index += 1
            # spare
            elif roll_index + 1 < len(rolls) and rolls[roll_index] + rolls[roll_index + 1] == 10:
                score += 10 + self._spare_bonus(roll_index)
                roll_index += 2
            else:
                score += self._sum_of_frame(roll_index)
                roll_index += 2
        return score

    def _strike_bonus(self, i: int) -> int:
        rolls = self.rolls
        # bonus is next two rolls (if present)
        b1 = rolls[i + 1] if i + 1 < len(rolls) else 0
        b2 = rolls[i + 2] if i + 2 < len(rolls) else 0
        return b1 + b2

    def _spare_bonus(self, i: int) -> int:
        rolls = self.rolls
        return rolls[i + 2] if i + 2 < len(rolls) else 0

    def _sum_of_frame(self, i: int) -> int:
        rolls = self.rolls
        a = rolls[i] if i < len(rolls) else 0
        b = rolls[i + 1] if i + 1 < len(rolls) else 0
        return a + b
