import pytest

from bowling import BowlingGame  # implement this in `bowling.py`

def new_game():
    return BowlingGame()

def roll_many(game, pins, times):
    for _ in range(times):
        game.roll(pins)

def roll_sequence(game, rolls):
    for pins in rolls:
        game.roll(pins)

# Phase 1: basic rolls
def test_gutter_game_scores_zero():
    g = new_game()
    roll_many(g, 0, 20)
    assert g.score() == 0

def test_all_ones_scores_20():
    g = new_game()
    roll_many(g, 1, 20)
    assert g.score() == 20