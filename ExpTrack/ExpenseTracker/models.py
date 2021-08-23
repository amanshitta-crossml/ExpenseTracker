from django.db import models

# Create your models here.

# class User(models.Model):
# 	"""
# 	User Model for a user and his budget 
# 	"""
# 	name = models.CharField(max_length=72)
# 	budget = models.DecimalField(max_digits=10, decimal_places=2)

# 	def __str__(self):
# 		"""
# 		string representation for the object
# 		"""
# 		return self.name

class Expense(models.Model):
	CATEGORY_OF_EXPENSES = [
		('Travel','Travel'),
		('Education','Education'),
		('Gifts & Donations','Gifts & Donations'),
		('Investments','Investments'),
		('Bills & Utilities','Bills & Utilities'),
		('Food & Dining','Food & Dining'),
		('Health & Fitness','Health & Fitness'),
		('Personal Care','Personal Care'),
		('Fees & Charges','Fees & Charges'),
		('Others','Others')
	]
	# user = models.ManyToManyField(User)
	category = models.CharField(max_length=70, choices=CATEGORY_OF_EXPENSES, default = 'OT')
	spent = models.DecimalField(max_digits=7, decimal_places=2)
	date = models.DateTimeField()
	comment = models.TextField(max_length=300, null=True)


	def __str__(self):
		"""
		string representation for the object
		"""

		return (self.category)



