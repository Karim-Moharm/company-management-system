# Copyright (c) 2025, Karim Moharm and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Company(Document):
	def validate(self):
		self.calculate_company_counts()
	
	def on_load(self):
		self.calculate_company_counts()
	

	def calculate_company_counts(self):
		if not self.name:
			self.number_of_departments = 0
			self.number_of_employees = 0
			self.number_of_projects = 0
			return
		
		self.number_of_departments = frappe.db.count('Department', {'company': self.name})
		self.number_of_employees = frappe.db.count('Employee', {'company': self.name})
		self.number_of_projects = frappe.db.count('Project', {'company': self.name})

