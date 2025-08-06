## Day 6: Visualize Bubble Sort using Matplotlib

import matplotlib.pyplot as plt
import random
import time

def bubble_sort_visual(arr):
    # Turn on interactive mode
    plt.ion()
    fig, ax = plt.subplots()

    for i in range(len(arr)):
        for j in range(0, len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                # Swap elements
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

            # Clear and redraw chart with current state of the array
            ax.clear()
            ax.bar(range(len(arr)), arr, color='skyblue')
            ax.set_title("Bubble Sort Visualization")
            ax.set_xlabel("Index")
            ax.set_ylabel("Value")
            plt.pause(0.1)  # Pause to simulate animation

    plt.ioff()
    plt.show()


# Generate a list of 20 random integers between 10 and 100
data = [random.randint(10, 100) for _ in range(20)]

# Run the visualization
bubble_sort_visual(data)
