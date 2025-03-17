# SKA Model Implementation

This repository contains the implementation of the SKA (Simulated Knowledge Acquisition) Model using the Iris dataset as a proof of concept.
"""
SKA (Simulated Knowledge Acquisition) Model Implementation for Iris Dataset Classification

The SKA model is a novel neural network architecture that learns through knowledge accumulation
rather than traditional backpropagation. Key characteristics:

1. Architecture:
   - Multi-layer network designed for the Iris dataset (4 input features -> 3 output classes)
   - Uses sigmoid activation for decision-making at each layer
   - Implements 4 layers: [16, 8, 6, 3] neurons

2. Learning Process:
   - Knowledge Accumulation: Uses tensor Z = Wx + b to accumulate knowledge
   - Decision Making: Transforms knowledge into decisions using sigmoid function
   - Entropy-based Updates: Updates weights based on entropy reduction between steps
   - No Backpropagation: Learning occurs through forward passes only

3. Update Mechanism:
   - Computes decision shifts (delta_D) between consecutive steps
   - Calculates entropy reduction using dot product of knowledge and decision shifts
   - Updates weights using entropy gradients and local computations
   - Learning rate controls the magnitude of weight updates

4. Application to Iris Dataset:
   - Input: 4 features (sepal length, sepal width, petal length, petal width)
   - Output: 3 classes (setosa, versicolor, virginica)
   - Uses 30 samples per class for training
   - Performs K=50 forward steps for knowledge accumulation
"""


## Project Structure

- `understand.ipynb`: Jupyter notebook containing research and analysis done to understand the SKA model implementation
- `test.ipynb`: Jupyter notebook with code to test the model using the Iris dataset
- `dataset.py`: Python script for dataset generation and preprocessing
- `SKA_model_update.py`: Final implementation of the SKA model using the Iris dataset

## Setup Instructions

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Installation

1. Clone the repository
```bash
git clone https://github.com/yourusername/SKA_Model.git
cd SKA_Model
```

2. Create and activate a virtual environment (recommended)
```bash
python -m venv venv
source venv/bin/activate  # For Mac/Linux
```

3. Install required packages
```bash
pip install -r requirements.txt
```

## Usage

1. To explore the research and understanding phase:
   - Open `understand.ipynb` in Jupyter Notebook/Lab
   ```bash
   jupyter notebook understand.ipynb
   ```

2. To run the model test with Iris dataset:
   - Open `test.ipynb` in Jupyter Notebook/Lab
   ```bash
   jupyter notebook test.ipynb
   ```

3. To generate custom datasets:
   ```bash
   python dataset.py
   ```

4. To run the final SKA model implementation:
   ```bash
   python SKA_model_update.py
   ```

## Files Description

### understand.ipynb
- Contains detailed research and analysis of the SKA model
- Includes theoretical background and implementation considerations
- Shows step-by-step development process

### test.ipynb
- Implementation of model testing using the Iris dataset
- Includes performance metrics and visualization
- Contains validation and testing procedures

### dataset.py
- Functions for dataset generation and preprocessing
- Data transformation and normalization utilities
- Dataset splitting and preparation methods

### SKA_model_update.py
- Final implementation of the SKA model
- Optimized code for Iris dataset classification
- Model training and evaluation procedures



## Contact

email : vivek.choudhry084@gmail.com
