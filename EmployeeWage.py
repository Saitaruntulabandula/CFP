'''
@Author: Sai Tarun
@Date: 2022-03-30 20: 47: 00
@Last Modified by: Sai Tarun
@Last Modified time: 2022-03-30 20: 50: 00
@Title: Daily Wage and Total Wage.
'''

import random

def working_hours_fun(check_attendance):
    """
        Description:
            Function is used to check Working Hours.
        Parameter:
            Random integer is used as a parameter. 
        Return:
            Returns the value of working hours
    """
    switcher={0:0,1:8,2:4}
    return switcher[check_attendance]
def cal_hours():
    """
        Description:
            Function is used to calculate daily wage and total wage
        Parameter:
            No parameter is required 
        Return:
            Returns nothing,but prints daily wage and total wage
    """
    Rate_Per_Hour=20
    Max_Working_Days=20
    Max_Working_Hours_In_Month=100
    Total_Emp_Hours=0
    Total_Working_Days=0
    while(Total_Working_Days<Max_Working_Days) and (Total_Emp_Hours<Max_Working_Hours_In_Month):
        Total_Working_Days+=1
        check_attendance=random.randint(0,2)
        working_hours=working_hours_fun(check_attendance)
        Daily_Wage=working_hours*Rate_Per_Hour
        print("Daily Wage of Employee is ",Daily_Wage)
        Total_Emp_Hours=Total_Emp_Hours+working_hours
    print("Total Working Hours are",Total_Emp_Hours)
cal_hours()
