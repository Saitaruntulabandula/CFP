'''
@Author: Sai Tarun
@Date: 2022-03-04 07: 39: 00
@Last Modified by: Sai Tarun
@Last Modified time: 2022-03-04 07: 45: 00
@Title: Check if Employee is Present or Absent
        Employee monthly wage for 20 working days
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

rate_per_hour=20
part_time_count=0
full_time_count=0
total_monthly_wage=0
total_working_days=0
while total_working_days<20:
    check_attendance=random.randint(0,1)
    attendance_status=attendance(check_attendance)
    if attendance_status==0:
        print("Employee is absent")
    elif attendance_status==1:
        working_hours_count=random.randint(0,1)
        working_hours=working_hours_fun(working_hours_count)
        if working_hours==8:
            print("Employee is present full time")
            full_time_count=full_time_count+1
            employee_salary=(rate_per_hour*working_hours)
        else:
            print("Employee is present part time")
            part_time_count=part_time_count+1
            employee_salary=(rate_per_hour*working_hours)
        total_monthly_wage=total_monthly_wage+employee_salary
        total_working_days=total_working_days+1
print("Total working days is: ",total_working_days)
print("Part time working days: ",part_time_count)
print("Full time working days: ",full_time_count)
print("Total monthly wage: ",total_monthly_wage)