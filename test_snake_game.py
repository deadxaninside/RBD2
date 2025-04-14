import pytest
from snake_game import SnakeGame, WIDTH, HEIGHT, CELL_SIZE

def test_initial_snake_length():
    game = SnakeGame()
    assert len(game.snake) == 3

def test_food_spawn_within_bounds():
    game = SnakeGame()
    x, y = game.spawn_food()
    assert 0 <= x < WIDTH
    assert 0 <= y < HEIGHT
    assert x % CELL_SIZE == 0
    assert y % CELL_SIZE == 0

def test_snake_eats_food_and_grows():
    game = SnakeGame()
    game.food = (game.snake[0][0] + CELL_SIZE, game.snake[0][1])
    game.move()
    assert len(game.snake) == 4
    assert game.score == 1

def test_collision_with_wall():
    game = SnakeGame()
    game.snake[0] = (WIDTH - CELL_SIZE, 0)
    game.direction = "RIGHT"
    game.move()
    assert game.running is False

