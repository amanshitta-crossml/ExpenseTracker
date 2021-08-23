# Epic for Expense Tracker app

1. Design models Expense and Budget
	i. Expense

	- Category, Spent, Date, Comment
	- functions to get specific reault set

2. URLS 

- 'expense/' --> VIEW[view.all_expense]
- 'expense/<int:year>' --> VIEW[view.year_expense]
- 'expense/<int:year>/<int:month>' --> VIEW[view.month_expense]


3. Views

- all_expense()
- year_expense(year)
- month_expense(month_expense)


4. Templates

- base template - base.html
- Default undex.html
- year_rep.html
- month_rep.html
