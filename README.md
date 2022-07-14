# Understanding Churn: Analyzing and Modeling Churn using Classification


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

1. Ask 4 distinct questions of our data \
  a. Do M2m customers churn more than 1-yr or 2-yr customers? \
  b. Does paying by electronic check influence churn? Do customers paying by electronic check churn more than other        payment types? \
  c. Do customers with Fiber churn more than other internet service types? \
  d. Do adults with dependents churn more than adults without dependents? Furthermore, are single adults more likely to churn than customers with a partner? \
2. Explore these questions through visualizations \
  a. Barplots are used primarily due to our features being categorical variables \
  b. These plots illustrate statistical significance of our chosen features \
3. Statistical Testing is conducted on all relevant features to determine statistical significance \
4. Summary includes key takeaways from all features explored \

#### Modeling and Evaluate

1. Select Evaluation Metric: Accuracy
2. Evaluate a Baseline: ~73%
3. Develop 3 distinct models
4. Evaluate on Train and then on Validate (for promising feature sets)
5. Once a top performing model is selected, evaluate on test dataset


### Conclusion

#### Summary

In seeking solutions to Telco's churn, we have explored a multiplicity of factors in the dataset that affect churn rate. We have shown that some potential primary drivers of churn are :

- Having a month-to-month contract
- Paying by electronic check 
- Paying for fiber internet
- Having a contract as a single adult, without a partner or dependents.

The statistical significance of these features, combined within our analysis and models, expresses 95% confidence in the validity of our findings. With the addition of the other features within contract type, payment type, internet type, and family type, we have created robust models that perform significantly better than our baseline of 73%.

Having fit the best performing model to our train, validate, and test datasets, we expect this model to perform with 80% accuracy in the future on data it has not seen, given no major changes to our data source.

#### Recommendations

There are a number of recommendations that can be offered based on the above analysis. These suggestions are tied directly to the findings within each of our primary drivers of churn:

1. Month-to-Month contracts - Although month-to-month contracts are here to stay, we could feasibly limit churn by offering a discount on 1 and 2 yr contracts. By offering a discount that still maintains a healthy profit margin, we could incentivize customers to sign on for longer contracts which is shown to reduce churn in the long term.

2. Electronic check - We have shown that churn is significantly higher for electronic check customers than any other payment type. Although there are multiple potential solutions to this phenomenon, I believe Telco needs to perform a full review of the customer process for submitting payment via electronic check. It is my experience that online portals for submitting payment by e-check can be inefficient, not well designed, and frustrating to the user. This could be a significant reason why customers who use this method of payment are cancelling their contracts.

3. Fiber internet - Customers with this internet type express a significant likelihood of churn, despite Fiber being the optimal option for internet access. Although fiber is undoubtedly more expensive to implement, due to infrastructure costs, the amount of potential churn of this internet type needs to inform our business practices. Options include a potential discount for fiber customers if this is profitably viable. Otherwise, increased company investment in fiber infrastructure may lead to increased profit margin down the road, allowing the company greater leverage for retaining these customers. 

4. Customers with no partner or dependents (single adults) - This customer demographic has a significant likelihood of churn. Yet, attempting to retain these customers may not be the most effective option for maximizing customer retention. Instead, by observing the likelihood of churn for other partner/dependent statuses, we find that customers with dependents are less likely to churn. Therefore, offering a family discount for those customers who have dependents could attract more customers who fall under this demographic. This customer base has shown to be less likely to churn, thus decreasing potential churn by attracting more stable and committed customers.

#### Next Steps

Despite the overall effectiveness of our best-performing model, there is always room for improvement and optimization. \
If given more time to pursue a better results, I would begin by further exploration and analysis of other features within our dataset. Through additional exploration I've already performed, I can say with confidence that there are a number of features I could analyze and implement into my models to improve prediction accuracy. \
Namely, observing features such as whether a customer has online security or tech support could improve our models' predictions.

Additionally, prompting customers who churn to fill out a simple satisfaction survey could produce meaningful insight into more specific reasons customers choose to cancel their contracts. This information could be analyzed using methods such as Natural Language Processing in order to improve Telco's understanding of its customers' needs and the resulting customer service they provide.

