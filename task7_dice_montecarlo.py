import random
import matplotlib.pyplot as plt

def monte_carlo_dice(trials=100000):
    counts = {i: 0 for i in range(2, 13)}
    for _ in range(trials):
        s = random.randint(1,6)+random.randint(1,6)
        counts[s]+=1
    probs = {k: v/trials for k,v in counts.items()}
    return probs

if __name__ == "__main__":
    probs = monte_carlo_dice()
    print(probs)
    plt.bar(probs.keys(), probs.values())
    plt.show()
