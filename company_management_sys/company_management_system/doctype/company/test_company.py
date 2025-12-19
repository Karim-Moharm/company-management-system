from frappe.tests.utils import FrappeTestCase
import frappe
from frappe.exceptions import MandatoryError



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
            return self.company.delete()
        
    def test_create_company(self):
        """
        test case for creating a company
        """
        company = frappe.get_doc({
            "doctype": "Company",
            "company_name": "test company"
        }).insert()
        self.assertEqual(company.company_name, "test company")
        self.assertEqual(company.number_of_departments, 0)
        self.assertEqual(company.number_of_employees, 0)
        self.assertEqual(company.number_of_pojects, "test company")

        company.delete()


    def test_requied_company_name(self):
        """test case for a required field"""
        with self.assertRaises(MandatoryError):
            frappe.get_doc({
                "doctype": "Company"
            }).insert()


    