from frappe.tests.utils import FrappeTestCase
import frappe
from frappe import exceptions



class TestCompany(FrappeTestCase):
    """
    unit test cases for company docType
    """
    def setUp(self):
        self.company = frappe.get_doc({
            "doctype": "Company",
            "company_name": "microsoft" 
        }).insert()
    
    def tearDown(self):
        if self.company:
            self.company.delete()
        
    def test_create_company(self):
        """
        test case for creating a company
        """
        company = frappe.get_doc({
            "doctype": "Company",
            "company_name": "test company",
        }).insert()
        self.assertEqual(company.company_name, "test company")
        self.assertEqual(company.number_of_departments, 0)
        self.assertEqual(company.number_of_employees, 0)
        self.assertEqual(company.number_of_projects, 0)

        company.delete()


    def test_requied_company_name(self):
        """test case for a required field"""
        with self.assertRaises(exceptions.ValidationError):
            frappe.get_doc({
                "doctype": "Company"
            }).insert()


    def test_unique_company_name(self):
        """test case for unique fiels"""
        company1 = frappe.get_doc({
        "doctype": "Company",
        "company_name": "test company",
        }).insert()
        with self.assertRaises(exceptions.DuplicateEntryError):
            frappe.get_doc({
                "doctype": "Company",
                "company_name": "test company",
            }).insert()
        company1.delete()
    