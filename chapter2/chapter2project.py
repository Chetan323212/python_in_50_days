# making student Result print project 
from tabulate import tabulate

studentname = "chetan patil"
studentclass = "10th"
studentRollnumber = 33
totalmarks = 456
parcentage = totalmarks/500*100

studentdata = [[studentname],[studentclass],
               [studentRollnumber],[totalmarks],
               [parcentage]
              ]

print(tabulate(studentdata))