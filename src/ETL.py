import json
import os
import pandas as pd
import pymysql

def create_database(cursor, db_name):
    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name}")
    connection.commit()
    cursor.execute(f"USE {db_name}")
    print(f"Database '{db_name}' created and selected.")
    connection.commit()

def create_table(cursor, table_name, query):
    cursor.execute(f"create table if not exists {table_name} {query}")
    connection.commit()
    print(f"Table `{table_name}` created successfully!")
    

def insert_records(cursor, connection, table_name, values):   
    placeholder= ', '.join(['%s'] * len(values[0])) 
    query = f"INSERT INTO {table_name} VALUES ({placeholder})"
    cursor.executemany(query, values)
    connection.commit()
    
# Connect to MySQL database
try:
    connection = pymysql.connect(
    host="localhost",       
    port=3306,
    user="root",
    password="12345",
    database='phonepe' 
    )
    print("Connected successfully!")
    cursor=connection.cursor()
except pymysql.MySQLError as e:
    print(f"Error connecting to MySQL: {e}")    

create_database(cursor, "phonepe")

# Create 10 tables for PhonePe data
""" 
        1. agg_transaction
        2. agg_insurance
        3. agg_user
        4. map_transaction
        5. map_insurance
        6. map_user 
        7. top_transaction
        8. top_insurance
        9. top_user
        10. top_district
# """

# 1.AGGREGATED_TRANSACTION

path="C:/Users/saghe/OneDrive/Desktop/phonepe-transaction-insights/pulse/data/aggregated/transaction/country/india/state/"
Agg_state_list=os.listdir(path)
Agg_state_list
clm={'States':[], 'Years':[],'Quarter':[],'Transaction_type':[], 'Transaction_count':[], 'Transaction_amount':[]}

for i in Agg_state_list:
    p_i=path+i+"/"
    Agg_yr=os.listdir(p_i)
    for j in Agg_yr:
        p_j=p_i+j+"/"
        Agg_yr_list=os.listdir(p_j)
        for k in Agg_yr_list:
            p_k=p_j+k
            Data=open(p_k,'r')
            D=json.load(Data)
            for z in D['data']['transactionData']:
              Name=z['name']
              count=z['paymentInstruments'][0]['count']
              amount=z['paymentInstruments'][0]['amount']
              clm['Transaction_type'].append(Name)
              clm['Transaction_count'].append(count)
              clm['Transaction_amount'].append(amount)
              clm['States'].append(i)
              clm['Years'].append(j)
              clm['Quarter'].append(int(k.strip('.json')))
              
#Succesfully created a dataframe
Agg_Trans=pd.DataFrame(clm)

#replacing the state names
Agg_Trans["States"] = Agg_Trans["States"].str.replace("andaman-&-nicobar-islands","Andaman & Nicobar")
Agg_Trans["States"] = Agg_Trans["States"].str.replace("-"," ")
Agg_Trans["States"] = Agg_Trans["States"].str.title()
Agg_Trans['States'] = Agg_Trans['States'].str.replace("Dadra & Nagar Haveli & Daman & Diu", "Dadra and Nagar Haveli and Daman and Diu")
# Create the agg_transaction table
create_table_query_for_agg_transaction = """
(
    States VARCHAR(100),
    Years INT,
    Quarter INT,
    Transaction_type VARCHAR(100),
    Transaction_count BIGINT,
    Transaction_amount DOUBLE
)
"""
create_table(cursor, 'agg_transaction', create_table_query_for_agg_transaction)

# Convert DataFrame to list of tuples
values = list(Agg_Trans.itertuples(index=False, name=None))

# Insert all rows at once
insert_records(cursor, connection, 'agg_transaction', values)
print("Data inserted into MySQL table successfully.")

# ******************************************************************************************************************************************************************

# 2. AGGREGATED_INSURANCE

path="C:/Users/saghe/OneDrive/Desktop/phonepe-transaction-insights/pulse/data/aggregated/insurance/country/india/state/"
Agg_state_list=os.listdir(path)
Agg_state_list
clm={'States':[], 'Years':[],'Quarter':[],'Transaction_type':[], 'Transaction_count':[], 'Transaction_amount':[]}

for i in Agg_state_list:
    p_i=path+i+"/"
    Agg_yr=os.listdir(p_i)
    for j in Agg_yr:
        p_j=p_i+j+"/"
        Agg_yr_list=os.listdir(p_j)
        for k in Agg_yr_list:
            p_k=p_j+k
            Data=open(p_k,'r')
            D=json.load(Data)
            for z in D['data']['transactionData']:
              Name=z['name']
              count=z['paymentInstruments'][0]['count']
              amount=z['paymentInstruments'][0]['amount']
              clm['Transaction_type'].append(Name)
              clm['Transaction_count'].append(count)
              clm['Transaction_amount'].append(amount)
              clm['States'].append(i)
              clm['Years'].append(j)
              clm['Quarter'].append(int(k.strip('.json')))

#Succesfully created a dataframe
Agg_Insurance=pd.DataFrame(clm)

#replacing the state names
Agg_Insurance["States"] = Agg_Insurance["States"].str.replace("andaman-&-nicobar-islands","Andaman & Nicobar")
Agg_Insurance["States"] = Agg_Insurance["States"].str.replace("-"," ")
Agg_Insurance["States"] = Agg_Insurance["States"].str.title()
Agg_Insurance['States'] = Agg_Insurance['States'].str.replace("Dadra & Nagar Haveli & Daman & Diu", "Dadra and Nagar Haveli and Daman and Diu")

# Create the agg_insurance table
create_table_query_for_agg_insurance  = """
(
    States VARCHAR(100),
    Years INT,
    Quarter INT,
    Transaction_type VARCHAR(100),
    Transaction_count BIGINT,
    Transaction_amount DOUBLE
)
"""
create_table(cursor, 'agg_insurance', create_table_query_for_agg_insurance)

# Convert DataFrame to list of tuples
values = list(Agg_Insurance.itertuples(index=False, name=None))

# Insert all rows at once
insert_records(cursor, connection, 'agg_insurance', values)
print("Data inserted into MySQL table successfully.")

# ******************************************************************************************************************************************************************

# 3. AGGREGATED_USER

path="C:/Users/saghe/OneDrive/Desktop/phonepe-transaction-insights/pulse/data/aggregated/user/country/india/state/"
Agg_state_list=os.listdir(path)
Agg_state_list
clm = {'States': [],'Years': [],'Quarter': [],'Brand': [],'Transaction_count': [],'Transaction_percentage': []}

for i in Agg_state_list:
    p_i=path+i+"/"
    Agg_yr=os.listdir(p_i)
    for j in Agg_yr:
        p_j=p_i+j+"/"
        Agg_yr_list=os.listdir(p_j)
        for k in Agg_yr_list:
            p_k=p_j+k
            Data=open(p_k,'r')
            D=json.load(Data)
            users_by_device = D.get('data', {}).get('usersByDevice')
            if users_by_device:
                for z in users_by_device:
                    Brand = z.get('brand')
                    Count = z.get('count')
                    Percentage = z.get('percentage')
                    clm['Brand'].append(Brand)
                    clm['Transaction_count'].append(Count)
                    clm['Transaction_percentage'].append(Percentage)
                    clm['States'].append(i)  # i = state name
                    clm['Years'].append(j)   # j = year
                    clm['Quarter'].append(int(k.strip('.json')))  # k = quarter filename
# Convert to DataFrame
Agg_user = pd.DataFrame(clm)

# replacing the state names
Agg_user["States"] = Agg_user["States"].str.replace("andaman-&-nicobar-islands","Andaman & Nicobar")
Agg_user["States"] = Agg_user["States"].str.replace("-"," ")
Agg_user["States"] = Agg_user["States"].str.title()
Agg_user['States'] = Agg_user['States'].str.replace("Dadra & Nagar Haveli & Daman & Diu", "Dadra and Nagar Haveli and Daman and Diu")
# Create the agg_user table
create_table_query_for_agg_user = """
(
    States VARCHAR(100),
    Years INT,
    Quarter INT,
    Brand VARCHAR(100),
    Transaction_count BIGINT,
    Transaction_percentage DOUBLE
)"""
create_table(cursor, 'agg_user', create_table_query_for_agg_user)

# Convert DataFrame to list of tuples
values = list(Agg_user.itertuples(index=False, name=None))

# Insert all rows at once
insert_records(cursor, connection, 'agg_user', values)
print("Data inserted into MySQL table successfully.")

# ******************************************************************************************************************************************************************

# 4. MAP INSURANCE

path="C:/Users/saghe/OneDrive/Desktop/phonepe-transaction-insights/pulse/data/map/insurance/hover/country/india/state/"
Agg_state_list=os.listdir(path)
clm = {"States":[], "Years":[], "Quarter":[], "District":[], "Transaction_count":[],"Transaction_amount":[] }

for i in Agg_state_list:
    p_i=path+i+"/"
    Agg_yr=os.listdir(p_i)
    for j in Agg_yr:
        p_j=p_i+j+"/"
        Agg_yr_list=os.listdir(p_j)
        for k in Agg_yr_list:
            p_k=p_j+k
            Data=open(p_k,'r')
            D=json.load(Data)
            for z in D['data']['hoverDataList']:
                district = z['name']
                count = z['metric'][0]['count']
                amount = z['metric'][0]['amount']
                clm['States'].append(i)
                clm['Years'].append(j)
                clm['Quarter'].append(int(k.strip('.json')))
                clm['District'].append(district)
                clm['Transaction_count'].append(count)
                clm['Transaction_amount'].append(amount)
                
# Convert to DataFrame
map_insurance = pd.DataFrame(clm)

# replacing the state names
map_insurance["States"] = map_insurance["States"].str.replace("andaman-&-nicobar-islands","Andaman & Nicobar")
map_insurance["States"] = map_insurance["States"].str.replace("-"," ")
map_insurance["States"] = map_insurance["States"].str.title()
map_insurance['States'] = map_insurance['States'].str.replace("Dadra & Nagar Haveli & Daman & Diu", "Dadra and Nagar Haveli and Daman and Diu")

# Create the map_insurance table
create_table_query_for_map_insurance = """
(
    States VARCHAR(100),
    Years INT,
    Quarter INT,
    District VARCHAR(100),
    Transaction_count BIGINT,
    Transaction_amount DOUBLE
)
"""
create_table(cursor, 'map_insurance', create_table_query_for_map_insurance)
values = list(map_insurance.itertuples(index=False, name=None))

# Insert all rows at once
insert_records(cursor, connection, 'map_insurance', values)
print("Data inserted into MySQL table successfully.")

#******************************************************************************************************************************************************************

# 5. MAP TRANSACTION

path="C:/Users/saghe/OneDrive/Desktop/phonepe-transaction-insights/pulse/data/map/transaction/hover/country/india/state/"
Agg_state_list=os.listdir(path)
clm = {"States":[], "Years":[], "Quarter":[], "District":[], "Transaction_count":[],"Transaction_amount":[] }

for i in Agg_state_list:
    p_i=path+i+"/"
    Agg_yr=os.listdir(p_i)
    for j in Agg_yr:
        p_j=p_i+j+"/"
        Agg_yr_list=os.listdir(p_j)
        for k in Agg_yr_list:
            p_k=p_j+k
            Data=open(p_k,'r')
            D=json.load(Data)
            for z in D['data']['hoverDataList']:
                district = z['name']
                count = z['metric'][0]['count']
                amount = z['metric'][0]['amount']
                clm['States'].append(i)
                clm['Years'].append(j)
                clm['Quarter'].append(int(k.strip('.json')))
                clm['District'].append(district)
                clm['Transaction_count'].append(count)
                clm['Transaction_amount'].append(amount)
                
# Convert to DataFrame
map_transaction = pd.DataFrame(clm)

# replacing the state names
map_transaction["States"] = map_transaction["States"].str.replace("andaman-&-nicobar-islands","Andaman & Nicobar")
map_transaction["States"] = map_transaction["States"].str.replace("-"," ")
map_transaction["States"] = map_transaction["States"].str.title()
map_transaction['States'] = map_transaction['States'].str.replace("Dadra & Nagar Haveli & Daman & Diu", "Dadra and Nagar Haveli and Daman and Diu")

# Create the map_transaction table
create_table_query_for_map_transaction = """
(
    States VARCHAR(100),
    Years INT,
    Quarter INT,
    District VARCHAR(100),
    Transaction_count BIGINT,
    Transaction_amount DOUBLE
)
"""
create_table(cursor, 'map_transaction', create_table_query_for_map_transaction)
values = list(map_transaction.itertuples(index=False, name=None))

# Insert all rows at once
insert_records(cursor, connection, 'map_transaction', values)
print("Data inserted into MySQL table successfully.")

# ***************************************************************************************************************************************************

# 6. MAP USER

path = "C:/Users/saghe/OneDrive/Desktop/phonepe-transaction-insights/pulse/data/map/user/hover/country/india/state/"
Agg_state_list = os.listdir(path)

clm = {
    "States": [],
    "Years": [],
    "Quarter": [],
    "District": [],
    "RegisteredUser": [],
    "AppOpens": []
}

for i in Agg_state_list:
    p_i = path + i + "/"
    Agg_yr = os.listdir(p_i)
    for j in Agg_yr:
        p_j = p_i + j + "/"
        Agg_yr_list = os.listdir(p_j)
        for k in Agg_yr_list:
            p_k = p_j + k
            with open(p_k, 'r') as Data:
                D = json.load(Data)
                for district, district_data in D['data']['hoverData'].items():
                    registereduser = district_data["registeredUsers"]
                    appopens = district_data["appOpens"]
                    clm["District"].append(district)
                    clm["RegisteredUser"].append(registereduser)
                    clm["AppOpens"].append(appopens)
                    clm["States"].append(i)
                    clm["Years"].append(j)
                    clm["Quarter"].append(int(k.strip(".json")))

# Convert to DataFrame                    
map_user = pd.DataFrame(clm)

# replacing the state names
map_user["States"] = map_user["States"].str.replace("andaman-&-nicobar-islands","Andaman & Nicobar")
map_user["States"] = map_user["States"].str.replace("-"," ")
map_user["States"] = map_user["States"].str.title()
map_user['States'] = map_user['States'].str.replace("Dadra & Nagar Haveli & Daman & Diu", "Dadra and Nagar Haveli and Daman and Diu")

# Create the map_user table
create_table_query_for_map_user = """
(
    States VARCHAR(100),
    Years INT,
    Quarter INT,
    District VARCHAR(100),
    registereduser BIGINT,
    appopens BIGINT
)
"""
create_table(cursor, 'map_user', create_table_query_for_map_user)

# Convert DataFrame to list of tuples
values = list(map_user.itertuples(index=False, name=None))

# Insert all rows at once
insert_records(cursor, connection, 'map_user', values)
print("Data inserted into MySQL table successfully.")   



#*************************************************************************************************************************************************************

# 7. TOP INSURANCE

path = "C:/Users/saghe/OneDrive/Desktop/phonepe-transaction-insights/pulse/data/top/insurance/country/india/state/"
Agg_state_list = os.listdir(path)

clm = {"States":[], "Years":[], "Quarter":[], "Pincodes":[], "Transaction_count":[], "Transaction_amount":[]}

for i in Agg_state_list:
    p_i = path + i + "/"
    Agg_yr = os.listdir(p_i)
    for j in Agg_yr:
        p_j = p_i + j + "/"
        Agg_yr_list = os.listdir(p_j)
        for k in Agg_yr_list:
            p_k = p_j + k
            with open(p_k, 'r') as Data:
                D = json.load(Data)
                for z in D["data"]["pincodes"]:
                    entityName = z["entityName"]
                    count = z["metric"]["count"]
                    amount = z["metric"]["amount"]
                    clm["Pincodes"].append(entityName)
                    clm["Transaction_count"].append(count)
                    clm["Transaction_amount"].append(amount)
                    clm["States"].append(i)
                    clm["Years"].append(j)
                    clm["Quarter"].append(int(k.strip(".json")))
                    
# create a DataFrame
Top_insurance = pd.DataFrame(clm)

#replacing the state names
Top_insurance["States"] = Top_insurance["States"].str.replace("andaman-&-nicobar-islands","Andaman & Nicobar")
Top_insurance["States"] = Top_insurance["States"].str.replace("-"," ")
Top_insurance["States"] = Top_insurance["States"].str.title()
Top_insurance['States'] = Top_insurance['States'].str.replace("Dadra & Nagar Haveli & Daman & Diu", "Dadra and Nagar Haveli and Daman and Diu")

# Create the top_insurance table
create_table_query_for_top_insurance = """  (
    States VARCHAR(100),
    Years INT,
    Quarter INT,
    Pincodes VARCHAR(100),
    Transaction_count BIGINT,
    Transaction_amount DOUBLE
)"""
create_table(cursor, 'top_insurance', create_table_query_for_top_insurance)

# Convert DataFrame to list of tuples
values = list(Top_insurance.itertuples(index=False, name=None))

# Insert all rows at once
insert_records(cursor, connection, 'top_insurance', values)
print("Data inserted into MySQL table successfully.")   


# **************************************************************************************************************************************************************

# 8. TOP USER

path = "C:/Users/saghe/OneDrive/Desktop/phonepe-transaction-insights/pulse/data/top/transaction/country/india/state/"
Agg_state_list = os.listdir(path)
clm = {"States":[], "Years":[], "Quarter":[], "Pincodes":[], "Transaction_count":[], "Transaction_amount":[]}

for i in Agg_state_list:
    p_i = path + i + "/"
    Agg_yr = os.listdir(p_i)
    for j in Agg_yr:
        p_j = p_i + j + "/"
        Agg_yr_list = os.listdir(p_j)
        for k in Agg_yr_list:
            p_k = p_j + k
            with open(p_k, 'r') as Data:
                D = json.load(Data)
                for z in D["data"]["pincodes"]:
                    entityName = z["entityName"]
                    count = z["metric"]["count"]
                    amount = z["metric"]["amount"]
                    clm["Pincodes"].append(entityName)
                    clm["Transaction_count"].append(count)
                    clm["Transaction_amount"].append(amount)
                    clm["States"].append(i)
                    clm["Years"].append(j)
                    clm["Quarter"].append(int(k.strip(".json")))
                    
# create a DataFrame
Top_transaction = pd.DataFrame(clm)

#replacing the state names
Top_transaction["States"] = Top_transaction["States"].str.replace("andaman-&-nicobar-islands","Andaman & Nicobar")
Top_transaction["States"] = Top_transaction["States"].str.replace("-"," ")
Top_transaction["States"] = Top_transaction["States"].str.title()
Top_transaction['States'] = Top_transaction['States'].str.replace("Dadra & Nagar Haveli & Daman & Diu", "Dadra and Nagar Haveli and Daman and Diu")

# Create the top_transaction table
create_table_query_for_top_transaction = """  (
    States VARCHAR(100),
    Years INT,
    Quarter INT,
    Pincodes VARCHAR(100),
    Transaction_count BIGINT,
    Transaction_amount DOUBLE
)"""
create_table(cursor, 'top_transaction', create_table_query_for_top_transaction)

# Convert DataFrame to list of tuples
values = list(Top_transaction.itertuples(index=False, name=None))

# Insert all rows at once
insert_records(cursor, connection, 'top_transaction', values)
print("Data inserted into MySQL table successfully.")   

#*************************************************************************************************************************************************

# 9. TOP USER

path= "C:/Users/saghe/OneDrive/Desktop/phonepe-transaction-insights/pulse/data/top/user/country/india/state/"
Agg_state_list = os.listdir(path)

clm = {"States":[], "Years":[], "Quarter":[], "Pincodes":[], "RegisteredUser":[]}

for i in Agg_state_list:
    p_i = path + i + "/"
    Agg_yr = os.listdir(p_i)
    for j in Agg_yr:
        p_j = p_i + j + "/"
        Agg_yr_list = os.listdir(p_j)
        for k in Agg_yr_list:
            p_k = p_j + k
            with open(p_k, 'r') as Data:
                D = json.load(Data)
                for z in D["data"]["pincodes"]:
                    name = z["name"]
                    registeredusers = z["registeredUsers"]
                    clm["Pincodes"].append(name)
                    clm["RegisteredUser"].append(registeredusers)
                    clm["States"].append(i)
                    clm["Years"].append(j)
                    clm["Quarter"].append(int(k.strip(".json")))
# create a DataFrame
Top_user = pd.DataFrame(clm)

# replacing the state names
Top_user["States"] = Top_user["States"].str.replace("andaman-&-nicobar-islands","Andaman & Nicobar")
Top_user["States"] = Top_user["States"].str.replace("-"," ")
Top_user["States"] = Top_user["States"].str.title()
Top_user['States'] = Top_user['States'].str.replace("Dadra & Nagar Haveli & Daman & Diu", "Dadra and Nagar Haveli and Daman and Diu")

# Create the top_user table
create_table_query_for_top_user = """  (
    States varchar(50),
    Years int,
    Quarter int,
    Pincodes int,
    RegisteredUser bigint
)"""
create_table(cursor, 'top_user', create_table_query_for_top_user)

# Convert DataFrame to list of tuples
values = list(Top_user.itertuples(index=False, name=None))

# Insert all rows at once
insert_records(cursor, connection, 'top_user', values)
print("Data inserted into MySQL table successfully.")

# #***************************************************************************************************************************************************************

# 10. TOP DISTRICT

path = "C:/Users/saghe/OneDrive/Desktop/phonepe-transaction-insights/pulse/data/top/transaction/country/india/state/"
Agg_state_list = os.listdir(path)

clm = {"States":[], "Years":[], "Quarter":[], "Districts":[], "Transaction_count":[], "Transaction_amount":[]}

for i in Agg_state_list:
    p_i = path + i + "/"
    Agg_yr = os.listdir(p_i)
    for j in Agg_yr:
        if not j.isdigit():  # Skip non-year folders
            continue
        year_int = int(j)
        p_j = p_i + j + "/"
        Agg_yr_list = os.listdir(p_j)
        for k in Agg_yr_list:
            p_k = p_j + k
            with open(p_k, 'r') as Data:
                D = json.load(Data)
                for z in D["data"]["districts"]:
                    entityName = z["entityName"]
                    count = z["metric"]["count"]
                    amount = z["metric"]["amount"]
                    clm["Districts"].append(entityName)
                    clm["Transaction_count"].append(count)
                    clm["Transaction_amount"].append(amount)
                    clm["States"].append(i)
                    clm["Years"].append(year_int)
                    quarter_num = int(k.replace(".json", "")) 
                    clm["Quarter"].append(quarter_num)
                    
# Create a DataFrame
Top_transaction_district = pd.DataFrame(clm)

# replacing the state names
Top_transaction_district["States"] = Top_transaction_district["States"].str.replace("andaman-&-nicobar-islands","Andaman & Nicobar")
Top_transaction_district["States"] = Top_transaction_district["States"].str.replace("-"," ")
Top_transaction_district["States"] = Top_transaction_district["States"].str.title()
Top_transaction_district['States'] = Top_transaction_district['States'].str.replace("Dadra & Nagar Haveli & Daman & Diu", "Dadra and Nagar Haveli and Daman and Diu")

# Create the top_district table
create_table_query_for_top_district = """  (
    States varchar(50),
    Years int,
    Quarter int,
    Districts varchar(100),
    Transaction_count bigint,
    Transaction_amount DECIMAL(18,2)
)"""
create_table(cursor, 'top_district', create_table_query_for_top_district)

# Convert DataFrame to list of tuples
values = list(Top_transaction_district.itertuples(index=False, name=None))

# Insert all rows at once
insert_records(cursor, connection, 'top_district', values)
print("Data inserted into MySQL table successfully.")