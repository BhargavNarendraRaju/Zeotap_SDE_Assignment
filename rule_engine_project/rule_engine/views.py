import re
from django.shortcuts import render, redirect
from .models import Rule


def evaluate_single_condition(condition, user_input):
    match = re.match(r'(\w+)\s*([<>=!]+)\s*(.+)', condition.strip())
    if not match:
        return False  # Invalid condition format

    variable, operator, value = match.groups()

    if variable in ['age', 'salary', 'experience']:
        value = float(value)
    elif variable == 'department':
        value = value.strip().strip("'")

    user_value = user_input.get(variable)

    if user_value is None:
        return False

    if operator == '>':
        return user_value > value
    elif operator == '<':
        return user_value < value
    elif operator == '=':
        return user_value == value
    elif operator == '>=':
        return user_value >= value
    elif operator == '<=':
        return user_value <= value
    elif operator == '!=':
        return user_value != value

    return False


def evaluate_rule(rule_query, user_input):
    try:
        sanitized_query = rule_query
        for key, value in user_input.items():
            if isinstance(value, str):
                sanitized_query = sanitized_query.replace(key, f"'{value}'")
            else:
                sanitized_query = sanitized_query.replace(key, str(value))

        return eval(sanitized_query)
    except Exception as e:
        print(f"Error evaluating rule: {e}")
        return False


def home(request):
    if request.method == "POST":
        age = int(request.POST['age'])
        department = request.POST['department']
        salary = float(request.POST['salary'])
        experience = float(request.POST['experience'])

        user_input = {
            'age': age,
            'department': department,
            'salary': salary,
            'experience': experience,
        }

        # Check if the two specific rules are satisfied
        rule1 = "((age > 30 AND department = 'Sales') OR (age < 25 AND department = 'Marketing')) AND (salary > 50000 OR experience > 5)"
        rule2 = "((age > 30 AND department = 'Marketing')) AND (salary > 20000 OR experience > 5)"

        if evaluate_rule(rule1, user_input) or evaluate_rule(rule2, user_input):
            return render(request, 'home.html', {'result': "Congratulations!"})

        # Check against database rules
        rules = Rule.objects.all()
        if not rules.exists():
            if age > 0 and salary > 0 and experience >= 0:
                return render(request, 'home.html', {'result': "Congratulations!"})
            else:
                return render(request, 'home.html', {'result': "Sorry!"})

        for rule in rules:
            if evaluate_rule(rule.query, user_input):
                return render(request, 'home.html', {'result': "Congratulations!"})

        return render(request, 'home.html', {'result': "Sorry!"})

    return render(request, 'home.html')


def create_rule(request):
    if request.method == "POST":
        rule_query = request.POST['rule_query']
        Rule.objects.create(query=rule_query)
        return redirect('create_rule')

    return render(request, 'create_rule.html')


def edit_rule(request):
    rules = Rule.objects.all()
    if request.method == "POST":
        rule_id = request.POST.get('rule_id')
        Rule.objects.filter(id=rule_id).delete()
        return redirect('edit_rule')

    return render(request, 'edit_rule.html', {'rules': rules})
