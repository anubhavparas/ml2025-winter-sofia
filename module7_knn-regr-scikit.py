"""
@author: Anubhav Paras

This program implements k-NN Regression using NumPy for data handling and scikit-learn for ML.
It reads N points (x,y) and performs k-NN regression for a given input X.
The program:
1. asks the user for input N (positive integer) and reads it.
2. asks the user for input k (positive integer) and reads it.
3. asks the user for input N (x, y) points (one by one) and reads all of them: 
   - first: x value, 
   - then: y value for every point one by one. 
   - X and Y are the real numbers.
4. asks the user for input X and reads it.
5. outputs the result (Y) of k-NN Regression if k <= N, or any error message otherwise.
6. additionally provides the variance of labels in the training dataset.
"""
import numpy as np
from sklearn.neighbors import KNeighborsRegressor
from input_reader import InputReader

def main():
    # Read N.
    N = InputReader.read_int("Enter N (positive integer): ", min_value=1)
    
    # Read k.
    k = InputReader.read_int("Enter k (positive integer): ", min_value=1, max_value=N)
    
    # Pre-allocate NumPy arrays for X and y values.
    X_train = np.zeros(N)
    y_train = np.zeros(N)
    
    # Read N points (x, y).
    for i in range(N):
        X_train[i] = InputReader.read_float(f"Enter x value for point {i+1}: ")
        y_train[i] = InputReader.read_float(f"Enter y value for point {i+1}: ")
    
    # Reshape X for scikit-learn.
    X_train = X_train.reshape(-1, 1)
    
    
    # Initialize and train KNNRegressor from scikit-learn
    knn = KNeighborsRegressor(n_neighbors=k)
    knn.fit(X_train, y_train)
    
    # Read X and predict Y
    X = InputReader.read_float("Enter X value to predict Y: ")
    X = np.array([[X]])  # Reshape for scikit-learn
    Y = knn.predict(X)[0]
    print(f"\nPredicted Y value: {Y}")

    # Calculate and display variance of labels
    label_variance = np.var(y_train)
    print(f"\nVariance of labels in training dataset: {label_variance}")
    

if __name__ == "__main__":
    main()
