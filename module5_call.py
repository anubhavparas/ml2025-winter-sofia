"""
This program reads a positive integer N from the user, then reads N numbers from the user, and then reads a number X from the user.
It then searches for X in the list of numbers and prints the position of X in the list. If X is not found, it prints -1.
"""
from module5_oop import NumberSearchManager

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


