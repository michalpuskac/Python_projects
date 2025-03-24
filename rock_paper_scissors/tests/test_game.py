import sys
import os

# Insert the absolute path to the src directory
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

import pytest
import random
from game import RockPaperScissors

@pytest.fixture
def game():
    return RockPaperScissors()

def test_determine_winner_tie(game, capsys):
    # When both choices are the same, it should be a tie.
    result = game.determine_winner("rock", "rock")
    captured = capsys.readouterr().out
    assert result == "tie"
    assert "TIE!" in captured or "Both chose" in captured

def test_determine_winner_user_wins(game, capsys):
    # rock beats scissors, so user should win.
    result = game.determine_winner("rock", "scissors")
    captured = capsys.readouterr().out
    assert result == "user"
    assert "YOU WIN!" in captured or "Your ROCK beats SCISSORS" in captured

def test_determine_winner_computer_wins(game, capsys):
    # rock loses to paper, so computer should win.
    result = game.determine_winner("rock", "paper")
    captured = capsys.readouterr().out
    assert result == "computer"
    assert "YOU LOSE!" in captured or "Computer's PAPER beats your ROCK" in captured

def test_get_computer_choice(game, monkeypatch):
    # Force random.randint to return a known value (1 => "paper")
    monkeypatch.setattr(random, 'randint', lambda a, b: 1)
    choice = game.get_computer_choice()
    assert choice == "paper"

def test_score_update_user_wins(game):
    initial_user_score = game.user_wins
    # scissors beats paper
    game.determine_winner("scissors", "paper")
    assert game.user_wins == initial_user_score + 1

def test_score_update_computer_wins(game):
    initial_computer_score = game.computer_wins
    # paper loses to scissors
    game.determine_winner("paper", "scissors")
    assert game.computer_wins == initial_computer_score + 1

def test_get_user_choice_valid(monkeypatch, game):
    # Simulate an invalid input followed by a valid one.
    inputs = iter(["invalid", "rock"])
    monkeypatch.setattr('builtins.input', lambda prompt: next(inputs))
    choice = game.get_user_choice()
    assert choice == "rock"
