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
