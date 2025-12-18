# Copyright (c) 2025, Karim Moharm and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Company(Document):
	def on_load(self):
		self.calculate_counts()
	
	def calculate_counts(self):
		self.number_of_departements = frappe.db.count(
			'Departement', {
				'company': self.name
			}
		)
		self.number_of_employees = frappe.db.count(
			'Employee', {
				'company': self.name
			}
		)
		self.number_of_projects = frappe.db.count(
			'Project', {
				'company': self.name
			}
		)


	def update_company_counts(doc, method=None):
		"""
		Called from hooks when Department / Employee or Project is created/deleted
		"""
		if hasattr(doc, 'company') and doc.company:
			company = frappe.get_doc('Company', doc.company)
			company.calculate_counts()
			company.save(ignore_permissions=True)


