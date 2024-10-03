import random

class WumpusWorld:
    def __init__(self, size=4):
        self.size = size
        self.world = [[' ' for _ in range(size)] for _ in range(size)]
        self.agent_position = [0, 0]
        self.gold_position = [random.randint(1, size-1), random.randint(1, size-1)]
        self.wumpus_position = [random.randint(1, size-1), random.randint(1, size-1)]
        self.pit_positions = [ [random.randint(1, size-1), random.randint(1, size-1)] for _ in range(size-1)]
        self.agent_alive = True
        self.gold_collected = False
        self.wumpus_alive = True
        self.agent_has_arrow = True
    
    def print_world(self):
        for row in self.world:
            print(' '.join(row))
        print("\n")

    def get_percept(self):
        percepts = []
        x, y = self.agent_position

        # Stench near Wumpus
        if abs(x - self.wumpus_position[0]) + abs(y - self.wumpus_position[1]) == 1:
            percepts.append('stench')

        # Breeze near Pits
        for pit in self.pit_positions:
            if abs(x - pit[0]) + abs(y - pit[1]) == 1:
                percepts.append('breeze')

        # Gold in the same position
        if self.agent_position == self.gold_position:
            percepts.append('glitter')

        return percepts
    
    def move_agent(self, direction):
        if not self.agent_alive:
            print("Game Over! The agent is dead.")
            return

        x, y = self.agent_position

        if direction == 'up':
            if x > 0:
                self.agent_position[0] -= 1
        elif direction == 'down':
            if x < self.size - 1:
                self.agent_position[0] += 1
        elif direction == 'left':
            if y > 0:
                self.agent_position[1] -= 1
        elif direction == 'right':
            if y < self.size - 1:
                self.agent_position[1] += 1
        else:
            print("Invalid move.")

        self.check_agent_status()
    
    def check_agent_status(self):
        if self.agent_position == self.wumpus_position and self.wumpus_alive:
            print("Oh no! The agent encountered the Wumpus and died.")
            self.agent_alive = False

        if self.agent_position in self.pit_positions:
            print("Oops! The agent fell into a pit.")
            self.agent_alive = False

        if self.agent_position == self.gold_position:
            print("The agent found the gold!")
            self.gold_collected = True

    def shoot_arrow(self, direction):
        if not self.agent_has_arrow:
            print("The agent has no arrows left.")
            return

        print(f"The agent shoots the arrow {direction}!")
        self.agent_has_arrow = False
        x, y = self.agent_position

        if direction == 'up' and self.wumpus_position[0] < x:
            print("The arrow killed the Wumpus!")
            self.wumpus_alive = False
        elif direction == 'down' and self.wumpus_position[0] > x:
            print("The arrow killed the Wumpus!")
            self.wumpus_alive = False
        elif direction == 'left' and self.wumpus_position[1] < y:
            print("The arrow killed the Wumpus!")
            self.wumpus_alive = False
        elif direction == 'right' and self.wumpus_position[1] > y:
            print("The arrow killed the Wumpus!")
            self.wumpus_alive = False
        else:
            print("The arrow missed!")
    
    def play(self):
        print("Welcome to the Wumpus World!")
        while self.agent_alive and not self.gold_collected:
            percepts = self.get_percept()
            print(f"Percepts: {percepts}")
            move = input("Move (up, down, left, right) or shoot (s): ")
            
            if move == 's':
                direction = input("Shoot direction (up, down, left, right): ")
                self.shoot_arrow(direction)
            else:
                self.move_agent(move)
            
            if self.gold_collected:
                print("Congratulations! The agent collected the gold and won!")
                break
        if not self.agent_alive:
            print("Game Over.")

if __name__ == "__main__":
    game = WumpusWorld()
    game.play()
