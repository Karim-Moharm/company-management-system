# Copyright (c) 2025, Karim Moharm and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from datetime import datetime
from frappe.utils import getdate, nowdate, date_diff

class Employee(Document):
	def validate(self):
		self.calculate_days_employed()

	def after_insert(self):
		update_company_fields(self.company)
		update_dept_fields(self.department)

	def on_trash(self):
		update_company_fields(self.company)
		update_dept_fields(self.department)




	def calculate_days_employed(self):
		if not self.hired_on:
			self.days_employed = None
			return

		hired_date = getdate(self.hired_on)
		today = getdate(nowdate())

		self.days_employed = date_diff(today, hired_date)


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