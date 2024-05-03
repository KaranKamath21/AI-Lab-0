import random

# This function returns a list of possible moves from the current state
def get_possible_moves(state):
    # Get a list of possible moves from the current state
    possible_moves = []
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                if i > 0:
                    possible_moves.append((i - 1, j))
                if i < 2:
                    possible_moves.append((i + 1, j))
                if j > 0:
                    possible_moves.append((i, j - 1))
                if j < 2:
                    possible_moves.append((i, j + 1))
    return possible_moves


# This function performs a move on the current state
def perform_move(state, move):
    i, j = move
    new_state = [row[:] for row in state]
    blank_i, blank_j = next((row, col) for row in range(3) for col in range(3) if state[row][col] == 0)
    new_state[blank_i][blank_j], new_state[i][j] = new_state[i][j], new_state[blank_i][blank_j]
    return new_state



# here 0 = blank space
GOAL_STATE = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]


# This function generates a random state by performing 100 random moves from the goal state.
def generate_random_state():
    current_state = [row[:] for row in GOAL_STATE]  # Start with a copy of the goal state
    for i in range(100):
        possible_moves = get_possible_moves(current_state)
        random_move = random.choice(possible_moves)
        current_state = perform_move(current_state, random_move)
    return current_state



# This function checks if the current state is the goal state
def is_goal_state(state):
    # Check if the current state is the goal state
    return state == GOAL_STATE


# This function calculates the Manhattan distance heuristic for the current state.
def manhattan_distance(state):
    # Calculate the Manhattan distance heuristic
    distance = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0:
                row = (state[i][j] - 1) // 3
                col = (state[i][j] - 1) % 3
                distance += abs(row - i) + abs(col - j)
    return distance


# This function prints the state in a readable format
def print_state(state):
    for row in state:
        print(" ".join(map(str, row)))
    print()


def main():
    # Generate a random initial state
    initial_state = generate_random_state()
    print("Random Initial State:")
    print_state(initial_state)
    
    # Check if the initial state is the goal state
    if is_goal_state(initial_state):
        print("The initial state is already the goal state.")
        return
    
    # Calculate the Manhattan distance heuristic for the initial state
    initial_heuristic = manhattan_distance(initial_state)
    print("Manhattan Distance Heuristic for Initial State:", initial_heuristic)

if __name__ == "__main__":
    main()
