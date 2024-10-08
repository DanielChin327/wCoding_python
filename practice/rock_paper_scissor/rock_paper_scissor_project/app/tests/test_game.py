# tests/test_game.py

import pytest
import game
# tests/test_game.py

from src.game import comp_choice, check_game

def test_comp_choice():
    choices = ['rock', 'paper', 'scissor']
    for _ in range(100):
        assert comp_choice() in choices

def test_check_game_tie():
    assert check_game('rock', 'rock') == 'tie'
