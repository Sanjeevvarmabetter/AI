class PuzzleNode:
    def __init__(self, state, moves, parent):
        self.state = state
        self.moves = moves
        self.parent = parent

    def is_goal(self, goal_state):
        return self.state == goal_state

    def generate_child_nodes(self):
        # Generate possible child nodes by making valid moves
        children = []
        zero_index = self.state.index(0)

        for move in moves:
            new_zero_index = zero_index + move

            if 0 <= new_zero_index < len(self.state):
                new_state = list(self.state)
                new_state[zero_index], new_state[new_zero_index] = new_state[new_zero_index], new_state[zero_index]
                children.append(PuzzleNode(new_state, self.moves + 1, self))

        return children

    def print_solution(self):
        if self.parent:
            self.parent.print_solution()
        print(self.state)

def dfs(initial_state, goal_state):
    stack = [PuzzleNode(initial_state, 0, None)]

    while stack:
        current_node = stack.pop()

        if current_node.is_goal(goal_state):
            print("Solution found in", current_node.moves, "moves:")
            current_node.print_solution()
            return

        stack.extend(current_node.generate_child_nodes())

# Possible moves: Left, Right, Up, Down
moves = [-1, 1, -3, 3]

# Initial and goal states for 8-puzzle
initial_state = [1, 2, 3, 0, 4, 5, 6, 7, 8]
goal_state = [1, 2, 3, 6, 5, 4, 0, 7, 8]

dfs(initial_state, goal_state)
