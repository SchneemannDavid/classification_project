from pandas import DataFrame
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
                              drop_first=True)
    
    # Concatenate dummy dataframe to original 
    df = pd.concat([df, dummy_df], axis=1)
    
    # Create addl. features
    df['partner_w_dependents'] = np.where((df['partner_encoded'] == 1) & (df['dependents_encoded'] == 1), 1, 0)
    df['partner_no_dependents'] = np.where((df['partner_encoded'] == 1) & (df['dependents_encoded'] == 0), 1, 0)
    df['dependents_no_partner'] = np.where((df['partner_encoded'] == 0) & (df['dependents_encoded'] == 1), 1, 0)
    df['male_w_dependents'] = np.where((df['partner_encoded'] == 0) & (df['dependents_encoded'] == 1) & (df['gender_encoded'] == 0), 1, 0)
    df['female_w_dependents'] = np.where((df['partner_encoded'] == 0) & (df['dependents_encoded'] == 1) & (df['gender_encoded'] == 1), 1, 0)
    # encode number_relationships by utilizing information from dependents_encoded and partner_encoded
    df['number_relationships'] = df['dependents_encoded'] + df['partner_encoded']
    
   
    return df




#### Split #####


def train_validate_test_split(df, seed=123):
    train_and_validate, test = train_test_split(
        df, test_size=0.2, random_state=seed, stratify=df.survived
    )
    train, validate = train_test_split(
        train_and_validate,
        test_size=0.3,
        random_state=seed,
        stratify=train_and_validate.survived,
    )
    return train, validate, test



def split(df, stratify_by=None):
    """
    Crude train, validate, test split
    To stratify, send in a column name
    """
    
    if stratify_by == None:
        train, test = train_test_split(df, test_size=.2, random_state=123)
        train, validate = train_test_split(train, test_size=.3, random_state=123)
    else:
        train, test = train_test_split(df, test_size=.2, random_state=123, stratify=df[stratify_by])
        train, validate = train_test_split(train, test_size=.3, random_state=123, stratify=train[stratify_by])
    
    return train, validate, test