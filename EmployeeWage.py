'''
@Author: Sai Tarun
@Date: 2022-03-31 16: 30: 00
@Last Modified by: Sai Tarun
@Last Modified time: 2022-03-31 16: 50: 00
@Title: Check if Employee is Present or Absent
        Using Case Statement
'''

import random

def working_hours_fun(working_hours_count):
    """
        Description:
            Function is used to check Working Hours.
        Parameter:
            Random integer is used as a parameter. 
        Return:
            Returns the value of working hours
    """
    switcher={0:8,1:4}
    return switcher[working_hours_count]

def attendance(check_attendance):
    """
        Description:
            Function is used to check attendance.
        Parameter:
            Random integer is used as a parameter. 
        Return:
            Returns the value of the random integer key.
    """
    switcher={0:0,1:1}
    return switcher[check_attendance]

Rate_Per_Hour=20
check_attendance=random.randint(0,1)
attendance_status=attendance(check_attendance)
if attendance_status==0:
    print("Employee is absent")
elif attendance_status==1:
    print("Employee is present")
    working_hours_count=random.randint(0,1)
    working_hours=working_hours_fun(working_hours_count)
    if working_hours==8:
        print("Employee is present full time")
        employee_salary=(Rate_Per_Hour*working_hours)
        print(f"Salary of the full time employee is:{employee_salary}")
    else:
        print("Employee is present part time")
        employee_salary=(Rate_Per_Hour*working_hours)
        print(f"Salary of the part time employee is:{employee_salary}")