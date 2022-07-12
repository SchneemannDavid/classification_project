from sklearn.model_selection import train_test_split


# Split for Exploration

## 
# Train, Validate, Test Split Function: for exploration
def telco_split_explore(df):
    '''
    This function performs split on telco data, stratifying on churn.
    Returns train, validate, and test dfs.
    '''
    # 80/20 train test split
    train, test = train_test_split(df, train_size=0.8, random_state=123, stratify=df.churn)
    # 70/30 train validate split
    train, validate = train_test_split(train, train_size=0.7, random_state=123, stratify=train.churn)
    
    return train, validate, test

### ------------------------------------------------------------------------

# Split for Modeling: X & Y dfs
def telco_split_model(df):
    '''
    This function performs split on telco data, stratifying on churn.
    Returns both X and y train, validate, and test dfs
    '''
    
    # 80/20 train test split
    train, test = train_test_split(df, train_size=0.8, random_state=123, stratify=df.churn)
    # 70/30 train validate split
    train, validate = train_test_split(train, train_size=0.7, random_state=123, stratify=train.churn)
    
    x_vars = ['contract_type_Month-to-month', 'contract_type_One year', 'contract_type_Two year', 'payment_type_Bank transfer (automatic)', 'payment_type_Credit card (automatic)', 'payment_type_Electronic check', 'payment_type_Mailed check', 'no_pod', 'partner_w_dependents']
    y_vars = ['churn']

    x_train, y_train = train[x_vars], train[y_vars]
    x_validate, y_validate = validate[x_vars], validate[y_vars]
    x_test, y_test = test[x_vars], test[y_vars]
    

    return x_train, y_train, x_validate, y_validate, x_test, y_test


