# Copyright (c) 2025, Karim Moharm and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Department(Document):

	def validate(self):
		self.calculate_dept_counts()
	
	def on_load(self):
		self.calculate_dept_counts()

	
	def calculate_dept_counts(self):
		"""
		Count related records for this department
		"""
		if not self.name:
			self.number_of_employees = 0
			self.number_of_projects = 0
			return
		
		self.number_of_employees = frappe.db.count('Employee', {'department': self.name})
		self.number_of_projects = frappe.db.count('Project', {'department': self.name})

	
	def after_insert(self):
		update_company_fields(self.company)
	
	def on_trash(self):
		update_company_fields(self.company)
	


def update_company_fields(company_name):
	if not company_name:
		return
	
	dept_count = frappe.db.count('Department', {'company': company_name})
	emp_count = frappe.db.count('Employee', {'company': company_name})
	proj_count = frappe.db.count('Project', {'company': company_name})

	frappe.db.set_value(
		'Company',
		company_name,
		{'number_of_departments': dept_count},
		{'number_of_employees': emp_count},
		{'number_of_projects': proj_count}
	)
