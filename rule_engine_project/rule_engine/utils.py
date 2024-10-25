def evaluate_rule(parsed_rule, age, department, salary, experience):
    # Logic to evaluate the rule against the user inputs
    # Example of simple evaluation
    context = {
        'age': int(age),
        'department': department,
        'salary': float(salary),
        'experience': float(experience),
    }

    # You need to implement this logic based on your AST
    # A simple evaluation might look like this:
    if parsed_rule.type == 'operator':
        left_value = context[parsed_rule.left.value]
        right_value = context[parsed_rule.right.value]
        if parsed_rule.value == '>':
            return left_value > right_value
        elif parsed_rule.value == '<':
            return left_value < right_value
        # Implement other operators as needed

    return False
