# Copyright (c) 2025, Karim Moharm and Contributors
# See license.txt

import frappe
from frappe.tests import IntegrationTestCase
from frappe.tests.utils import FrappeTestCase
from datetime import  datetime

# On IntegrationTestCase, the doctype test records and all
# link-field test record dependencies are recursively loaded
# Use these module variables to add/remove to/from that list
EXTRA_TEST_RECORD_DEPENDENCIES = []  # eg. ["User"]
IGNORE_TEST_RECORD_DEPENDENCIES = []  # eg. ["User"]


class TestEmployee(FrappeTestCase):
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

		self.employee = frappe.get_doc({
			"doctype": "Employee",
			"employee_name": "ayser",
			"company": self.company.name,
			"department" : self.dept.name,
			"email_address": "ayser@a.com", 
			"mobile_number": "+201111111112",
		}).insert()

	def tearDown(self):
		if self.employee:
			# self.employee.delete()
			frappe.db.delete("Employee", {"company": self.company.name})
		if self.dept:
			self.dept.delete()
		if self.company:
			self.company.delete() 


	
	# def test_create_employee(self):
	# 	self.assertEqual(self.employee.employee_name, "ayser")
	# 	self.assertEqual(self.employee.email_address, "ayser@a.com")
	# 	self.assertEqual(self.employee.address, None)
	# 	self.assertEqual(self.employee.department, self.dept.name)


	# def test_unique_fields(self):
	# 	with self.assertRaises(frappe.exceptions.DuplicateEntryError):
	# 		frappe.get_doc({
	# 		"doctype": "Employee",
	# 		"employee_name": "hossam",
	# 		"company": self.company.name,
	# 		"department" : self.dept.name,
	# 		"email_address": "ayser@a.com", 
	# 		"mobile_number": "+201111111112",
	# 	}).insert()
			

	# def test_required_fields(self):
	# 	with self.assertRaises(frappe.exceptions.ValidationError):
	# 		frappe.get_doc({
	# 			"doctype": "Employee",
	# 			"employee_name": "karim",
	# 		}).insert()

	# 	# an employee without a company
	# 	with self.assertRaises(frappe.exceptions.ValidationError):
	# 		frappe.get_doc({
	# 			"doctype": "Employee",
	# 			"employee_name": "karim",
	# 			"department" : self.dept.name,
	# 			"email_address": "ayser@a.com", 
	# 			"mobile_number": "+201111111112",
	# 		}).insert()

	# 	# an employee without a department
	# 	with self.assertRaises(frappe.exceptions.ValidationError):
	# 		frappe.get_doc({
	# 			"doctype": "Employee",
	# 			"employee_name": "karim",
	# 			"company": self.company.name,
	# 			"email_address": "ayser@a.com", 
	# 			"mobile_number": "+201111111112",
	# 		}).insert()

	# 	# an employee without an email address
	# 	with self.assertRaises(frappe.exceptions.ValidationError):
	# 		frappe.get_doc({
	# 			"doctype": "Employee",
	# 			"employee_name": "karim",
	# 			"company": self.company.name,
	# 			"department" : self.dept.name,
	# 			"mobile_number": "+201111111112",
	# 		}).insert()

	# 	# an employee without a mobile number
	# 	with self.assertRaises(frappe.exceptions.ValidationError):
	# 		frappe.get_doc({
	# 			"doctype": "Employee",
	# 			"employee_name": "karim",
	# 			"company": self.company.name,
	# 			"department" : self.dept.name,
	# 			"email_address": "ayser@a.com", 
	# 		}).insert()


	def test_calculate_days_employed(self):
		unhired_emp = self.employee
		
		today = datetime.now().date()
		hired_date = datetime.strptime('2025-10-4', '%Y-%m-%d').date()
		employeed_days = (today - hired_date).days


		hired_emp = frappe.get_doc({
			"doctype": "Employee",
			"employee_name": "hossam",
			"company": self.company.name,
			"department" : self.dept.name,
			"email_address": "hossam@a.com", 
			"mobile_number": "+201111111112",
			"hired_on": hired_date,
			"designation__position": "HR"
		}).insert()

		self.assertEqual(unhired_emp.days_employed, None)
		self.assertEqual(hired_emp.days_employed, employeed_days)

