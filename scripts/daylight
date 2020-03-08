"""
Created on Sun Mar  8 19:51:26 2020

@author: James Densmore & Sergio Sanz
https://www.dataliftoff.com/author/dataliftoff_tuq2s3/

"""

import math
import datetime


def day_length(day_of_year, latitude):
    
    P = math.asin(0.39795 * math.cos(0.2163108 + 2 * math.atan(0.9671396 
        * math.tan(.00860 * (day_of_year - 186)))))

    pi = math.pi
    day_light_hours = 24 - (24 / pi) * math.acos((math.sin(0.8333 * pi / 180) 
        + math.sin(latitude * pi / 180) * math.sin(P)) 
        / (math.cos(latitude * pi / 180) * math.cos(P)))

    print(str(int(day_light_hours)) + ' hours, ' 
          + str(int((day_light_hours - int(day_light_hours)) * 60)) + ' min.')
    
time_now = datetime.datetime.now()
day_of_year = int(time_now.strftime('%j'))

latitude = float(input('Introduce your latitude: '))

day_length(day_of_year, latitude)
