'''
@Author: Sai Tarun
@Date: 2022-04-03 11: 11: 00
@Last Modified by: Sai Tarun
@Last Modified time: 2022-04-03 11: 20: 00
@Title: Check if Employee is Present or Absent
        Reaching Maximum Working Hours and Days
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

#Declaring Variables
Rate_Per_Hour=20
Max_Working_Days=20
Max_Working_Hours_In_Month=100
Total_Emp_Hours=0
Total_Working_Days=0
while(Total_Working_Days<Max_Working_Days) or (Total_Emp_Hours<Max_Working_Hours_In_Month):
    check_attendance=random.randint(0,1)
    attendance_status=attendance(check_attendance)
    if attendance_status==0:
        Total_Emp_Hours=Total_Emp_Hours+0
    elif attendance_status==1:
        working_hours_count=random.randint(0,1)
        working_hours=working_hours_fun(working_hours_count)
        if working_hours==8:
            Total_Emp_Hours=Total_Emp_Hours+8
        else:
            Total_Emp_Hours=Total_Emp_Hours+4
        Total_Working_Days=Total_Working_Days+1


employee_salary=(Rate_Per_Hour*Total_Emp_Hours)
print("Total working days: ",Total_Working_Days)
print("Total emp working hours: ",Total_Emp_Hours)
print(f"Employee's Monthly Wage is :{employee_salary}")
