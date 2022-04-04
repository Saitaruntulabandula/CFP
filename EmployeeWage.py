'''
@Author: Sai Tarun
@Date: 2022-04-03 11: 11: 00
@Last Modified by: Sai Tarun
@Last Modified time: 2022-04-03 11: 20: 00
@Title: Check if Employee is Present or Absent
        Using Function to Daily Wage and Total Wage
        Reaching Maximum Working Hours and Days
'''

import random
from re import L

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
def cal_hours():
    """
        Description:
            Function is used to Calculate Working Hours.
        Parameter:
            Not passed any parameter 
        Return:
            Returns nothing but prints daily wage and total wage.
    """
    #Declaring Variables
    rate_per_hour=20
    max_working_days=20
    max_working_hours_in_month=100
    total_emp_hours=0
    total_working_days=0
    total_wage=0
    list=[]
    while(total_working_days<max_working_days) and (total_emp_hours<max_working_hours_in_month):
        check_attendance=random.randint(0,1)
        attendance_status=attendance(check_attendance)
        if attendance_status==0:
            pass
        elif attendance_status==1:
            working_hours_count=random.randint(0,1)
            working_hours=working_hours_fun(working_hours_count)
            if working_hours==8:
                daily_wage=working_hours*rate_per_hour
                total_emp_hours=total_emp_hours+8
            else:
                daily_wage=working_hours*rate_per_hour
                total_emp_hours=total_emp_hours+4
            total_wage=total_wage+daily_wage
            total_working_days=total_working_days+1
            list.append(daily_wage)
    print("Daily Wage of Employee is ",list)
    print("Total emp wage:  ",total_wage)
    print("Total working days:  ",total_working_days)
    print("Total emp working hours: ",total_emp_hours)

cal_hours()