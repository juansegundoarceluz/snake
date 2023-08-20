import pygame 
import random

# Dimensiones de la pantalla
WIDTH = 640
HEIGHT = 480

# Colores
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Tamaño del bloque y velocidad de movimiento
BLOCK_SIZE = 20
SNAKE_SPEED = 7

# Inicialización de Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Clase Snake
class Snake:
    def __init__(self):
        self.body = [(WIDTH // 2, HEIGHT // 2)]
        self.direction = random.choice(['UP', 'DOWN', 'LEFT', 'RIGHT'])

    def move(self):
        x, y = self.body[0]
        if self.direction == 'UP':
            y -= BLOCK_SIZE
        elif self.direction == 'DOWN':
            y += BLOCK_SIZE
        elif self.direction == 'LEFT':
            x -= BLOCK_SIZE
        elif self.direction == 'RIGHT':
            x += BLOCK_SIZE
        self.body.insert(0, (x, y))
        self.body.pop()

    def change_direction(self, new_direction):
        if (new_direction == 'UP' and self.direction != 'DOWN') or \
                (new_direction == 'DOWN' and self.direction != 'UP') or \
                (new_direction == 'LEFT' and self.direction != 'RIGHT') or \
                (new_direction == 'RIGHT' and self.direction != 'LEFT'):
            self.direction = new_direction

    def draw(self):
        for x, y in self.body:
            pygame.draw.rect(screen, GREEN, (x, y, BLOCK_SIZE, BLOCK_SIZE))

    def check_collision(self):
        x, y = self.body[0]
        if x < 0 or x >= WIDTH or y < 0 or y >= HEIGHT:
            return True
        for block in self.body[1:]:
            if block == (x, y):
                return True
        return False

    def eat_food(self, food):
        if self.body[0] == food.position:
            self.body.append((0, 0))
            return True
        return False

# Clase Food
class Food:
    def __init__(self):
        self.position = (random.randint(0, (WIDTH - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE,
                         random.randint(0, (HEIGHT - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE)

    def draw(self):
        pygame.draw.rect(screen, RED, (self.position[0], self.position[1], BLOCK_SIZE, BLOCK_SIZE))

# Creación de la serpiente y la comida
snake = Snake()
food = Food()

# Bucle principal del juego
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake.change_direction('UP')
            elif event.key == pygame.K_DOWN:
                snake.change_direction('DOWN')
            elif event.key == pygame.K_LEFT:
                snake.change_direction('LEFT')
            elif event.key == pygame.K_RIGHT:
                snake.change_direction('RIGHT')

    snake.move()
    if snake.check_collision():
        pygame.quit()
        exit()

    if snake.eat_food(food):
        food = Food()

    # Dibujar en pantalla
    screen.fill(BLACK)
    snake.draw()
    food.draw()
    pygame.display.flip()

    # Controlar la velocidad del juego
    clock.tick(SNAKE_SPEED)