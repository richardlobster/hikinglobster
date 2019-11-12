#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import csv


# In[ ]:


input_file = list(csv.DictReader(open('Border_Crossing_Entry_Data.csv')))


# In[ ]:


output_list=[]
output_dict = {}

date_list = []
measure_list = []
border_list = []

for row in input_file:
    if row['Border'] not in border_list:
        border_list.append(row['Border'])
    if row['Date'] not in date_list:
        date_list.append(row['Date'])
    if row['Measure'] not in measure_list:
        measure_list.append(row['Measure'])
    
    new_key = (row['Border'],row['Date'],row['Measure']) # create new keys with combinations
    
    if new_key not in output_list:
        output_list.append(new_key)                      # output_list has the same order of rows as input_file
        output_dict[new_key] = int(row['Value'])         # assign the value to the new key if the new key has not been added into the dictionary
    else:
        output_dict[new_key] += int(row['Value'])        # add up the value for the existing new key for project purpose


# In[ ]:


# print(output_dict)


# In[ ]:


date_list.sort(reverse=True)      # convert to desending order
border_list.sort(reverse=True)
measure_list.sort(reverse=True)


# In[ ]:


value_list = list(output_dict.values())


# In[ ]:


value_list.sort(reverse=True)


# In[ ]:


output_2 = {}       # write the output into csv with desending order : date--value--measure--border
with open('output_0.csv', mode='w', newline='') as out_file:
    out_writer = csv.writer(out_file, delimiter=',')
    out_writer.writerow(["Border", "Date", "Measure", "Value","Average"])
    for date_i in date_list:
        for value_i in value_list:
            for measure_i in measure_list:
                for border_i in border_list:
                    if output_dict.get((border_i,date_i,measure_i)):
                        if output_dict[(border_i,date_i,measure_i)]==value_i:
                            output_2[(border_i,date_i,measure_i)] = value_i
                            out_writer.writerow([border_i, date_i, measure_i, value_i])                


# In[ ]:


# print(output_2)


# In[ ]:


input_file2 = list(csv.DictReader(open('output_0.csv')))


# In[ ]:


total_rows = len(input_file2)      # Calculte the average value
with open('report.csv', mode='w', newline='') as out_file:
    out_writer = csv.writer(out_file, delimiter=',')
    out_writer.writerow(["Border", "Date", "Measure", "Value","Average"])
    
    for p1 in range (total_rows):
        cur_border = input_file2[p1]['Border']
        cur_measure = input_file2[p1]['Measure']
        cur_date = input_file2[p1]['Date']
        cur_value = input_file2[p1]['Value']
        cur_average = 0
        count = 0

        for p2 in range(p1+1, total_rows):
            if input_file2[p2]['Border']==cur_border and input_file2[p2]['Measure']==cur_measure:
                cur_average += int(input_file2[p2]['Value'])
                count +=1
        if count != 0:
            cur_average = int(cur_average/count)
        out_writer.writerow([cur_border, cur_date, cur_measure, cur_value, cur_average])


# In[ ]:


print('~~~~~Done~~~~~')

