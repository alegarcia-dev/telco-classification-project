# Reducing Customer Churn at Telco <img src="TelcoCo.png" alt="drawing" width="30"/>

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
    - detailed_report.ipynb: A reproducible notebook outlining the full project with technical details included.
    - acquire.ipynb: A detailed overview of the data acquisition process.
    - prepare.ipynb: A detailed overview of the data preparation process.
    - explore.ipynb: A detailed overview of the exploratory analysis process along with key takeaways.
    - model.ipynb: A detailed overview of the modeling process including key takeaways.
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

*pending*

## Outline of Project Plan

*in progress*

## Key Takeaways and Recommendations

*in progress*