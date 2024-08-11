import matplotlib.pyplot as plt
import math

def interpolate(value, min_value, max_value):
    if value is None:
        return 0
    
    if value < min_value:
        return 0

    if value > max_value:
        return 1
    
    if min_value == max_value:
        raise ValueError("min_value and max_value cannot be the same")

    return (value - min_value) / (max_value - min_value)

def interpolate_tanh(value, min_value, max_value):
    if value is None:
        return 0
    
    if value < min_value:
        return 0

    if value > max_value:
        return 1
    
    if min_value == max_value:
        raise ValueError("min_value and max_value cannot be the same")

    normalized_value = (value - min_value) / (max_value - min_value)
    return math.tanh(normalized_value * 2)

# Generate values
min_value = 0
max_value = 10
values = [i for i in range(min_value, max_value + 1)]

# Calculate interpolations
interpolations = [interpolate(v, min_value, max_value) for v in values]
interpolations_tanh = [interpolate_tanh(v, min_value, max_value) for v in values]

# Plot using matplotlib
plt.plot(values, interpolations, marker='o')
plt.plot(values, interpolations_tanh, marker='x', label='Tanh Interpolation')
plt.title('Interpolate Function')
plt.xlabel('Value')
plt.ylabel('Interpolated Value')
plt.grid(True)
plt.show()