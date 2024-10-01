import re

def parse_input(input_str):
    """
    Parse the input string to extract coefficients and variables.
    """
    # Regex to match variable pattern
    pattern = r"(-?\d+\.?\d*)\s*(X\d+|S\d+)"
    matches = re.findall(pattern, input_str)
    
    coefficients = {}
    for match in matches:
        coefficient, variable = match
        coefficients[variable] = float(coefficient)
    
    return coefficients

def adjust_negative_fractions(coefficients):
    """
    Adjust negative fractional coefficients to the next largest whole number.
    """
    adjusted_coefficients = {}
    whole_terms = []
    fractional_terms = []

    for var, coeff in coefficients.items():
        whole_part = int(coeff)
        fractional_part = coeff - whole_part
        
        if fractional_part < 0:
            # If the fractional part is negative, adjust to the next largest negative whole number
            new_whole_part = whole_part - 1
            new_fractional_part = fractional_part + 1
            adjusted_coefficients[var] = (new_whole_part, new_fractional_part)
        else:
            adjusted_coefficients[var] = (whole_part, fractional_part)
    
    return adjusted_coefficients

def construct_equation(adjusted_coefficients):
    """
    Construct the equations based on adjusted coefficients.
    """
    lhs_terms = []
    rhs_terms = []
    fractional_rhs = 0.0

    for var, (whole_part, fractional_part) in adjusted_coefficients.items():
        if fractional_part != 0:
            lhs_terms.append(f"{fractional_part:+.2f} {var}")
        if whole_part != 0:
            rhs_terms.append(f"{-whole_part:+d} {var}")
            fractional_rhs += fractional_part

    lhs_equation = " + ".join(lhs_terms) + " = 0"
    inequality_equation = " + ".join(lhs_terms) + f" <= {-fractional_rhs:.2f}"

    return lhs_equation, inequality_equation

def main():
    # Prompt the user for input
    input_str = input("Enter the coefficients and variables (e.g., '1 X1 0 X2 -1.25 S1 0.25 S2 3.75'): ")
    
    # Parsing the input
    coefficients = parse_input(input_str)
    print("Parsed coefficients:", coefficients)

    # Adjust negative fractions to next largest negative whole number
    adjusted_coefficients = adjust_negative_fractions(coefficients)
    print("Adjusted coefficients:", adjusted_coefficients)

    # Construct the resulting equations
    lhs_equation, inequality_equation = construct_equation(adjusted_coefficients)
    print("Resulting LHS equation:", lhs_equation)
    print("Resulting inequality:", inequality_equation)

# Run the main function
if __name__ == "__main__":
    main()
