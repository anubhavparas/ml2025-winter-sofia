"""
@author: Anubhav Paras

This program implements kNN classification with grid search to find the optimal k value.
It reads training and test data points where:
- x is the input feature (real number)
- y is the class label (non-negative integer)
The program:
1. Reads training data (N points)
2. Reads test data (M points)
3. Uses GridSearchCV to find the best k value
4. Outputs the best k and corresponding test accuracy
"""
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import GridSearchCV
from input_reader import InputReader

def read_data_set(size: int, set_name: str) -> tuple[np.ndarray, np.ndarray]:
    """Read a set of data points (x, y pairs).
    Args:
        size (int): Number of points to read.
        set_name (str): Name of the dataset (for prompts)
        
    Returns:
        tuple[np.ndarray, np.ndarray]: Features (X) and labels (y)
    """
    X = np.zeros(size)
    y = np.zeros(size, dtype=int)
    
    for i in range(size):
        X[i] = InputReader.read_float(f"Enter x value for {set_name} point {i+1}: ")
        y[i] = InputReader.read_int(f"Enter y value (class label) for {set_name} point {i+1}: ", min_value=0)
    
    # Compatible with scikit-learn's API.
    return X.reshape(-1, 1), y

def main():
    # Read training data.
    N = InputReader.read_int("Enter N (number of training points): ", min_value=1)
    X_train, y_train = read_data_set(N, "training")
    
    # Read test data.
    M = InputReader.read_int("Enter M (number of test points): ", min_value=1)
    X_test, y_test = read_data_set(M, "test")
    
    # Define parameter grid for k values.
    # Tests k values from 1 to 10.
    param_grid = {'n_neighbors': range(1, 11)}
    
    # Create and train the model with GridSearchCV
    knn = KNeighborsClassifier()
    grid_search = GridSearchCV(knn, param_grid, cv=5, scoring='accuracy')
    grid_search.fit(X_train, y_train)
    
    # Get the best k and its accuracy
    best_k = grid_search.best_params_['n_neighbors']
    best_accuracy = grid_search.score(X_test, y_test)
    
    # Output results
    print(f"\nBest k value: {best_k}")
    print(f"Test accuracy: {best_accuracy}")

if __name__ == "__main__":
    main()
