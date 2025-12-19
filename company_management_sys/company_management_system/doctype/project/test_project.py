# Copyright (c) 2025, Karim Moharm and Contributors
# See license.txt

import frappe
from frappe.tests import IntegrationTestCase
from frappe.tests.utils import FrappeTestCase



# On IntegrationTestCase, the doctype test records and all
# link-field test record dependencies are recursively loaded
# Use these module variables to add/remove to/from that list
EXTRA_TEST_RECORD_DEPENDENCIES = []  # eg. ["User"]
IGNORE_TEST_RECORD_DEPENDENCIES = []  # eg. ["User"]



class TestProject(FrappeTestCase):
	def setUp(self):
		self.company = frappe.get_doc({
			"doctype": "Company",
			"company_name": "test company"
		}).insert()

		# Create department
		self.dept = frappe.get_doc({
			"doctype": "Department",
			"department_name": "test dept",
			"company": self.company.name
		}).insert()

		# Create first project
		self.project = frappe.get_doc({
			"doctype": "Project",
			"project_name": "Project 1",
			"company": self.company.name,
			"department": self.dept.name,
			"description": "a simple project description",
			"start_date": "2025-10-20"
		}).insert()

	def tearDown(self):
		# Delete all projects safely (triggers hooks)
		frappe.db.delete("Project", {"company": self.company.name})

		if self.dept:
			self.dept.delete()

		if self.company:
			self.company.delete()




	def test_update_project_for_company(self):
		"""
		Test updating number_of_projects for company
		"""
		self.company.reload()
		self.assertEqual(self.company.number_of_projects, 1)

		# Add more projects
		self.create_projects(3)
		self.company.reload()
		self.assertEqual(self.company.number_of_projects, 4)

		# Delete one project
		self.project.delete()
		self.company.reload()
		self.assertEqual(self.company.number_of_projects, 3)



	def test_update_project_for_department(self):
		"""
		Test updating number_of_projects for department
		"""
		self.dept.reload()
		self.assertEqual(self.dept.number_of_projects, 1)

		# Add more projects
		self.create_projects(2)
		self.dept.reload()
		self.assertEqual(self.dept.number_of_projects, 3)

		# Delete one project
		self.project.delete()
		self.dept.reload()
		self.assertEqual(self.dept.number_of_projects, 2)




	def create_projects(self, count=1):
		for i in range(count):
			frappe.get_doc({
				"doctype": "Project",
				"project_name": f"Project {i + 2}",
				"company": self.company.name,
				"department": self.dept.name,
				"description": "a simple project description",
				"start_date": f"2025-10-{i}"
			}).insert()



