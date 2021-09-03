class Employee:
    name = 'Dulal'
    age = 22


class DataAnalysis(Employee):

    def employeeInfo(self):
        print(f"The name of data analyst is {self.name} and age {self.age}")



data = DataAnalysis()
data.employeeInfo()