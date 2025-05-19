"""
@author: Anubhav Paras

This program implements k-NN Regression using NumPy and OOP principles.
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
"""
import numpy as np

class InputReader:
    """
    This class provides static methods to read and validate integer and float inputs.
    """
    @staticmethod
    def read_int(prompt: str, min_value: int = None, max_value: int = None) -> int:
        """Read and validate an integer input.
        Args:
            prompt (str): The prompt to display to the user.
            min_value (int, optional): The minimum value allowed. Defaults to None.
            max_value (int, optional): The maximum value allowed. Defaults to None.
        Returns:
            int: The validated integer input.
        """
        while True:
            try:
                value = int(input(prompt))
                if min_value is not None and value < min_value:
                    print(f"Value must be greater than or equal to {min_value}. Please try again.")
                    continue
                if max_value is not None and value > max_value:
                    print(f"Value must be less than or equal to {max_value}. Please try again.")
                    continue
                return value
            except ValueError:
                print("Invalid input. Please enter an integer.")

    @staticmethod
    def read_float(prompt: str) -> float:
        """Read and validate a float input.
        Args:
            prompt (str): The prompt to display to the user.
        Returns:
            float: The validated float input.
        """
        while True:
            try:
                return float(input(prompt))
            except ValueError:
                print("Invalid input. Please enter a real number.")

class KNNRegressor:
    """
    This class implements k-NN Regression using NumPy.
    """
    def __init__(self):
        """Initialize the KNNRegressor object."""
        self.X = None
        self.y = None
    
    def fit(self, X, y):
        """Store the training data X and y."""
        self.X = np.array(X)
        self.y = np.array(y)
        
        # Extra check to ensure X and y have the same length.
        if len(self.X) != len(self.y):
            raise ValueError("X and y must have the same length")
    
    def predict(self, X, k):
        """Perform k-NN regression for input X using k neighbors."""
        if self.X is None or self.y is None:
            raise ValueError("Model has not been trained yet. Call fit() first.")
        if k <= 0:
            raise ValueError("k must be positive")
        if k > len(self.X):
            raise ValueError(f"k ({k}) must be less than or equal to number of points ({len(self.X)})")
            
        # Calculate distances from X to all points.
        # For now we are using absolute distance, but we can use other distances.
        # We can use L2 distance (Euclidean distance) as well 
        #   but for 1D data it's the same as absolute distance.
        distances = np.abs(self.X - X)
        
        # Get indices of k nearest neighbors.
        k_indices = np.argsort(distances)[:k]
        
        # Get y values of k nearest neighbors.
        k_nearest_y = self.y[k_indices]
        
        # Calculate mean of y values (regression result).
        # We can also use weighted mean, where weights are inversely proportional to distance.
        #   In that case we can use np.average(k_nearest_y, weights=1/distances[k_indices]).
        # But for now we are using simple mean.
        return np.mean(k_nearest_y)

def main():
    # Read N.
    N = InputReader.read_int("Enter N (positive integer): ", min_value=1)
    
    # Read k.
    k = InputReader.read_int("Enter k (positive integer): ", min_value=1, max_value=N)
    
    # Read N points (x, y).
    X_train = []
    y_train = []
    for i in range(N):
        x = InputReader.read_float(f"Enter x value for point {i+1}: ")
        y = InputReader.read_float(f"Enter y value for point {i+1}: ")
        X_train.append(x)
        y_train.append(y)
    
    # Initialize and train KNNRegressor.
    knn = KNNRegressor()
    knn.fit(X_train, y_train)
    
    # Read X and predict Y.
    X = InputReader.read_float("Enter X value to predict Y: ")
    Y = knn.predict(X, k)
    print(f"\nPredicted Y value: {Y}")

if __name__ == "__main__":
    main()
