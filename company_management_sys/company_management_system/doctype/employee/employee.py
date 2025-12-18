# Copyright (c) 2025, Karim Moharm and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document
from datetime import date

class Employee(Document):
	def validate(self):
		self.calculate_days_employed()


	def calculate_days_employed(self):
		if self.hired_on:
			today = date.today()
			self.days_employed = (today - self.hired_on).days
		else:	
			self.days_employed = 0



