import random
import time
import psutil  # For memory usage measurement

# Function to get possible moves for the empty tile
def get_possible_moves(state):
    empty_index = state.index(0)
    moves = []
    if empty_index not in [0, 1, 2]:  # can move up
        moves.append(-3)
    if empty_index not in [6, 7, 8]:  # can move down
        moves.append(3)
    if empty_index not in [0, 3, 6]:  # can move left
        moves.append(-1)
    if empty_index not in [2, 5, 8]:  # can move right
        moves.append(1)
    return moves

# Function to perform a move
def perform_move(state, move):
    empty_index = state.index(0)
    new_state = state[:]
    new_index = empty_index + move
    new_state[empty_index], new_state[new_index] = new_state[new_index], new_state[empty_index]
    return new_state

# Function to generate Puzzle-8 instances with the goal state at depth “d”
def generate_puzzle_8_depth_d(d):
    goal_state = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    current_state = goal_state.copy()

    for depth in range(d + 1):
        result, current_state = perform_depth_limited_search(current_state, goal_state, depth)
        if result == "found":
            return current_state

    return None

# Function to perform depth-limited search
def perform_depth_limited_search(current_state, goal_state, depth_limit):
    if current_state == goal_state:
        return "found", current_state

    if depth_limit == 0:
        return "not found", current_state

    moves = get_possible_moves(current_state)
    random.shuffle(moves)

    for move in moves:
        new_state = perform_move(current_state, move)
        result, final_state = perform_depth_limited_search(new_state, goal_state, depth_limit - 1)
        if result == "found":
            return "found", final_state
    return "not_found", current_state

# Perform experiments for different depth values
depth_values = list(range(1, 11))  # Depth values from 1 to 10
results = []

for depth in depth_values:
    memory_usage = []
    execution_time = []

    for _ in range(10):  # Repeat each experiment 10 times
        start_time = time.time()
        process = psutil.Process()
        initial_memory = process.memory_info().rss / 1024  # Initial memory usage in KB

        puzzle_instance = generate_puzzle_8_depth_d(depth)

        end_time = time.time()
        final_memory = process.memory_info().rss / 1024  # Final memory usage in KB

        memory_usage.append(final_memory - initial_memory)  # Memory usage in KB
        execution_time.append(end_time - start_time)  # Execution time in seconds

    average_memory = sum(memory_usage) / len(memory_usage)
    average_time = sum(execution_time) / len(execution_time)

    results.append((depth, average_memory, average_time))

# Print the results in a table format
print("Depth\tAverage Memory (B)\tAverage Time (s)")
for depth, memory, time_taken in results:
    print(f"{depth}\t{memory:.2f}\t\t\t{time_taken:.6f}")
