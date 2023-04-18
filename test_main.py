import pytest
import random
from main import Game

@pytest.fixture
def game():
    return Game()

def test_roll(game): #擊倒測試
    game.roll(5)
    assert game.game_stat[0][0] == 5
    
def test_score_calc_strike(game): #strike測試
    score = game.score_calc(10)
    assert score == 30

def test_score(game): #每回都擊倒四顆
    score_test = [4 for _ in range(20)]
    for i in score_test:
        game.roll(i)
    game.score()
    assert game.total_score == 80

def test_score_calc_spare(game): #spare測試
    game.roll(5)
    game.roll(5)
    score = game.score_pt[0]
    assert score == 15