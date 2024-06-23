import random
import curses
import time

class SnakeGame:
    def __init__(self, stdscr):
        self.stdscr = stdscr
        self.height, self.width = stdscr.getmaxyx()
        self.timeout = 100  # Initial timeout for snake movement
        self.direction = curses.KEY_RIGHT
        self.score = 0
        self.snake = [(1, 1), (1, 2), (1, 3)]  # Initial snake position
        self.generate_food()
        self.generate_obstacles()
        self.paused = False

    def generate_food(self):
        while True:
            self.food = (random.randint(1, self.height - 2), random.randint(1, self.width - 2))
            if self.food not in self.snake:
                self.stdscr.addch(self.food[0], self.food[1], 'π')
                break

    def generate_special_food(self):
        while True:
            self.special_food = (random.randint(1, self.height - 2), random.randint(1, self.width - 2))
            if self.special_food not in self.snake and self.special_food != self.food:
                self.stdscr.addch(self.special_food[0], self.special_food[1], 'X')
                break

    def generate_obstacles(self):
        self.obstacles = set()
        obstacle_count = self.height * self.width // 20  # 5% of the game screen
        for _ in range(obstacle_count):
            while True:
                row = random.randint(1, self.height - 6)
                col = random.randint(1, self.width - 6)
                orientation = random.choice(['horizontal', 'vertical'])
                if orientation == 'horizontal':
                    obstacle = [(row, col + i) for i in range(5)]
                else:
                    obstacle = [(row + i, col) for i in range(5)]
                if all(cell not in self.snake and cell not in self.obstacles for cell in obstacle):
                    self.obstacles.update(obstacle)
                    for cell in obstacle:
                        self.stdscr.addch(cell[0], cell[1], ' ')
                    break

    def draw(self):
        self.stdscr.clear()
        self.stdscr.border()
        self.stdscr.addstr(0, 5, 'Score: ' + str(self.score))
        for y, x in self.snake:
            self.stdscr.addch(y, x, ' ')
        for y, x in self.obstacles:
            self.stdscr.addch(y, x, ' ')
        self.stdscr.addch(self.food[0], self.food[1], 'π')
        if hasattr(self, 'special_food'):
            self.stdscr.addch(self.special_food[0], self.special_food[1], 'X')
        self.stdscr.refresh()

    def move(self):
        head = self.snake[0]
        new_head = (head[0] + (self.direction == curses.KEY_DOWN and 1) + (self.direction == curses.KEY_UP and -1),
                    head[1] + (self.direction == curses.KEY_RIGHT and 1) + (self.direction == curses.KEY_LEFT and -1))
        self.snake.insert(0, new_head)
        if new_head == self.food:
            self.score += 1
            self.generate_food()
            if self.score % 5 == 0:
                self.generate_special_food()
        else:
            tail = self.snake.pop()
            self.stdscr.addch(tail[0], tail[1], ' ')
        if new_head in self.obstacles or new_head in self.snake[1:]:
            return False
        return True

    def run(self):
        self.stdscr.clear()
        self.stdscr.nodelay(1)
        while True:
            if not self.paused:
                key = self.stdscr.getch()
                if key == ord(' '):
                    self.paused = not self.paused
                    self.stdscr.addstr(self.height // 2, self.width // 2 - 5, "PAUSED")
                    self.stdscr.refresh()
                    continue
                elif key in [curses.KEY_RIGHT, curses.KEY_LEFT, curses.KEY_UP, curses.KEY_DOWN]:
                    self.direction = key
            if not self.move():
                break
            self.draw()
            time.sleep(0.1)
            if self.score > 0 and self.score % 10 == 0:
                self.timeout -= 10
            self.stdscr.timeout(self.timeout)

        self.stdscr.clear()
        self.stdscr.addstr(self.height // 2 - 1, self.width // 2 - 5, "GAME OVER")
        self.stdscr.addstr(self.height // 2, self.width // 2 - 10, f"Score: {self.score}")
        self.stdscr.addstr(self.height // 2 + 1, self.width // 2 - 10, "Press any key to exit...")
        self.stdscr.getch()

def main(stdscr):
    snake_game = SnakeGame(stdscr)
    snake_game.run()

curses.wrapper(main)
