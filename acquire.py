import pandas as pd
import numpy as np
import env
import os

######## titanic_db ########

def get_db_url(dbname, username=env.user, hostname=env.host, passw=env.password):
    url = f'mysql+pymysql://{username}:{passw}@{hostname}/titanic_db'
    return url

url = get_db_url('titanic_db', env.user, env.host, env.password)

def new_titanic_data():
    return pd.read_sql('SELECT * FROM passengers', url)




def get_titanic_data():
    filename = "titanic.csv"
    
    # if file is available locally, read it
    if os.path.isfile(filename):
        return pd.read_csv(filename)
    
    # if file not available locally, acquire data from SQL database
    # and write it as csv locally for future use
    else:
        # read the SQL query into a dataframe
        df = new_titanic_data()
        
        # Write that dataframe to disk for later. Called "caching" the data for later.
        df.to_csv(filename)

        # Return the dataframe to the calling code
        return df  

df = get_titanic_data()
df.head()

#-----------------------------------

######## iris_db ########

def get_db_url(dbname, username=env.user, hostname=env.host, passw=env.password):
    url = f'mysql+pymysql://{username}:{passw}@{hostname}/iris_db'
    return url

url = get_db_url('iris_db', env.user, env.host, env.password)

def new_iris_data():
    return pd.read_sql('SELECT * FROM measurements JOIN species ON measurements.species_id = species.species_id', url)


import os

def get_iris_data():
    filename = "iris.csv"
    
    # if file is available locally, read it
    if os.path.isfile(filename):
        return pd.read_csv(filename)
    
    # if file not available locally, acquire data from SQL database
    # and write it as csv locally for future use
    else:
        # read the SQL query into a dataframe
        df = new_iris_data()
        
        # Write that dataframe to disk for later. Called "caching" the data for later.
        df.to_csv(filename)

        # Return the dataframe to the calling code
        return df  

df_iris = get_iris_data()
df_iris.head()

#-----------------------------------

######## telco_churn ########

def get_db_url(dbname, username=env.user, hostname=env.host, passw=env.password):
    url = f'mysql+pymysql://{username}:{passw}@{hostname}/telco_churn'
    return url

url = get_db_url('telco_churn', env.user, env.host, env.password)

def new_telco_data():
    return pd.read_sql('SELECT * FROM customers as c JOIN contract_types as ct ON c.contract_type_id = ct.contract_type_id JOIN payment_types as pt ON c.payment_type_id = pt.payment_type_id JOIN internet_service_types as ist ON c.internet_service_type_id = ist.internet_service_type_id', url)


import os

def get_telco_data():
    filename = "telco.csv"
    
    # if file is available locally, read it
    if os.path.isfile(filename):
        return pd.read_csv(filename)
    
    # if file not available locally, acquire data from SQL database
    # and write it as csv locally for future use
    else:
        # read the SQL query into a dataframe
        df = new_telco_data()
        
        # Write that dataframe to disk for later. Called "caching" the data for later.
        df.to_csv(filename)

        # Return the dataframe to the calling code
        return df  

df_telco = get_telco_data()
df_telco.head()