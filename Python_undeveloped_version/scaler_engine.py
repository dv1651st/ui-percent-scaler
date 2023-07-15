import numpy as np

def calculate_values(skew, element_count, spread):
    # Create an array of element indices (1 to element_count)
    indices = np.arange(1, element_count + 1)
    
    # Minkowski-like calculation
    spread_factor = spread / 100  # Convert spread from 0-100 scale to 0-1 scale
    if spread_factor != 0:  # Avoid division by zero
        print("skew",skew)
        minkowski_values = 1 / np.abs(indices - skew) ** spread_factor
    else:  # If spread is zero, create an array where only the skew point has value
        minkowski_values = np.zeros(element_count)
        minkowski_values[skew - 1] = 1  # Index is skew - 1 because indices are 0-based
    
    # Normalize so the sum is 100
    minkowski_values = minkowski_values / np.sum(minkowski_values) * 100

    # Convert to percentage strings for display and return
    final_values = [f"{val:.2f}%" for val in minkowski_values]
    return final_values
