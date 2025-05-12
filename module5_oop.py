"""
This program reads a positive integer N from the user, then reads N numbers from the user, and then reads a number X from the user.
It then searches for X in the list of numbers and prints the position of X in the list. If X is not found, it prints -1.
"""
class NumberSearchManager:
    def __init__(self, N):
        self.N = N
        self.numbers = []

        # Use a set to store the numbers for efficient lookup:
        #   O(1) time complexity for lookup as compared to O(n) for list
        self.numbers_set = set()
    
    def set_N(self, N):
        """
        Set the number of numbers to read.
        """
        self.N = N

    def check_valid_input(self, N, should_be_positive=True):
        """
        Check if the input is a valid integer.
        If should_be_positive is True, check if the integer is positive.
        """
        # Check if the input string can be converted to an integer
        try:
            N = int(N)
        except ValueError:
            print("Input must be an integer. Please try again.")
            return False
        
        if should_be_positive and N <= 0:
            print("Input must be a positive integer. Please try again.")
            return False
        
        return True

    def read_numbers(self):
        """
        Read N numbers from user and store them in the list and set.
        """
        i = 0
        while i < self.N:
            num = input(f"Enter number {i+1}: ")
            if self.check_valid_input(num, should_be_positive=False):
                num = int(num)
                self.numbers.append(num)
                self.numbers_set.add(num)
                i += 1

    def search_number(self, X):
        """
        Search for X in the list and print its position.
        """
        print(f"\nThe numbers in the list are: {self.numbers}")
        if X in self.numbers_set:
            print(f"\nNumber X={X} found!")
            print(self.numbers.index(X) + 1)
        else:
            print(f"\nNumber {X} not found in the list.")
            print(-1)

def main():
    """
    Main function to read N, N numbers, and X from user and search for X in the list.
    """
    N = input("Enter a positive integer N: ")
    manager = NumberSearchManager(N)
    
    # Check if N is a number
    if not manager.check_valid_input(N):
        return
    manager.set_N(int(N))

    # Read N numbers from user
    manager.read_numbers()

    # Read X and find its position
    X = input("Enter number X to search for: ")
    if not manager.check_valid_input(X, should_be_positive=False):
        return
    X = int(X)

    # Search for X in the list
    manager.search_number(X)

if __name__ == "__main__":
    main()

