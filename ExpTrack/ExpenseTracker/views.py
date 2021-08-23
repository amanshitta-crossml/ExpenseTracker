from django.shortcuts import render, redirect
from django.views import generic
from .models import Expense
from .forms import ExpenseForm
import datetime

# Create your views here.


class ReportView(generic.ListView):
	"""
	Generic List view for getting all expenses
	"""

	template_name = 'ExpenseTracker/report.html'
	context_object_name = 'expenses'

	def get_queryset(self):
		"""
		the data to be passed onto the template is called 
		from here
		"""
		return Expense.objects.all()


def add(request):
	"""
	check the method of request
	"""
	form = ExpenseForm(request.POST or None, request.FILES or None)

	if request.method == "POST":
		if form.is_valid():
			form.save()

		return redirect('report')
	else:
		context = {'form':form}

		return render(request, 'ExpenseTracker/add.html', context)


def prevMonthExpense(request):
	"""
	function to display previous month expenses
	"""

	prev_month = datetime.date.today().strftime("%m")
	# month_name = datetime.date.today().strftime("%B")
	month_name = datetime.date(2021,int(prev_month)-1, 1).strftime('%B')

	expense_of_month = Expense.objects.filter(date__month=int(prev_month)-1)

	context = {'expenses':expense_of_month,'month_name':month_name}

	return render(request, 'ExpenseTracker/month_exp.html',context)




def currentMonthExpense(request):
	"""
	function to display current month expenses
	"""
	
	current_month = datetime.date.today().strftime("%m")
	month_name = datetime.date.today().strftime("%B")
	expense_of_month = Expense.objects.filter(date__month=int(current_month))

	context = {'expenses':expense_of_month,'month_name':month_name}

	return render(request, 'ExpenseTracker/month_exp.html',context)



def yearExpense(request):
	"""
	function to display whole years expense
	"""
	
	year = datetime.date.today().strftime("%Y")
	
	expense_of_year = Expense.objects.filter(date__year=int(year))

	context = {'expenses':expense_of_year,'year':year}

	return render(request, 'ExpenseTracker/year.html',context)


def catExpense(request,category):
	"""
	function to display expense Category Based
	"""

	expenses = Expense.objects.get(category=category)
	breakpoint()
	print(expenses)
