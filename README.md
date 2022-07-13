# classification_project

## About the Project
### Project Goals

My goal with this project is to identify Telco's key drivers of customer churn and to provide insight into why and how these factors are producing churn. With this information and the following recommendations, our organization can work together to improve business processes and procedures in order to minimize customer churn moving forward.


### Project Description

Losing customers, expressed as churn, is a real issue for the Telco Co. 

In today's business world, the cost of acquiring customers can be steep. Thus, businesses are seeking ways to retain the customers they already have through providing more options to consumers that can meet the needs of a diverse customer population. 

In order to meet the desire for customer retention at Telco Co., we will analyze the attributes (features) of customers who are more or less likely to churn. We will then develop models for predicting churn based on these attributes and provide recommendations and predictions to Telco for reducing churn and predicting churn for their customer base moving forward.


### Initial Questions

##### 1. Do M2m customers churn more than 1-yr or 2-yr customers?
    
- Ho = M2M customers churn <= 1&2-yr customers
- Ha = M2M customers churn > 1&2-yr customers

##### 2. Does paying by electronic check influence churn?

- Ho = Electronic check churn <= other payment types
- Ha = Electronic check churns > other payment types

##### 3. Do customers with Fiber churn more than other internet service types?

- Ho = Fiber internet churn <= DSL or no internet churn
- Ha = Fiber internet churn > DSL or no internet churn

##### 4. Do adults with dependents churn more than other family types?

- Ho = Adults with dependents churn <= adults without dependents and adults with just partner
- Ha = Adults with dependents churn > adults without dependents and adults with just partner


### Data Dictionary

| Variable      | Meaning |
| ----------- | ----------- |
| Churn      | Defines whether a customer left their service contract       |
| Monthly Charges   | The average monthly charge per customer        |
| m2m      | Customers who have month to month contracts       |
| yr1      | Customers who have 1-yr contracts       |
| yr2      | Customers who have 1-yr contracts       |
| a_bank_transfer   | Customers who pay via bank transfer (automatic)       |
| a_ccard      | Customers who pay via credit card (automatic)      |
| e_check      | Customers who pay via electronic check       |
| m_check      | Customers who pay via mailed check       |
| p_w_d   | Defines customers who have both a partner and dependents        |
| p_no_d      | Defines customers who have a partner but no dependents|
| d_no_p      | Defines customers who have dependents but no partner  |
| no_pod      | Defines customers who have neither a partner nor dependents       |


### Steps to Reproduce

1. You will need an env.py file that contains the hostname, username and password of the mySQL database that contains the telco dataset. Store that env file locally in the repository.
2. Clone my repo (including the acquire_telco.py, prepare.py and split_telco.py) 
   (confirm .gitignore is hiding your env.py file)
3. To acquire the telco data, I used the telco_db in our mySQL server. I selected all columns from the customers table. I then joined this table with the contract_type, payment_type, and internet_service_type tables.
4. Libraries used are pandas, matplotlib, seaborn, numpy, sklearn, scipy, and model. A full list of modules with specific tools are provided in my Full Report.
5. Following these steps, you should be able to run the full report


### The Plan
Below, I walk through all stages of my pipeline and process.

#### Wrangle
##### Modules (acquire_telco.py + prepare.py + telco_split.py)

1. Test acquire function
2. Add to acquire_telco.py module
3. Write and test function to clean data
4. Add to prepare.py module
5. Write and test function to split data
6. Add to split_telco.py module

#### Explore

1. Ask 4 distinct questions of our data
  a. Do M2m customers churn more than 1-yr or 2-yr customers?
  b. Does paying by electronic check influence churn? Do customers paying by electronic check churn more than other        payment types?
  c. Do customers with Fiber churn more than other internet service types?
  d. Do adults with dependents churn more than adults without dependents? Furthermore, are single adults more likely to churn than customers with a partner?
2. Explore these questions through visualizations
  a. Barplots are used primarily due to our features being categorical variables
  b. These plots illustrate statistical significance of our chosen features
3. Statistical Testing is conducted on all relevant features to determine statistical significance
4. Summary includes key takeaways from all features explored

#### Modeling and Evaluate

1. Select Evaluation Metric: Accuracy
2. Evaluate a Baseline: ~73%
3. Develop 3 distinct models
4. Evaluate on Train and then on Validate (for promising feature sets)
5. Once a top performing model is selected, evaluate on test dataset




