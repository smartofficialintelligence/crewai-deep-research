import matplotlib.pyplot as plt

def plot_sentiment_distribution(sentiments):
    plt.hist(sentiments, bins=5)
    plt.title("Sentiment Distribution")
    plt.xlabel("Sentiment Score")
    plt.ylabel("Frequency")
    plt.show()

# Add other visualization-related functions here.