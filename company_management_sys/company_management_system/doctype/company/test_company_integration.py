# Copyright (c) 2025, Karim Moharm and Contributors
# See license.txt

import frappe
from frappe.tests import IntegrationTestCase


# On IntegrationTestCase, the doctype test records and all
# link-field test record dependencies are recursively loaded
# Use these module variables to add/remove to/from that list
EXTRA_TEST_RECORD_DEPENDENCIES = []  # eg. ["User"]
IGNORE_TEST_RECORD_DEPENDENCIES = []  # eg. ["User"]



class IntegrationTestCompany(IntegrationTestCase):
	"""
	Integration tests for Company.
	Use this class for testing interactions between multiple components.
	"""

	def test_company_with_fields(self):
		"""
		integration test where we create a company create
		department, employee and projects linked to it
		"""
		company = frappe.get_doc({
			"doctype": "Company",
			"company_name": "test company"
		}).insert()
		# create department for that company
		dept = frappe.get_doc({
			"doctype": "Department",
			"department_name": "marketing",
			"company": company.name,
		}).insert()
		# create employee for that company
		empl = frappe.get_doc({

			"doctype": "Employee",
			"employee_name":  "ahmed",
			"email_address": "ahmed@me.com",
			"mobile_number": "+201111111112",
			"department": dept.name,
			"company": company.name,
		}).insert()
		# create project for that company
		project = frappe.get_doc({

			"doctype": "Project",
			"project_name":  "test project",
			"description": "this is desc",
			"start_date": "2025-12-14",
			"department": dept.name,
			"company": company.name,
		}).insert()

		company.reload()
		self.assertEqual(company.number_of_departments, 1)
		self.assertEqual(company.number_of_employees, 1)
		self.assertEqual(company.number_of_projects, 1)

		project.delete()
		empl.delete()
		dept.delete()
		company.delete()
