import csv

file_name="static/csvFiles/answers.csv"

def writeToCsv (data):

  with open(file_name,'a', encoding='UTF8', newline='') as writeFile:
      csvwriter=csv.writer(writeFile)
      csvwriter.writerow([data])

def deleteCsv ():

  with open(file_name,'w', encoding='UTF8', newline='') as writeFile:
      csvwriter=csv.writer(writeFile)
      csvwriter.writerow(["data"])