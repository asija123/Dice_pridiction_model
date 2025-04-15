# train_model.py
import numpy as np
import pickle
from sklearn.neighbors import KNeighborsRegressor
import os

def generate_dice_sums(n=1000):
    return np.random.randint(1, 7, size=(n, 3)).sum(axis=1)

def prepare_sequences(sums, window_size=3):
    X, y = [], []
    for i in range(len(sums) - window_size):
        X.append(sums[i:i+window_size])
        y.append(sums[i+window_size])
    return np.array(X), np.array(y)

# Generate random data
sums = generate_dice_sums(1000)
X, y = prepare_sequences(sums)

# Train the KNN model
knn = KNeighborsRegressor(n_neighbors=3)
knn.fit(X, y)

# Save model
os.makedirs("model", exist_ok=True)
with open("model/knn_model.pkl", "wb") as f:
    pickle.dump(knn, f)

print("Model training complete and saved.")
