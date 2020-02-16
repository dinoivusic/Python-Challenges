class PayrollSystem:
    def calculate(self, employees):
        print('Calculating Payroll')
        print('===================')
        for employee in employees:
            print('Payroll for: {} - {}'.format(employee.id, employee.name))
            print('Check amount: {}'.format(employee.calculate()))
            print('')


class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id


class SalaryEmployee(Employee):
    def __init__(self, name, id, weekly_salary):
        super().__init__(id, name)
        self.weekly_salary = weekly_salary

    def calculate(self):
        return self.weekly_salary


class HourlyEmployee(Employee):
    def __init__(self, id, name, hours_worked, hour_rate):
        super().__init__(id, name)
        self.hours_worked = hours_worked
        self.hour_rate = hour_rate

    def calculate(self):
        return self.hours_worked * self.hour_rate


class CommissionEmployee(SalaryEmployee):
    def __init__(self, id, name, weekly_salary, commission):
        super().__init__(id, name, weekly_salary)
        self.commission = commission

    def calculate(self):
        fixed = super().calculate()
        return fixed + self.commission


salary_employee = SalaryEmployee('John Doe', 1, 500)
hourly_employee = HourlyEmployee(1, 'Alan', 40, 15)
commission_employee = CommissionEmployee(3, 'Sary', 450, 200)
payrollSys = PayrollSystem()

print(payrollSys.calculate([salary_employee, hourly_employee, commission_employee]))
