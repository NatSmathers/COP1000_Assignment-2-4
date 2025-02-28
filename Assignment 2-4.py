# input statements
salary = float(input("Enter Salary: $"))
numDependents = float(input("Enter Number of Dependents: "))

# calculate taxes here
stateTax = 0.065 * salary
federalTax = 0.28 * salary
dependentDeduction = salary * 0.025 * numDependents
totalWithholding = stateTax + federalTax + dependentDeduction
takehomePay = salary - totalWithholding
# output statements
print("State Tax: $" + str(stateTax))
print("Federal Tax: $" + str(federalTax))
print("Dependents: $" + str(dependentDeduction)) 
print("Salary: $" + str(salary))
print("Take Home Pay: $" + str(takehomePay))
