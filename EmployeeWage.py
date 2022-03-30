'''
@Author: Sai Tarun
@Date: 2022-03-29 20: 47: 00
@Last Modified by: Sai Tarun
@Last Modified time: 2022-03-29 20: 50: 00
@Title: Check if Employee is Present or Absent
        Calculating Wages per Month.
'''

import random

#Declaring Variables
Rate_Per_Hour=20
Max_Working_Days=20
Total_Emp_Hours=0
Total_Working_Days=0

def working_hours_fun(check_attendance):
    switcher={0:0,1:8,2:4}
    return switcher[check_attendance]

while(Total_Working_Days<Max_Working_Days):
    Total_Working_Days+=1
    check_attendance=random.randint(0,2)
    working_hours=working_hours_fun(check_attendance)
    Total_Emp_Hours=Total_Emp_Hours+working_hours

employee_salary=(Rate_Per_Hour*Total_Emp_Hours)
print(f"Employee's Monthly Wage is:{employee_salary}")