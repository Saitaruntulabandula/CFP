'''
@Author: Sai Tarun
@Date: 2022-03-29 20: 47: 00
@Last Modified by: Sai Tarun
@Last Modified time: 2022-03-29 20: 50: 00
@Title: Check weather the Employee is Present or Absent
'''

import random

Present=1
Rate_Per_Hour=20
check_attendance=random.randint(0,1)

if check_attendance==1:   
    print("Employee is Present")
    working_hours=8
else:
    print("Employee is Absent")
    working_hours=0
employee_salary=(Rate_Per_Hour*working_hours)
print(f"Salary:{employee_salary}")