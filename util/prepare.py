####################
#
#   prepare.py
#   ----------
#   
#   Description:
#       Provides functions for preparing and splitting the Telco dataset for 
#       exploratory analysis.
#
#   Fields:
#       None
#
#   Functions:
#       _drop_useless_columns(df)
#       _remove_missing_values(df)
#       _combine_duplicate_values(df)
#       _encode_categorical_features(df)
#       _clean_column_names(df)
#       prep_telco_data(df)
#       split_data(df, stratify, random_seed = 24)
#
####################

import pandas as pd
from sklearn.model_selection import train_test_split

####################

def _drop_useless_columns(df: pd.core.frame.DataFrame) -> pd.core.frame.DataFrame:
    '''
        Accepts the telco dataset and removes columns that are either useless
        for our purposes or are redundant.

        Parameters
        ----------
        df: DataFrame
            The expected argument is a Pandas DataFrame containing the telco
            dataset.

        Returns
        -------
        DataFrame: A Pandas DataFrame with the columns customer_id, 
            contract_type_id, internet_service_type_id, and payment_type_id
            removed.
    '''

    cols_to_drop = [
        'customer_id',
        'contract_type_id',
        'internet_service_type_id',
        'payment_type_id'
    ]
    return df.drop(columns = cols_to_drop)

####################

def _remove_missing_values(df: pd.core.frame.DataFrame) -> pd.core.frame.DataFrame:
    '''
        Accepts the telco dataset and removes rows containing missing values
        in the total_charges column.

        Parameters
        ----------
        df: DataFrame
            The expected argument is a Pandas DataFrame containing the telco
            dataset.

        Returns
        -------
        DataFrame: A Pandas DataFrame containing the telco dataset with the
            rows containing missing values in the total_charges column
            removed.
    '''

    does_not_have_zero_tenure = df.tenure != 0
    df = df[does_not_have_zero_tenure]
    df.total_charges = df.total_charges.astype('float')
    return df

####################

def _combine_duplicate_values(df: pd.core.frame.DataFrame) -> pd.core.frame.DataFrame:
    '''
        Accepts the telco dataset and combines duplicate values "No" and
        "No ... service" in the multiple_lines, online_security, online_backup,
        device_protection, tech_support, streaming_tv, and streaming_movies
        columns.

        Parameters
        ----------
        df: DataFrame
            The expected argument is a Pandas DataFrame containing the telco
            dataset.

        Returns
        -------
        DataFrame: A Pandas DataFrame containing the telco dataset redundant
            values "No" and "No ... service" combined into a single "No" value.
    '''

    columns = [
        'multiple_lines',
        'online_security',
        'online_backup',
        'device_protection',
        'tech_support',
        'streaming_tv',
        'streaming_movies'
    ]

    for column in columns:
        df[column] = np.where(df[column] == 'Yes', 'Yes', 'No')
    
    return df

####################

def _encode_categorical_features(df: pd.core.frame.DataFrame) -> pd.core.frame.DataFrame:
    '''
        Accepts the telco dataset and encodes all non numeric categorical features.

        Parameters
        ----------
        df: DataFrame
            The expected argument is a Pandas DataFrame containing the telco
            dataset.

        Returns
        -------
        DataFrame: A Pandas DataFrame with all non numeric categorical features
            encoded in numeric columns.
    '''

    categorical_cols = df.dtypes[df.dtypes == 'object'].index

    dummy_df = pd.get_dummies(df[categorical_cols], dummy_na = False, drop_first = True)
    return pd.concat([df, dummy_df], axis = 1)

####################

def _clean_column_names(df: pd.core.frame.DataFrame) -> pd.core.frame.DataFrame:
    '''
        Accepts the telco dataset and cleans all column names so that spaces
        are replaced by underscores, all letters are lowercased, and parantheses
        are replaced by empty strings.

        Parameters
        ----------
        df: DataFrame
            The expected argument is a Pandas DataFrame containing the telco
            dataset.

        Returns
        -------
        DataFrame: A Pandas DataFrame with all column names cleaned.
    '''

    df.columns = df.columns.str.replace(' ', '_', regex = False).str.lower()
    df.columns = df.columns.str.replace('\(|\)', '', regex = True)
    return df

####################

def prep_telco_data(df: pd.core.frame.DataFrame) -> pd.core.frame.DataFrame:
    '''
        Accepts the telco dataset and performs transformations to prepare the data
        for exploratory analysis.

        Parameters
        ----------
        df: DataFrame
            The expected argument is a Pandas DataFrame containing the telco
            dataset.

        Returns
        -------
        DataFrame: A Pandas DataFrame containing the telco dataset with transformations.
            The resultant dataframe has the customer_id, contract_type_id, 
            internet_service_type_id, and payment_type_id columns removed, and encoded
            variables for all categorical columns (all non-numeric columns except customer_id
            and total_charges). Rows with customers of 0 tenure are also removed.
    '''

    df = df.drop_duplicates()
    df = _drop_useless_columns(df)
    df = _remove_missing_values(df)
    df = _combine_duplicate_values(df)
    df = _encode_categorical_features(df)
    df = _clean_column_names(df)

    return df

####################

def split_data(df: pd.core.frame.DataFrame, stratify: str, random_seed: int = 24) -> tuple[
    pd.core.frame.DataFrame,
    pd.core.frame.DataFrame,
    pd.core.frame.DataFrame
]:
    '''
        Accepts a DataFrame and returns train, validate, and test DataFrames.
        Splits are performed randomly.

        Proportion of original dataframe that each return dataframe comprises.
        ---------------
        Train:      56% (70% of 80%)
        Validate:   24% (30% of 80%)
        Test:       20%

        Parameters
        ----------
        df: DataFrame
            A Pandas DataFrame containing prepared data. It is expected that
            the input to this function will already have been prepared and
            tidied so that it will be ready for exploratory analysis.

        stratify: str
            A string value containing the name of the column to be stratified
            in the sklearn train_test_split function. This parameter should
            be the name of a column in the df dataframe.

        random_seed: int, default 24
            An integer value to be used as the random number seed. This parameter
            is passed to the random_state argument in the sklearn train_test_split
            function.

        Returns
        -------
        tuple : A tuple containing three Pandas DataFrames for train, validate
            and test datasets.    
    '''
    test_split = 0.2
    train_validate_split = 0.3

    train_validate, test = train_test_split(
        df,
        test_size = test_split,
        random_state = random_seed,
        stratify = df[stratify]
    )
    
    train, validate = train_test_split(
        train_validate,
        test_size = train_validate_split,
        random_state = random_seed,
        stratify = train_validate[stratify]
    )
    return train, validate, test