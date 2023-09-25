import heapq

# Define the goal state
goal_state = [[0, 1, 2], [3, 4, 5], [6,7 ,8]]

# Function to calculate the Manhattan distance heuristic
def manhattan_distance(state):
    distance = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0:
                row, col = divmod(state[i][j] - 1, 3)
                distance += abs(i - row) + abs(j - col)
    return distance

# Function to get possible moves from the current state
def get_moves(state):
    moves = []
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                if i > 0:
                    moves.append(('U', (i - 1, j)))
                if i < 2:
                    moves.append(('D', (i + 1, j)))
                if j > 0:
                    moves.append(('L', (i, j - 1)))
                if j < 2:
                    moves.append(('R', (i, j + 1)))
    return moves

# Function to perform A* search
# // A* Search Algorithm
# 1.  Initialize the open list
# 2.  Initialize the closed list
#     put the starting node on the open 
#     list (you can leave its f at zero)

# 3.  while the open list is not empty
#     a) find the node with the least f on 
#        the open list, call it "q"

#     b) pop q off the open list
  
#     c) generate q's 8 successors and set their 
#        parents to q
   
#     d) for each successor
#         i) if successor is the goal, stop search
        
#         ii) else, compute both g and h for successor
#           successor.g = q.g + distance between 
#                               successor and q
#           successor.h = distance from goal to 
#           successor (This can be done using many 
#           ways, we will discuss three heuristics- 
#           Manhattan, Diagonal and Euclidean 
#           Heuristics)
          
#           successor.f = successor.g + successor.h

#         iii) if a node with the same position as 
#             successor is in the OPEN list which has a 
#            lower f than successor, skip this successor

#         iV) if a node with the same position as 
#             successor  is in the CLOSED list which has
#             a lower f than successor, skip this successor
#             otherwise, add  the node to the open list
#      end (for loop)
  
#     e) push q on the closed list
#     end (while loop)
def solve_puzzle(initial_state):
    open_list = [(0 + manhattan_distance(initial_state), 0, initial_state, [])]
    closed_set = set()

    while open_list:
        _, cost, current_state, path = heapq.heappop(open_list)

        if current_state == goal_state:
            return path

        closed_set.add(tuple(map(tuple, current_state)))

        for move, (i, j) in get_moves(current_state):
            new_state = [list(row) for row in current_state]
            new_state[i][j], new_state[i][j] = new_state[i][j], new_state[i][j]  # Fix the typo here
            if tuple(map(tuple, new_state)) not in closed_set:
                new_cost = cost + 1
                heapq.heappush(open_list, (new_cost + manhattan_distance(new_state), new_cost, new_state, path + [move]))

    return None

# Example initial state (modify as needed)
initial_state = [[1, 7, 3], [4, 5, 6], [0, 2, 8]]

path = solve_puzzle(initial_state)
if path:
    print("Solution found with {} moves:".format(len(path)))
    for move in path:
        print(move, end=" ")
    print()
else:
    print("No solution found.")
