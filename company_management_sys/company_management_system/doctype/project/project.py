# Copyright (c) 2025, Karim Moharm and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Project(Document):
	def after_insert(self):
		"""
		After creating a project
		"""
		update_company_count(self.company)
		update_department_count(self.dept)

	def on_trash(self):
		"""
		after deleting a project
		"""
		update_company_count(self.company)
		update_department_count(self.dept)



def update_company_count(company_name):
	if not company_name:
		return 

	proj_count = frappe.db.count('Project', {'company': company_name})
	frappe.db.set_value(
		'Company',
		company_name,
		'number_of_projects',
		proj_count
	)


def update_department_count(dept_name):
	if not dept_name:
		return 

	proj_count = frappe.db.count('Project', {'Department': dept_name})
	frappe.db.set_value(
		'Department',
		dept_name,
		'number_of_projects',
		proj_count
	)