
# imports
import pandas as pd
import os

# In[2]:

# settings
request_directory = "C:/Users/Lin/Desktop/CodeForGood/requests/29-09-2017"
inventory_file_directory = "C:/Users/Lin/Desktop/CodeForGood/inventory/29-09-2017/inventory.xlsx"

# In[3]:

# create template for output
ben_list = pd.read_excel(inventory_file_directory, sheetname="B")
compiled_df = pd.read_excel(inventory_file_directory, sheetname="Inventory")

# In[4]:

compiled_df

# In[5]:

for filename in os.listdir(request_directory):
    if filename.endswith(".xlsx"):
        print "Processing -->", os.path.join(request_directory, filename)
        request_workbook = pd.read_excel(os.path.join(request_directory, filename))
        client_name = request_workbook.iloc[2, 2]
        compiled_df[client_name] = ""
        request_df = request_workbook.iloc[16:, 6]

        for i, row in enumerate(request_df):
            compiled_df.set_value(i, client_name, row)

        continue
    else:
        print "Not Excel -->", os.path.join(request_directory, filename)
print "completed"

# Get a ranking system
ben_list = ben_list.set_index(ben_list.Entity, drop=True)
ben_list = ben_list.drop('Entity', axis=1)
bf = pd.DataFrame(compiled_df.iloc[0, 6:], columns=['test'])
ben_list['Priority'] = ben_list['Success'] * ben_list['SCORE']
final_df = pd.concat([ben_list, bf], join='inner', axis=1)
final_df['Percentage'] = final_df['Priority'] * final_df['test'] / (final_df['Priority'] * final_df['test']).sum()
result = final_df.sort(['Percentage'], ascending=[0])
# Could not get algorithm to work, iterated multiple times but could not find satisfactory algorithm
# Using placeholder values to assign based on weightage


for k in range(compiled_df.shape[0]):
    assignment = pd.DataFrame(index=compiled_df.columns[6:], columns=['Quantity', 'Quantity_needed'])
    assignment["Quantity_needed"] = compiled_df.iloc[0, 6:]
    assignment["Quantity"] = 0
    total = compiled_df.iloc[0, 4]
    i = 0
    while (i < total):
        for row in assignment.index:
            if (assignment.loc[row, 'Quantity'] < assignment.loc[row, 'Quantity_needed']):
                assignment.loc[row, 'Quantity'] = assignment.loc[row, 'Quantity'] + 1
                i = i + 1
    name = compiled_df.iloc[k, 1].replace('/', '_')
    assignment.to_excel("assignment_" + name + ".xlsx")



