import pygame
import random

pygame.init()

WIDTH, HEIGHT = 500, 500
CELL_SIZE = 20


class SnakeGame:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True
        self.snake = [(100, 100), (90, 100), (80, 100)]
        self.direction = "RIGHT"
        self.food = self.spawn_food()
        self.score = 0

    def spawn_food(self):
        return (random.randint(0, WIDTH // CELL_SIZE - 1) * CELL_SIZE,
                random.randint(0, HEIGHT // CELL_SIZE - 1) * CELL_SIZE)

    def move(self):
        head_x, head_y = self.snake[0]
        if self.direction == "UP":
            head_y -= CELL_SIZE
        elif self.direction == "DOWN":
            head_y += CELL_SIZE
        elif self.direction == "LEFT":
            head_x -= CELL_SIZE
        elif self.direction == "RIGHT":
            head_x += CELL_SIZE

        new_head = (head_x, head_y)

        if (new_head in self.snake or
                head_x < 0 or head_x >= WIDTH or
                head_y < 0 or head_y >= HEIGHT):
            self.running = False  # Завершаем игру при столкновении

        self.snake.insert(0, new_head)

        if new_head == self.food:
            self.food = self.spawn_food()
            self.score += 1
        else:
            self.snake.pop()

    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and self.direction != "DOWN":
                    self.direction = "UP"
                elif event.key == pygame.K_DOWN and self.direction != "UP":
                    self.direction = "DOWN"
                elif event.key == pygame.K_LEFT and self.direction != "RIGHT":
                    self.direction = "LEFT"
                elif event.key == pygame.K_RIGHT and self.direction != "LEFT":
                    self.direction = "RIGHT"

    def render(self):
        self.screen.fill((0, 0, 0))

        for segment in self.snake:
            pygame.draw.rect(self.screen, (0, 255, 0), (*segment, CELL_SIZE, CELL_SIZE))

        pygame.draw.rect(self.screen, (255, 0, 0), (*self.food, CELL_SIZE, CELL_SIZE))

        pygame.display.flip()

    def run(self):
        while self.running:
            self.handle_input()
            self.move()
            self.render()
            self.clock.tick(10)
        print(f"Game Over! Your Score: {self.score}")


game = SnakeGame()
game.run()
pygame.quit()