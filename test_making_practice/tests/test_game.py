# tests/test_game.py

from src.game import comp_choice, check_game

def test_comp_choice():
    choices = ['rock', 'paper', 'scissor']
    for _ in range(100):  # Test multiple times to ensure randomness covers all choices
        assert comp_choice() in choices

def test_check_game_tie():
    assert check_game('rock', 'rock') == 'tie'
    assert check_game('paper', 'paper') == 'tie'
    assert check_game('scissor', 'scissor') == 'tie'

def test_check_game_player_wins():
    assert check_game('rock', 'paper') == 'player'
    assert check_game('paper', 'scissor') == 'player'
    assert check_game('scissor', 'rock') == 'player'

def test_check_game_computer_wins():
    assert check_game('paper', 'rock') == 'computer'
    assert check_game('scissor', 'paper') == 'computer'
    assert check_game('rock', 'scissor') == 'computer'

def test_invalid_input():
    assert check_game('rock', 'invalid') == 'Invalid Input'
    assert check_game('invalid', 'rock') == 'Invalid Input'
