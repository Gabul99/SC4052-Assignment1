import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm

# Parameters
NUM_EPISODES = 100000
MAX_ITERATIONS = 100
CAPACITY = 100
ALPHA = 0.1
PENALTY = -100  # Penalty for exceeding capacity

# Initialize Q-table
num_actions = 2  # Actions: increase or decrease window size for each user
Q = np.zeros((CAPACITY, CAPACITY, num_actions, num_actions))

# Define environment
class CongestionControlEnvironment:
    def __init__(self):
        self.state = [30, 45]  # Initial window sizes for two users

    def step(self, actions):
        # Apply actions to the state and return the next state and reward
        next_state = [self.state[0] + (1 if actions[0] else -1), self.state[1] + (1 if actions[1] else -1)]
        total_window_size = sum(next_state)
        reward = 0
        
        # Check if the total window size exceeds the capacity
        if total_window_size > CAPACITY:
            reward += PENALTY
        if next_state[0] < 0 or next_state[1] < 0:
            reward += PENALTY
        
        # Calculate reward based on the window sizes
        reward += ((next_state[0] + next_state[1])) - (abs(next_state[0] - next_state[1]) * 5)
        
        return next_state, reward

# Q-learning algorithm
for episode in tqdm(range(NUM_EPISODES)):
    environment = CongestionControlEnvironment()
    
    for _ in range(MAX_ITERATIONS):
        # Select actions by random
        actions = np.random.randint(0, num_actions, size=2)
        
        # Take actions and observe next state and reward
        next_state, reward = environment.step(actions)
        
        # Update Q-value function
        Q[environment.state[0]][environment.state[1]][actions[0]][actions[1]] += ALPHA * reward

        if next_state[0] < 0 or next_state[1] < 0:
            break
        
        # Update state
        environment.state = next_state
    
# Testing
TEST_ITERATIONS = 50
traceX1 = []
traceX2 = []
tempState = [30, 45]
for _ in range(TEST_ITERATIONS):
    traceX1.append(tempState[0])
    traceX2.append(tempState[1])
    actions = np.unravel_index(np.argmax(Q[tempState[0], tempState[1]]), Q[tempState[0], tempState[1]].shape)
    tempState = [tempState[0] + (1 if actions[0] else -1), tempState[1] + (1 if actions[1] else -1)]

plt.plot(traceX1, traceX2, marker=".", linewidth=0.5, markersize=1)
plt.xlim([0, 80])
plt.xlabel('X1 Window size')
plt.ylim([0, 80])
plt.ylabel('X2 Window size')
plt.axline((0, 0), slope=1, color="black", linewidth=0.5)
plt.axline((0, 100), slope=-1, color="black", linewidth=0.1)

plt.show()
