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

def process_coefficients(coefficients):
    """
    Process coefficients according to the specified rules.
    """
    lhs_terms = []
    rhs_terms = []
    rhs_value = 0.0

    for var, coeff in coefficients.items():
        whole_part = int(coeff)
        fractional_part = coeff - whole_part
        
        # Split into fractional and whole parts
        if fractional_part != 0:
            lhs_terms.append(f"{fractional_part:+.2f} {var}")
        if whole_part != 0:
            rhs_terms.append(f"{-whole_part:+.2f} {var}")
            rhs_value += whole_part

    # Set all fractional parts on LHS to equal the fractional RHS
    lhs_equation = " + ".join(lhs_terms) + f" = {rhs_value - int(rhs_value):.2f}"
    rhs_terms_equation = " + ".join(rhs_terms) + f" + {rhs_value - int(rhs_value):.2f}"
    inequality_equation = " + ".join(lhs_terms) + f" + {rhs_value - int(rhs_value):.2f} <= 0"

    return lhs_equation, rhs_terms_equation, inequality_equation

def main():
    # Prompt the user for input
    input_str = input("Enter the coefficients and variables (e.g., '1 X1 0 X2 -1.25 S1 0.25 S2 3.75'): ")
    
    # Parsing the input
    coefficients = parse_input(input_str)
    print("Parsed coefficients:", coefficients)

    # Process the coefficients
    lhs_equation, rhs_terms_equation, inequality_equation = process_coefficients(coefficients)
    print("Resulting LHS equation:", lhs_equation)
    print("Resulting RHS terms equation:", rhs_terms_equation)
    print("Resulting inequality:", inequality_equation)

# Run the main function
if __name__ == "__main__":
    main()
