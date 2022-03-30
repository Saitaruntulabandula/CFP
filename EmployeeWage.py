'''
@Author: Sai Tarun
@Date: 2022-03-29 20: 47: 00
@Last Modified by: Sai Tarun
@Last Modified time: 2022-03-29 20: 50: 00
@Title: Check if Employee is Present or Absent
        Add Part Time Employee and Wage.
'''

import random

Full_Time_Worker=1
Part_Time_Worker=2
Rate_Per_Hour=20
check_attendance=random.randint(0,2)

if check_attendance==Full_Time_Worker:   
    print("Employee is Full time worker")
    working_hours=8
elif check_attendance==Part_Time_Worker:
    print("Employee is Part time worker")
    working_hours=4
else:
    working_hours=0
    print("Employee is Absent")
employee_salary=(Rate_Per_Hour*working_hours)
print(f"Salary:{employee_salary}")