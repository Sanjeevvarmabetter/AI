from collections import deque

def water_jug_problem(capacity_x, capacity_y, target):
    # Create a set to store visited states
    visited = set()
    
    # Create an initial state with both jugs empty
    initial_state = (0, 0)
    
    # Create a queue for BFS
    queue = deque()
    queue.append(initial_state)
    
    while queue:
        current_state = queue.popleft()
        x, y = current_state
        
        # Check if the target amount is reached
        if x == target or y == target:
            return current_state
        
        # Generate possible next states
        next_states = []
        
        # Fill jug X
        next_states.append((capacity_x, y))
        
        # Fill jug Y
        next_states.append((x, capacity_y))
        
        # Empty jug X
        next_states.append((0, y))
        
        # Empty jug Y
        next_states.append((x, 0))
        
        # Pour water from X to Y
        pour = min(x, capacity_y - y)
        next_states.append((x - pour, y + pour))
        
        # Pour water from Y to X
        pour = min(capacity_x - x, y)
        next_states.append((x + pour, y - pour))
        
        for state in next_states:
            if state not in visited:
                queue.append(state)
                visited.add(state)
    
    # If the target amount cannot be reached
    return None

# Example usage:
capacity_x = 4
capacity_y = 3
target = 2

result = water_jug_problem(capacity_x, capacity_y, target)
if result:
    print(f"Target amount of {target} liters can be measured.")
    print(f"Final state: Jug X = {result[0]}, Jug Y = {result[1]}")
else:
    print(f"Target amount of {target} liters cannot be measured.")
