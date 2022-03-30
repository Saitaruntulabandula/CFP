'''
@Author: Sai Tarun
@Date: 2022-03-29 20: 47: 00
@Last Modified by: Sai Tarun
@Last Modified time: 2022-03-29 20: 50: 00
@Title: Check if Employee is Present or Absent
        Using Case Statement
'''

import random

def working_hours_fun(check_attendance):
    switcher={0:0,1:8,2:4}
    return switcher[check_attendance]



Full_Time_Worker=1
Part_Time_Worker=2
Rate_Per_Hour=20
check_attendance=random.randint(0,2)
working_hours=working_hours_fun(check_attendance)

employee_salary=(Rate_Per_Hour*working_hours)
print(f"Salary:{employee_salary}")