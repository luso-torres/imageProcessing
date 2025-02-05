import numpy as np

def squaredRange(data) -> float:
    data = np.array(data)
    min_val = np.inf
    max_val = -np.inf
    for info in data:
        if (info != 0) and (info<min_val):
            min_val = float(info)
        elif info > max_val:
            max_val = info
        else:
            continue
    squared_range = (max_val - min_val)**2
    #print(f'Min and max values: {min_val}, {max_val},\nSquared range {squared_range}\n')
    return squared_range