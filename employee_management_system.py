import unittest
class Employee:
    def __init__(self, name, age, emp_id, department):
        self.name = name
        self.age = age
        self.emp_id = emp_id
        self.department = department

class EmployeeManagementSystem:
    def __init__(self):
        self.employees = []

    def create_employee(self, name, age, emp_id, department):
        new_employee = Employee(name, age, emp_id, department)
        self.employees.append(new_employee)
        return new_employee

    def retrieve_employee(self, emp_id):
        for employee in self.employees:
            if employee.emp_id == emp_id:
                return employee
            return None

    def delete_employee(self, emp_id):
        for employee in self.employees:
            if employee.emp_id == emp_id:
                self.employees.remove(employee)
                return True
        return False


if __name__ == '__main__':
    unittest.main()