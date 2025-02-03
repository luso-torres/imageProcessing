import matplotlib.pyplot as plt

def plots(unique_values, counts):
    plt.bar(unique_values, counts/(sum(counts)), width=20, color='gray', edgecolor='black')
    plt.title("Histogram of The Probability of the Requantized Image")
    plt.xlabel("Pixel Intensity")
    plt.ylabel("Frequency")
    plt.xticks(unique_values)  # Ensure we see the exact levels
    plt.show()
