import pandas as pd
import numpy as np
import env
import os

######## telco_churn ########

# Standard function to acquire credentials to access SQL database
def get_db_url(dbname, username=env.user, hostname=env.host, passw=env.password):
    url = f'mysql+pymysql://{username}:{passw}@{hostname}/telco_churn'
    return url

url = get_db_url('telco_churn', env.user, env.host, env.password)

# SQL query to acquire telco dataset
def new_telco_data():
    return pd.read_sql('SELECT * FROM customers as c JOIN contract_types as ct ON c.contract_type_id = ct.contract_type_id JOIN payment_types as pt ON c.payment_type_id = pt.payment_type_id JOIN internet_service_types as ist ON c.internet_service_type_id = ist.internet_service_type_id', url)

# Function to read telco data, either locally or via SQL query
def get_telco_data():
    filename = "telco.csv"
    
    # if file is available locally, read it
    if os.path.isfile(filename):
        return pd.read_csv(filename)
    
    # if file not available locally, acquire data from SQL database
    # and write it as csv locally for future use
    else:
        # Reading the SQL query into a dataframe
        df = new_telco_data()
        
        # Writing the df to our disk for later
        df.to_csv(filename)

        # Returning the dataframe
        return df  



