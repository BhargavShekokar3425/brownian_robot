import pytest
from brownian_robot import BrownianRobot

@pytest.fixture
def bot():
    return BrownianRobot(arena_size=500)

def test_initial_position(bot):
    assert bot.x == 250
    assert bot.y == 250

def test_boundary_collision(bot):
    bot.x = 499
    bot.move()
    assert bot.x != 499  # Should change direction on collision

def test_movement_within_arena(bot):
    initial_x = bot.x
    bot.move()
    assert 0 < bot.x < 500
    assert abs(bot.x - initial_x) <= 2
