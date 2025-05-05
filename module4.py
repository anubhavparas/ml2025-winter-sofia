"""
This program reads a positive integer N from the user, then reads N numbers from the user, and then reads a number X from the user.
It then searches for X in the list of numbers and prints the position of X in the list. If X is not found, it prints -1.
"""
# Read N from user
def check_valid_input(N, should_be_positive=True):
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

def main():
    """
    Main function to read N, N numbers, and X from user and search for X in the list.
    """
    N = input("Enter a positive integer N: ")
    # Check if N is a number
    if not check_valid_input(N):
        return
    N = int(N)

    # Read N numbers from user
    numbers = []
    numbers_set = set()
    i = 0
    while i < N:
        num = input(f"Enter number {i+1}: ")
        # As X is mentioned to be an integer, we would accept other numbers as integers.
        # We can accept duplicates as well - As it is not mentioned that the numbers are unique.
        if check_valid_input(num, should_be_positive=False):
            num = int(num)
            numbers.append(num)
            numbers_set.add(num)
            i += 1

    # Read X and find its position
    X = input("Enter number X to search for: ")
    if not check_valid_input(X, should_be_positive=False):
        return
    X = int(X)

    # Search for X in the list
    # use index method to find the position of X
    print(f"\nThe numbers in the list are: {numbers}")
    if X in numbers_set:
        print(f"\nNumber X={X} found!")
        print(numbers.index(X) + 1)
    else:
        print(f"\nNumber {X} not found in the list.")
        print(-1)


if __name__ == "__main__":
    main()

