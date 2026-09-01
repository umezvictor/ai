def greeting():
    print("Hi there")


def calculate_pi():
    """
    Calculate pi to the 5th decimal digit using the Machin formula.
    Machin's formula: pi/4 = 4*arctan(1/5) - arctan(1/239)
    Returns pi accurate to at least 5 decimal places (3.14159)
    """
    def arctan(x, num_terms=50):
        """Calculate arctan using Taylor series expansion"""
        result = 0
        for n in range(num_terms):
            term = ((-1) ** n) * (x ** (2 * n + 1)) / (2 * n + 1)
            result += term
        return result
    
    # Machin's formula for pi
    pi = 4 * (4 * arctan(1/5, 50) - arctan(1/239, 50))
    
    # Round to 5 decimal places
    pi_rounded = round(pi, 5)
    
    return pi_rounded


if __name__ == "__main__":
    pi_value = calculate_pi()
    print(f"Pi calculated to 5 decimal places: {pi_value}")