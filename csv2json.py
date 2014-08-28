import csv
import sys
import json

#EDIT THIS LIST WITH YOUR REQUIRED JSON KEY NAMES
fieldnames=["firstname","secondname","age"]

def convert(filename):
  csv_filename = filename[0]
  print "Opening CSV file: ",csv_filename
  f=open(csv_filename, 'r')
  csv_reader = csv.DictReader(f,fieldnames)
  json_filename = csv_filename.split(".")[0]+".json"
  print "Saving JSON to file: ",json_filename
  jsonf = open(json_filename,'w')
  data = json.dumps([r for r in csv_reader])
  jsonf.write(data)
  f.close()
  jsonf.close()

if __name__=="__main__":
  convert(sys.argv[1:])
