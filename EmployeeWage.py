'''
@Author: Sai Tarun
@Date: 2022-03-30 20: 47: 00
@Last Modified by: Sai Tarun
@Last Modified time: 2022-03-30 20: 50: 00
@Title: Total working hours.
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
            Function is used to calculate Working Hours.
        Parameter:
            No parameter is required 
        Return:
            Returns nothing,but prints total working hours
    """
    Max_Working_Days=20
    Max_Working_Hours_In_Month=100
    Total_Emp_Hours=0
    Total_Working_Days=0
    while(Total_Working_Days<Max_Working_Days) and (Total_Emp_Hours<Max_Working_Hours_In_Month):
        Total_Working_Days+=1
        check_attendance=random.randint(0,2)
        working_hours=working_hours_fun(check_attendance)
        Total_Emp_Hours=Total_Emp_Hours+working_hours
    print("Total Working Hours are",Total_Emp_Hours)
cal_hours()
