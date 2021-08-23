from django.urls import path
from . import views

"""
urls for the Expense Tracker App
"""

urlpatterns = [
	path('',  views.ReportView.as_view(), name="report" ),
	path('add/', views.add, name="add"),
	path('year/', views.yearExpense, name="year_exp"),
	path('month/prev/', views.prevMonthExpense, name="prev_month_exp"),
	path('month/current/', views.currentMonthExpense, name="current_month_exp"),
	path('cat/<slug:category>/', views.catExpense, name="cat_exp"),
]