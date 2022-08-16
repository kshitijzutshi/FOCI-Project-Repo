# This is a test file for the project.

import pandas as pd
import os
import datetime

# function to swap two numbers without using a temporary variable
def swap(a, b) -> int:
    """
    Swap two numbers without using a temporary variable.
    :param a: first number
    :param b: second number
    """
    a = a ^ b
    b = a ^ b
    a = a ^ b
    return a, b


"""
Load all csv files in this directory that start with "battery_status__".

Write and document a function that takes the dataframe as an argument and 
returns to total time the battery was fully charged.

"""


# function that takes the dataframe as an argument and  returns to total time the battery was fully charged

# Load all csv files in this directory that start with "battery_status__"


PATH = "./"
files = os.listdir(PATH) # Returns list of files in the folder which is specifed path
li = []
for file in files:
    if file.startswith("battery_status__"):# Checking wheter file starts with battery_status__
        # os.sep returns the separtor of operator system
        # exec(f"{file[:-4]} = pandas.read_csv({path}+{os.sep}+{file})")
        df = pd.read_csv(file, index_col=None, header=0)
        li.append(df)
df_concat = pd.concat(li,axis=0, ignore_index=True)


df2 = df_concat[df_concat['battery_level'] == 100]

def calculate_total_time_fully_charged():


    # get the t1 time
    t1 = df2['date_time'].iloc[0]
    t1 = t1.split('_')[1]
    t1 = t1.split('-')
    t1 = datetime.datetime(int(t1[2]), int(t1[0]), int(t1[1]))
    # t1 = datetime.datetime.strptime(t1, '%m-%d-%Y')

    # get the t2 time
    t2 = df2['date_time'].iloc[-1]
    t2 = t2.split('_')[1]
    t2 = t2.split('-')
    t2 = datetime.datetime(int(t2[2]), int(t2[0]), int(t2[1]))
    print(t1)

    # find the time delta
    time_delta = pd.Timedelta(t2 - t1).seconds / 60.0

    return time_delta

# Actual approach

for _, row in df.iterrows():
    event, value = row["event"], row["value"]
    if event == "qc_scan":
        if value == "Entered":
            qc_scan_starttime = df["timestamp"]
        elif value == "Exited":
            if qc_scan_starttime is not None:
                duration = df["timestamp"] - qc_scan_starttime
                total_duration += duration
                qc_scan_starttime = None 