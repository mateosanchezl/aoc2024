from itertools import product

def evaluate_expression(numbers, operators):
    """Evaluate the expression formed by numbers and operators left-to-right."""
    result = numbers[0]
    for i, op in enumerate(operators):
        if op == '+':
            result += numbers[i + 1]
        elif op == '*':
            result *= numbers[i + 1]
        elif op == '||':
            result = int(str(result) + str(numbers[i + 1]))
    return result

def possible_results(numbers):
    """Generate all possible results by inserting '+', '*', and '||' between numbers."""
    operators = ['+', '*', '||']
    all_results = set()

    # Generate all combinations of operators
    for ops in product(operators, repeat=len(numbers) - 1):
        result = evaluate_expression(numbers, ops)
        all_results.add(result)

    return all_results

def find_valid_calibrations(filename):
    """Find and sum all valid test values from the input file."""
    total_calibration_result = 0

    with open(filename, 'r') as file:
        for line in file:
            target, *numbers = line.strip().split(':')
            target = int(target)
            numbers = list(map(int, numbers[0].split()))

            # Check if target is in possible results
            if target in possible_results(numbers):
                total_calibration_result += target

    return total_calibration_result

if __name__ == "__main__":
    input_file = "day7/input.txt"  # Replace with the path to your input file
    result = find_valid_calibrations(input_file)
    print("Total calibration result:", result)
