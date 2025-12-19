# Copyright (c) 2025, Karim Moharm and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from datetime import datetime

class Employee(Document):
	def validate(self):
		self.calculate_days_employed()


	def on_trash(self):
		update_company_fields(self.company)
		update_dept_fields(self.department)



	def after_insert(self):
		update_company_fields(self.company)
		update_dept_fields(self.department)



	def calculate_days_employed(self):
		if self.hired_on:
			today = datetime.now()
			hired_date = datetime.strptime(self.hired_on, '%Y-%m-%d')
			days = (today - hired_date).days
			if days > 0:
				self.days_employed = days
			else:
				self.days_employed = 0



def update_company_fields(company_name):
	if not company_name:
		return 
	
	emp_count = frappe.db.count('Employee', {'company': company_name})
	frappe.db.set_value(
		'Company',
		company_name,
		'number_of_employees',
		emp_count
	)

def update_dept_fields(dept_name):
	if not dept_name:
		return
	
	emp_count = frappe.db.count('Employee', {'department': dept_name})
	frappe.db.set_value(
		'Department',
		dept_name,
		'number_of_employees',
		emp_count
	)