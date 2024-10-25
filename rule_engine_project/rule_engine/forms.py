from django import forms

class RuleForm(forms.Form):
    age = forms.CharField(label="Age Condition", max_length=10, required=False)  # Changed to CharField to accommodate operators like '<4'
    department = forms.CharField(label="Department Condition", max_length=100, required=False)
    salary = forms.CharField(label="Salary Condition", max_length=10, required=False)
    experience = forms.CharField(label="Experience Condition", max_length=10, required=False)

class EligibilityForm(forms.Form):
    age = forms.IntegerField(label="Age")
    department = forms.CharField(label="Department", max_length=100)
    salary = forms.IntegerField(label="Salary")
    experience = forms.IntegerField(label="Experience")
