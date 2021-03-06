import numpy as np
import pandas as pd

dtype=object 

##pd.set_option('display.max_rows', 500)  
##pd.set_option('display.max_columns', 500)

result = pd.read_csv('readfile.csv',low_memory=False)

##reading column headers
text_file = pd.read_csv('column names.csv',sep='\t', header=None, low_memory=False) ##reading file with column names
text_file.columns=['filename']
column_name_arr = text_file.filename.get_values() ##converting column names into an array 

##assigning column headers
result.columns= column_name_arr

print ("The number of row is " + str (result.shape[0])) 
print ("\n  The number of column is "+ str (result.shape[1]))
print (" \n  Unique values of the last column:" + str (result['normal'].unique()))
print ("\n The number of times these unique values appear are: " + str (result.groupby('normal').size()))

     
