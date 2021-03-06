import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

# Clean, Tidy, Prep Function
def prep_telco_data(df):
    # Drop duplicate columns
    df.drop(columns=['Unnamed: 0', \
                     'payment_type_id', \
                     'internet_service_type_id', \
                     'contract_type_id', \
                     'customer_id'], inplace=True)

    
    # Drop null values stored as whitespace    
    df['total_charges'] = df['total_charges'].str.strip()
    df = df[df.total_charges != '']
    
    # Convert to correct datatype
    df['total_charges'] = df.total_charges.astype(float)
    
    # Convert binary categorical variables to numeric
    df['gender_encoded'] = df.gender.map({'Female': 1, 'Male': 0})
    df['partner_encoded'] = df.partner.map({'Yes': 1, 'No': 0})
    df['dependents_encoded'] = df.dependents.map({'Yes': 1, 'No': 0})
    df['phone_service_encoded'] = df.phone_service.map({'Yes': 1, 'No': 0})
    df['paperless_billing_encoded'] = df.paperless_billing.map({'Yes': 1, 'No': 0})
    df['churn_encoded'] = df.churn.map({'Yes': 1, 'No': 0})
    
    # Get dummies for non-binary categorical variables
    dummy_df = pd.get_dummies(df[['multiple_lines', \
                              'online_security', \
                              'online_backup', \
                              'device_protection', \
                              'tech_support', \
                              'streaming_tv', \
                              'streaming_movies', \
                              'contract_type', \
                              'internet_service_type', \
                              'payment_type']], dummy_na=False, \
                              drop_first=False)
    
    # Concatenate dummy dataframe to original 
    df = pd.concat([df, dummy_df], axis=1)
    
    # Create addl. features
    df['p_w_d'] = np.where((df['partner_encoded'] == 1) & (df['dependents_encoded'] == 1), 1, 0)
    df['p_no_d'] = np.where((df['partner_encoded'] == 1) & (df['dependents_encoded'] == 0), 1, 0)
    df['d_no_p'] = np.where((df['partner_encoded'] == 0) & (df['dependents_encoded'] == 1), 1, 0)
    df['no_pod'] = np.where((df['partner_encoded'] == 0) & (df['dependents_encoded'] == 0), 1, 0)
    
    # Rename significant features for ease of use
    df = df.rename(columns={'payment_type_Electronic check': 'e_check', \
                   'contract_type_Month-to-month': 'm2m', \
                   'contract_type_One year': 'yr1', \
                   'contract_type_Two year': 'yr2', \
                   'internet_service_type_DSL': 'DSL', \
                   'internet_service_type_Fiber optic': 'fiber', \
                   'internet_service_type_None': 'no_int', \
                   'payment_type_Bank transfer (automatic)': 'a_bank_tr', \
                   'payment_type_Credit card (automatic)': 'a_ccard', \
                   'payment_type_Electronic check': 'e_check', \
                   'payment_type_Mailed check': 'm_check'
                  }) 
                  
    return df



######### csv_df ##########

def prep_telco_csv(df):
    # Drop duplicate columns
    df.drop(columns=['Unnamed: 0', \
                     'payment_type_id', \
                     'internet_service_type_id', \
                     'contract_type_id'], inplace=True)

    
    # Drop null values stored as whitespace    
    df['total_charges'] = df['total_charges'].str.strip()
    df = df[df.total_charges != '']
    
    # Convert to correct datatype
    df['total_charges'] = df.total_charges.astype(float)
    
    # Convert binary categorical variables to numeric
    df['gender_encoded'] = df.gender.map({'Female': 1, 'Male': 0})
    df['partner_encoded'] = df.partner.map({'Yes': 1, 'No': 0})
    df['dependents_encoded'] = df.dependents.map({'Yes': 1, 'No': 0})
    df['phone_service_encoded'] = df.phone_service.map({'Yes': 1, 'No': 0})
    df['paperless_billing_encoded'] = df.paperless_billing.map({'Yes': 1, 'No': 0})
    df['churn_encoded'] = df.churn.map({'Yes': 1, 'No': 0})
    
    # Get dummies for non-binary categorical variables
    dummy_df = pd.get_dummies(df[['multiple_lines', \
                              'online_security', \
                              'online_backup', \
                              'device_protection', \
                              'tech_support', \
                              'streaming_tv', \
                              'streaming_movies', \
                              'contract_type', \
                              'internet_service_type', \
                              'payment_type']], dummy_na=False, \
                              drop_first=False)
    
    # Concatenate dummy dataframe to original 
    df = pd.concat([df, dummy_df], axis=1)
    
    # Create addl. features
    df['p_w_d'] = np.where((df['partner_encoded'] == 1) & (df['dependents_encoded'] == 1), 1, 0)
    df['p_no_d'] = np.where((df['partner_encoded'] == 1) & (df['dependents_encoded'] == 0), 1, 0)
    df['d_no_p'] = np.where((df['partner_encoded'] == 0) & (df['dependents_encoded'] == 1), 1, 0)
    df['no_pod'] = np.where((df['partner_encoded'] == 0) & (df['dependents_encoded'] == 0), 1, 0)
    
    
    # Rename significant features for ease of use
    df = df.rename(columns={'payment_type_Electronic check': 'e_check', \
                   'contract_type_Month-to-month': 'm2m', \
                   'contract_type_One year': 'yr1', \
                   'contract_type_Two year': 'yr2', \
                   'internet_service_type_DSL': 'DSL', \
                   'internet_service_type_Fiber optic': 'fiber', \
                   'internet_service_type_None': 'no_int', \
                   'payment_type_Bank transfer (automatic)': 'a_bank_tr', \
                   'payment_type_Credit card (automatic)': 'a_ccard', \
                   'payment_type_Electronic check': 'e_check', \
                   'payment_type_Mailed check': 'm_check'
                  }) 
   
    return df
