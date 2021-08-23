# import form class from django
from django import forms
from .models import Expense
  
# create a ModelForm
class ExpenseForm(forms.ModelForm):
    """
    specify the name of model to use
    """
    class Meta:
        model = Expense
        fields = "__all__"