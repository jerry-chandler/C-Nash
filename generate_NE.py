import numpy as np
import os

# Set parameters
start_action = 64
end_action = 512
step = 4
num_problems_per_size = 10
value_range = (-8, 8)  # Range of values for the matrix elements
output_dir = "./dataset"  # Base directory to store generated problems

# Generate problems
for action_size in range(start_action, end_action + 1, step):
    # Create a subdirectory for each action size
    sub_dir = os.path.join(output_dir, f"action_{action_size}")
    os.makedirs(sub_dir, exist_ok=True)

    for problem_id in range(1, num_problems_per_size + 1):
        # Generate two matrices with random integers
        M = np.random.randint(value_range[0], value_range[1] + 1, size=(action_size, action_size))
        N = np.random.randint(value_range[0], value_range[1] + 1, size=(action_size, action_size))
        
        # Save the matrices
        M_filename = os.path.join(sub_dir, f"M_problem{problem_id}.npy")
        N_filename = os.path.join(sub_dir, f"N_problem{problem_id}.npy")
        np.save(M_filename, M)
        np.save(N_filename, N)

print(f"Generated Nash equilibrium problems saved to directory: {output_dir}")