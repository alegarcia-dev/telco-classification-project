####################
#
#   explore.py
#   ----------
#   
#   Description:
#       Provides functions for visualizing key findings and performing
#       statistical tests to validate analysis conclusions.
#
#   Fields:
#       None
#
#   Functions:
#       distribution_of_customer_churn(df)
#       visualize_churn_rate_versus_contract_type(df)
#       visualize_churn_rate_versus_payment_type(df)
#       visualize_monthly_charges_versus_tenure(df)
#       visualize_churn_rate_versus_tenure(df)
#       perform_two_sample_ttest_on_monthly_charges(df)
#       perform_two_sample_ttest_on_tenure(df)
#       perform_chi2_test_on_contract_type(df)
#       perform_chi2_test_on_tech_support(df)
#
####################

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from util.stats_util import *

def distribution_of_customer_churn(df: pd.core.frame.DataFrame) -> None:
    '''
        Display a histogram visualizing the distribution of churn in
        Telco customer dataset.

        Parameters
        ----------
        df: DataFrame
            The expected argument is a pandas dataframe containing the
            Telco customer dataset.
    '''

    sns.histplot(df.churn)
    plt.title('Customers that churn make up roughly a quarter of the customer population')
    plt.show()

def visualize_churn_rate_versus_contract_type(df: pd.core.frame.DataFrame) -> None:
    '''
        Display a histogram visualizing the distribution of customers
        who have churned and those that haven't versus the contract
        type.

        Parameters
        ----------
        df: DataFrame
            The expected argument is a pandas dataframe containing the
            Telco customer dataset.
    '''

    churned = df[df.churn == 'Yes']
    not_churned = df[df.churn == 'No']

    sns.histplot(data = not_churned.contract_type, label = 'Not Churned', color = 'green')
    sns.histplot(data = churned.contract_type, label = 'Churned', color = 'red')
    plt.title('Most customers that are churning are on the month-to-month contract')
    plt.legend()
    plt.show()

def visualize_churn_rate_versus_tech_support(df: pd.core.frame.DataFrame) -> None:
    '''
        Display a histogram visualizing the distribution of customers
        who have churned and those that haven't versus tech support

        Parameters
        ----------
        df: DataFrame
            The expected argument is a pandas dataframe containing the
            Telco customer dataset.
    '''

    churned = df[df.churn == 'Yes']
    not_churned = df[df.churn == 'No']

    sns.histplot(data = not_churned.tech_support, label = 'Not Churned', color = 'green')
    sns.histplot(data = churned.tech_support, label = 'Churned', color = 'red')
    plt.title('Customers without tech support and higher monthly charges churn')
    plt.legend()
    plt.show()

def visualize_churn_rate_versus_tenure(df: pd.core.frame.DataFrame) -> None:
    '''

    '''

    churned = df[df.churn == 'Yes']
    not_churned = df[df.churn == 'No']

    sns.histplot(data = not_churned.tenure, label = 'Not Churned', color = 'green')
    sns.histplot(data = churned.tenure, label = 'Churned', color = 'red')
    plt.title('Most customers that are churning have low tenure')
    plt.legend()
    plt.show()

def visualize_monthly_charges_versus_tenure(df: pd.core.frame.DataFrame) -> None:
    '''
        Display a histogram visualizing the distribution of monthly charges
        for customers who have churned and have tenure less than or equal to
        24 months. Additionally the percentage of customers who have churned
        that are in this group is displayed.

        Parameters
        ----------
        df: DataFrame
            The expected argument is a pandas dataframe containing the
            Telco customer dataset.
    '''

    churn_customers = df[df.churn == 'Yes']
    print(f'Tenure less than or equal to 24, percentage of churn pop.: {(churn_customers.tenure <= 24).mean():.2%}')

    sns.histplot(data = churn_customers[churn_customers.tenure <= 24], x = 'monthly_charges')
    plt.title('Customers with 2 years or less of tenure that have churned')
    plt.show()

def perform_two_sample_ttest_on_monthly_charges(df: pd.core.frame.DataFrame) -> None:
    '''
        Conducts a two sample t-test on the dataset comparing the monthly
        charges of the two samples. The results are printed to the console.

        Parameters
        ----------
        df: DataFrame
            The expected argument is a pandas dataframe containing the
            Telco customer dataset.
    '''

    churn_customers = df[df.churn == 'Yes']
    not_churn_customers = df[df.churn == 'No']

    two_sample_ttest(churn_customers.monthly_charges, not_churn_customers.monthly_charges, alternative = 'greater')

def perform_two_sample_ttest_on_tenure(df: pd.core.frame.DataFrame) -> None:
    '''
        Conducts a two sample t-test on the dataset comparing the tenure
        of the two samples. The results are printed to the console.

        Parameters
        ----------
        df: DataFrame
            The expected argument is a pandas dataframe containing the
            Telco customer dataset.
    '''

    churn_customers = df[df.churn == 'Yes']
    not_churn_customers = df[df.churn == 'No']

    two_sample_ttest(churn_customers.tenure, not_churn_customers.tenure, alternative = 'less')

def perform_chi2_test_on_contract_type(df: pd.core.frame.DataFrame) -> None:
    '''
        Conducts a chi2 test between the contract type and churn features
        of the dataframe. The results are printed to the console.

        Parameters
        ----------
        df: DataFrame
            The expected argument is a pandas dataframe containing the
            Telco customer dataset.
    '''

    chi2_test(df.churn, df.contract_type)

def perform_chi2_test_on_tech_support(df: pd.core.frame.DataFrame) -> None:
    '''
        Conducts a chi2 test between the tech support and churn features
        of the dataframe. The results are printed to the console.

        Parameters
        ----------
        df: DataFrame
            The expected argument is a pandas dataframe containing the
            Telco customer dataset.
    '''

    chi2_test(df.churn, df.tech_support)