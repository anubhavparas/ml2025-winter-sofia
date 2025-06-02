"""
@author: Anubhav Paras

This program calculates Precision and Recall using scikit-learn metrics.
It reads N points (x,y) where:
- x is the ground truth class label (0 or 1)
- y is the predicted class label (0 or 1)
The program:
1. asks the user for input N (positive integer) and reads it.
2. asks the user for input N (x, y) points (one by one) and reads all of them:
   - first: x value (ground truth, 0 or 1)
   - then: y value (prediction, 0 or 1)
3. outputs the Precision and Recall based on the inputs.
"""
import numpy as np
from sklearn.metrics import precision_score, recall_score
from input_reader import InputReader

def main():
    # Read N
    N = InputReader.read_int("Enter N (positive integer): ", min_value=1)
    
    # Pre-allocate NumPy arrays for ground truth and predictions.
    y_true = np.zeros(N, dtype=int)
    y_pred = np.zeros(N, dtype=int)
    
    # Read N points (x, y).
    for i in range(N):
        # Read ground truth (x).
        y_true[i] = InputReader.read_int(f"Enter ground truth (0 or 1) for point {i+1}: ", min_value=0, max_value=1)
        
        # Read prediction (y).
        y_pred[i] = InputReader.read_int(f"Enter prediction (0 or 1) for point {i+1}: ", min_value=0, max_value=1)
    
    # Calculate Precision and Recall using scikit-learn.
    precision = precision_score(y_true, y_pred)
    recall = recall_score(y_true, y_pred)
    
    # Output results.
    print(f"\nPrecision: {precision:.4f}")
    print(f"Recall: {recall:.4f}")

if __name__ == "__main__":
    main()
