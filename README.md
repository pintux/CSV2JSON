CSV2JSON
========

A little tool to transform a CSV file into a JSON file with Python


**Usage**

1. edit csv2json.py file to specify column names of your CSV file. Example:

        #EDIT THIS LIST WITH YOUR REQUIRED JSON KEY NAMES
        fieldnames=["firstname","secondname","age"]


2. run

        python csv2json.py myCSVfile.txt

where myCSVfile.txt it's your CSV file.


It will create a JSON array in a file named myCSVfile.json
