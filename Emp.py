import unittest

from employee_management_system import EmployeeManagementSystem


class TestEmployeeManagementSystem(unittest.TestCase):

    def test_create_employee(self):
        system = EmployeeManagementSystem()
        employee = system.create_employee("John Doe", 30, 1, "Engineering")
        self.assertIsNotNone(employee)
        self.assertEqual(employee.name, "John Doe")
        self.assertEqual(employee.age, 30)
        self.assertEqual(employee.emp_id, 1)
        self.assertEqual(employee.department, "Engineering")
        
    def test_delete_employee(self):
        system = EmployeeManagementSystem()
        employee = system.delete_employee(1)
        self.assertIsNotNone(employee)
        
    def test_retrieve_employee(self):
        system = EmployeeManagementSystem()
        employee = system.retrieve_employee(1)
        self.assertIsNone(employee)
        # Mohamed, Mohamed 60084223
        
        

