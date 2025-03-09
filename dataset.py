import torch
import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split

# Load the Iris dataset
iris = datasets.load_iris()
X, y = iris.data, iris.target  # Features and labels

# Convert to NumPy for easier processing
X = np.array(X, dtype=np.float32)
y = np.array(y, dtype=np.int64)

# Dictionary to track class counts
class_counts = {i: 0 for i in range(3)}  # 3 classes in Iris
subset = []

# Extract 30 samples per class
for features, label in zip(X, y):
    if class_counts[label] < 300:
        subset.append((torch.tensor(features), torch.tensor(label)))
        class_counts[label] += 1
    if all(count == 30 for count in class_counts.values()):
        break

# Save the dataset subset as a PyTorch tensor
torch.save(subset, "iris_subset_30_per_class.pt")

print(f"Saved {len(subset)} samples from the Iris dataset.")