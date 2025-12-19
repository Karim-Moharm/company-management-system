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



	def check_duplicate(self):
		"""
		Ensure that the department name is unique within the same company.
		Rules:
		- A department name must be unique for the same company.
		- The same department name can exist in different companies.
		"""
		exists = frappe.db.exists('Department', {
			'department_name': self.department_name,
			'company': self.company,
			'name': ['!=', self.name]
		})
		
		if exists:
				frappe.throw(f'Department "{self.department_name}" already exists in {self.company}')
	


def update_company_fields(company_name):
	if not company_name:
		return
	
	dept_count = frappe.db.count('Department', {'company': company_name})

	frappe.db.set_value(
		'Company',
		company_name,
		'number_of_departments', 
		dept_count
	)
