import frappe
from frappe.tests.utils import FrappeTestCase


class TestDepartment(FrappeTestCase):
	"""test cases for Department docType
	"""
	

	def setUp(self):
		self.company = frappe.get_doc({
			"doctype": "Company",
			"company_name": "test company"
		}).insert()

		self.dept = frappe.get_doc({
			"doctype": "Department",
			"department_name": "dept test",
			"company": "test company",
		}).insert()
	
	def tearDown(self):
		if self.dept:
			self.dept.delete()
		if self.company:
			self.company.delete()
		
	def test_create_dept(self):
		self.assertEqual(self.dept.department_name, "dept test")
		self.assertEqual(self.dept.company, self.company.name)
	

	def test_same_department_different_company(self):
		company2 = frappe.get_doc({
			"doctype": "Company",
			"company_name": "second company"
		}).insert()

		dept2 = frappe.get_doc({
			"doctype": "Department",
			"department_name": "dept test",
			"company": "second company",
		}).insert()

		self.assertEqual(dept2.department_name, "dept test")

	def test_unique_department_same_company(self):
		with self.assertRaises(frappe.exceptions.DuplicateEntryError):
			frappe.get_doc({
			"doctype": "Department",
			"department_name": "dept test",
			"company": self.company.name,
			}).insert()

	def test_calculate_dept_counts(self):
		# create employee
		empl = frappe.get_doc({
			"doctype": "Employee",
			"employee_name": "karim",
			"department": self.dept.name,
			"company": self.company.name,
			"email_address": "karim@me.com",
			"mobile_number": "+201111111112",

		}).insert()
		# create project
		project = frappe.get_doc({
			"doctype": "Project",
			"project_name":  "test project",
			"description": "this is desc",
			"start_date": "2025-12-14",
			"department": self.dept.name,
			"company": self.company.name,
		}).insert()

		self.dept.calculate_dept_counts()
		self.dept.reload()
		
		self.assertEqual(self.dept.number_of_employees, 1)
		self.assertEqual(self.dept.number_of_projects, 1)

		project.delete()
		empl.delete()


	def test_required_fields(self):
			"""
			Test that required fields are enforced.
			"""
			# without department name
			with self.assertRaises(frappe.exceptions.ValidationError):
				department = frappe.get_doc({
					"doctype": "Department",
					"company": self.company.name
				}).insert()

			# witout the company
			with self.assertRaises(frappe.exceptions.ValidationError):
				dept = frappe.get_doc({
					"doctype": "Department",
					"department_name": "test dept"
				}).insert()

			