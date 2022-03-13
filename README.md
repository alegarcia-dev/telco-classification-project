# Reducing Customer Churn at Telco
<img src="TelcoCo.png" alt="drawing" width="70"/>

This repository contains all deliverables for the Telco classification project including additional files used 
in the process of producing the final deliverables.

**Repository Format**
- README.md: Contains a full outline of the project as well as information regarding the format of the repository 
and instructions for reproducing the results.
- Telco_Final_Report.ipynb: The final report containing a high level overview of the project including key takeaways, 
final results, and a recommended course of action.
- predictions.csv: A list of customers predicted as either likely to churn or not likely to churn produced by our
final prediction model.
- notebooks:
    - acquire.ipynb: A detailed and thorough overview of the data acquisition process.
    - prepare.ipynb: A detailed and thorough overview of the data preparation process.
    - explore.ipynb: A detailed and thorough overview of the exploratory analysis process along with key takeaways.
    - model.ipynb: A detailed and thorough overview of the modeling process including key takeaways.
- util:
    - acquire.py: Contains functions used for acquiring the Telco customer data.
    - prepare.py: Contains functions used for preparing and tidying the Telco customer data.
    - explore.py: Contains functions used for visualizing key findings.
    - model.py: Contains functions used for producing and visualizing ML model results.
---

## Table of Contents

1. [Project Goals](#project-goals)
2. [Project Description](#project-description)
3. [Initial Questions](#initial-questions)
4. [Data Dictionary](#data-dictionary)
5. [Instructions for Reproducing the Results](#instructions-for-reproducing-the-results)
6. [Outline of Project Plan](#outline-of-project-plan)
    1. [Data Acquisition](#data-acquisition)
    2. [Data Preparation](#data-preparation)
    3. [Exploratory Analysis](#exploratory-analysis)
    4. [Modeling](#modeling)
7. [Key Takeaways and Recommendations](#key-takeaways-and-recommendations)

## Project Goals

The goal of this project is to identify drivers of customer churn at Telco, produce a prediction model to identify 
which customers are at the highest risk of churning, and offer a recommendation for reducing customer churn.

## Project Description

Telco customers are churning at an unacceptably high rate which is affecting the company's bottom line. Retaining
existing customers costs far less than signing new customers. As such we want to reduce churn in order to help
the Telco's bottom line rather than relying on signing new customers to make up the difference. We will compare
and contrast customers who have churned versus those who haven't to determine the attributes that are driving 
customers to churn. We will produce a prediction model to help identify the customers that are at the highest risk 
of churning and we will provide a list of customers who are likely to churn (provided in predictions.csv). Finally, 
we will offer a recommended course of action to help promote customer retention.

## Initial Questions

Initial analysis of the data was conducted by answering these questions:

- Are customers who have been with Telco a longer time less likely to churn?
- Do customers with high monthly charges churn more frequently?
- Are customers on a month to month contract more likely to churn?
- Are customers with automatic payment setup less likely to churn?
- Is there a difference in churn frequency between customers with phone service and those without?
- Is there a relationship between customers who churn and internet service type?
- Is there a relationship between gender and customers who churn?
- Are senior citizens more likely to churn?

## Data Dictionary

| Variable              | Meaning      |
| --------------------- | ------------ |
| churn                 | Whether or not a customer has churned, "Yes" for did churn or "No" for did not churn. |
| tenure                | The number of months a customer has been with Telco represented as an integer value. |
| monthly_charges       | A customer's total monthly charges represented as a decimal value. |
| contract_type         | A customer's contract type (Month-to-month, One year, or Two year). |
| payment_type          | A customer's method of payment (Electronic check, Mailed check, Bank transfer (automatic), or Credit card (automatic)). |
| phone_service         | Whether or not a customer has phone service, "Yes" for does have phone service or "No" for does not have phone service. |
| internet_service_type | Type of internet service a customer has (DSL, Fiber optic, or None) |
| gender                | A customer's gender (Female or Male) |
| senior_citizen        | Whether or not a customer is a senior citizen, 0 for is not a senior citizen or 1 for is a senior citizen |

## Instructions for Reproducing the Results

1. Clone this repository using the following command
```
git clone git@github.com:alegarcia-dev/telco-classification-project.git
```
2. You will need to have pandas, numpy, matplotlib, seaborn, and sklearn installed.
3. You will also need login credentials for the MySQL database hosted at data.codeup.com.
4. Save your login credentials in a env.py file in the following form:
```python
username = 'your_username'
password = 'your_password'
hostname = 'data.codeup.com'
```
5. Ensure that the util directory along with its contents (acquire.py, prepare.py, explore.py, and model.py) are in the same working directory
as Telco_Final_Report.ipynb.
6. Open the Telco_Final_Report.ipynb notebook in Jupyter Notebooks.
7. The notebook uses a random seed to ensure all results are reproducible. Simply execute the code blocks in order to reproduce the results.

For details on the underlying code being executed refer to the python files in the util directory. For detailed breakdowns of each phase
of the pipeline refer to the notebooks in the notebooks directory. These notebooks are split into each individual phase of the pipeline:
- acquire.ipynb
- prepare.ipynb
- explore.ipynb
- model.ipynb

These notebooks are designed to run on their own without any outside files.

## Outline of Project Plan
---
### Data Acquisition

The Telco customer data used in this project is acquired from the telco_churn database hosted at data.codeup.com. After 
running the project notebook for the first time this dataset is saved to a local telco.csv file, for quicker access, which 
is not included in this repository.

- The acquire.ipynb notebook located in the notebooks directory provides a very thorough walkthrough of how the acquisition 
process was performed and details on how to reproduce the work from scratch.

- The acquire.py file located in the util directory provides all the functions used by the final report notebook with documentation
describing how to use each function.

**Steps Taken:**
1. Create and test function to acquire our data from either the database or .csv file if it exists.
2. Add the acquire function to acquire.py.

### Data Preparation

**Preparing Data**:

To prepare the dataset for exploratory analysis and modeling we needed to remove redundant columns and deal with missing or otherwise
unusual values. Missing values could be values that are absent in one form or another and unusual values could be values that do not match
the form that the majority of data in a single column follow. Redundant columns would be columns that essentially represent the same data
as another column.

- The prepare.ipynb notebook located in the notebooks directory provides a very thorough walkthrough of how the preparation
process was performed with details on how to reproduce the work from scratch.

- The prepare.py file located in the util directory provides all the functions used by the final report notebook with documentation
describing how to use each function.

**Missing Values**:

A small number of rows with missing values in the total_charges column were identified (11 out of 7043). It was decided that these
rows could be removed from the dataset without affecting our final results.

**Data Split**:

The data was split into train, validate and test datasets with the proportions 56%, 24% and 20% respectively. All exploratory analysis
is performed on the train dataset.

**Steps Taken:**
1. Identify missing values in the dataset.
2. Remove rows with missing values.
3. Identify redundant or otherwise useless columns.
4. Remove redundant and useless columns.
5. Encode categorical features into numeric columns.
6. Create a function for each step of the preparation process.
7. Gather all preparation functions into a single data prep function.
8. Create a function for splitting our data.

### Exploratory Analysis

Once the data was prepared we began analyzing the data to identify potential drivers of churn. This was done through univariate, 
bivariate, and multivariate analysis in order to identify which features were most likely driving customer churn and how these
features relate to each other.

After identifying the most likely drivers of churn statistical tests were performed to determine if our conclusion were valid.

- The explore.ipynb notebook located in the notebooks directory provides a very thorough walkthrough of how the exploration
process was performed with details on how to reproduce the work from scratch.

- The explore.py file located in the util directory provides all the functions used by the final report notebook with documentation
describing how to use each function.

**Steps Taken:**
1. Conduct univariate analysis on all features identified as potential drivers in our initial questions.
2. Conduct bivariate analysis on all features identified as potential drivers in our initial questions.
3. Summarize key takeaways and formulate additional questions to answer.
4. Conduct multivariate analysis on all the features identified as most likely drivers of churn.
5. Summarize key takeaways.
6. Conduct statistical tests on all features identified as drivers of churn.
7. Summarize key takeaways.

### Modeling

With our most likely drivers of churn identified we moved forward with creating some machine learning models that would allow us
to identify customers that are likely to churn so that action can be taken to retain these customers. Three different models were
created to predict customer churn and the performance of these were compared primarily by there recall scores and secondarily by
there accuracy scores.

We chose to focus on recall because the cost of signing new customers is greater than the cost of retaining an existing. As such
the cost of falsely identifying a customer as not likely to churn is greater than the cost of falsely identifying a customer as
likely to churn. This aligns with the goal of optimizing for recall which is to reduce missed positive cases.

- The model.ipynb notebook located in the notebooks directory provides a very thorough walkthrough of how the modeling process
was performed with details on how to reproduce the work from scratch.

- The model.py file located in the util directory provides all the functions used by the final report notebook with documentation
describing how to use each function.

**Steps Taken:**
1. Establish a baseline model.
2. Measure the performance of the baseline model.
3. Split our datasets into X and y where X is the features identified in exploration and y is the target variable churn.
4. Create a decision tree model.
5. Create a random forest model.
6. Create a k nearest neighors model.
7. Test the performance of all models and the baseline on the validate dataset.
8. Choose the top performer.

---
## Key Takeaways and Recommendations

The decision tree model was determined to be the best performing model. For more information refer to Telco_Final_Report.ipynb. For a detailed
breakdown of the results refer to model.ipynb in the notebooks directory.

Here I will provide my recommended course of action formulated with the help of the decision tree model breakdown:
- Customers identified as likely to churn who have less than 17 months of tenure should be offered a reduced monthly rate to bring their monthly charges below 68 dollars until they reach 17 months of tenure. If their monthly bill is already below 68 dollars they can be offered an incentive to utilize a different form of payment.
- Customers identified as likely to churn who have more than 17 months of tenure should be offered a discounted rate to reduce their monthly charges by a small percentage.

[Back to top](#reducing-customer-churn-at-telco)