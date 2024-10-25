# Rule Engine Application

## Overview

The **Rule Engine Application** is a Django-based web application designed to check user eligibility based on specified rules. Users can create, edit, and evaluate rules written in a SQL-like syntax. The application evaluates user input against these rules, providing instant feedback on eligibility.

## Features

- **Home Page**: A user-friendly interface to input user details: age, department, salary, and experience.
- **Rule Creation**: Users can create custom eligibility rules using an SQL-like syntax.
- **Rule Editing**: Users can view existing rules, modify them, or delete rules as needed.
- **Eligibility Check**: The application evaluates user inputs against all stored rules and provides feedback.
- **Default Values**: If no rules are defined in the database, the application uses default values for eligibility checks.
- **Responsive Design**: The application has a colorful and attractive UI, enhancing user experience.

## Technologies Used

- **Python**: The primary programming language used to develop the backend logic.
- **Django**: The web framework used to build the application.
- **HTML/CSS**: For creating the user interface.
- **JavaScript**: For enhancing interactivity in the web application.
- **SQLite**: The database used for storing rules and user input data.

## How It Works

1. **Home Page**:
   - Users enter their details (age, department, salary, experience) in the input fields.
   - Clicking the "Check Eligibility" button triggers the evaluation process.

2. **Rule Evaluation**:
   - The application retrieves rules from the database.
   - If no rules exist, default conditions are applied:
     - Age > 0
     - Department can be any string
     - Salary > 0
     - Experience >= 0
   - If rules exist, user input is evaluated against these rules using logical operators (AND, OR).

3. **Creating Rules**:
   - Users can navigate to the "Create Rule" tab and enter rules in an SQL-like syntax.
   - The application parses the entered rules to identify conditions and stores them in the database.

4. **Editing Rules**:
   - Users can view existing rules in the "Edit Rule" tab.
   - Options are available to modify or delete rules.

5. **Feedback**:
   - After evaluating the user input against the rules, the application displays "Congratulations!" if the user meets the criteria, otherwise it shows "Sorry!".

## Installation

To set up the project locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/BhargavNarendraRaju/Zeotap_SDE_Assignment.git

### Saving and Committing

```markdown
### Saving and Committing

1. **Create a file** named `README.md` in your project directory.
2. **Copy and paste** the above content into the file.
3. **Save the file**.

Then, you can add, commit, and push it to your GitHub repository:
```bash
git add README.md
git commit -m "Add README file with project description"
git push origin main  # or 'master' if your default branch is 'master'


You can use this structured format for your `README.md` file, making it easy to read and follow!

