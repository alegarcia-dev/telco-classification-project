####################
#
#   acquire.py
#   ----------
#   
#   Description:
#       Provides functions for acquiring and cacheing telco dataset.
#
#   Fields:
#       _telco_file
#       _telco_db
#
#   Functions:
#       get_db_url(database_name, username = username, password = password, hostname = hostname)
#       _get_telco_sql()
#       get_telco_data(use_cache = True)
#
####################

import pandas as pd
import os

if os.path.exists('env.py'):
    from env import username, password, hostname
else:
    username, password, hostname = '', '', ''

# File name and database name for Telco dataset

_telco_file = 'telco.csv'
_telco_db = 'telco_churn'

####################

def get_db_url(database_name: str, username: str = username, password: str = password, hostname: str = hostname) -> str:
    '''
        Return the URL needed to read data from the mysql database.

        It is recommended that you create a env.py file containing your login
        credentials before using this function. Otherwise, be sure to pass
        your login credentials as arguments to the function.

        Parameters
        ----------
        database_name: str
            The name of the database that needs to be accessed.

        username: str, default env.username
            The user's username to access the database. Default is to get the
            username from the env.py file.

        password: str, default env.password
            The user's password to access the database. Default is to get the 
            password from the env.py file.

        hostname: str, default env.hostname
            The hostname of the database. Default is to get the hostname from
            the env.py file.

        Returns
        -------
        str: A string value containing the URL needed to access the mysql
            database.
    '''

    return f'mysql+pymysql://{username}:{password}@{hostname}/{database_name}'

####################

def _get_telco_sql() -> str:
    '''
        Returns the SQL code required to retrieve the telco dataset
        from the MySQL database.
    '''

    return '''
        SELECT *
        FROM customers
        JOIN payment_types USING (payment_type_id)
        JOIN internet_service_types USING (internet_service_type_id)
        JOIN contract_types USING (contract_type_id);
    '''

####################

def get_telco_data(use_cache: bool = True) -> pd.core.frame.DataFrame:
    '''
        Return a dataframe containing data from the telco dataset.

        If a telco.csv file containing the data does not already
        exist the data will be cached in that file inside the current
        working directory. Otherwise, the data will be read from the
        .csv file.

        Parameters
        ----------
        use_cache: bool, default True
            If True the dataset will be retrieved from a csv file if one
            exists, otherwise, it will be retrieved from the MySQL database. 
            If False the dataset will be retrieved from the MySQL database
            even if the csv file exists.

        Returns
        -------
        DataFrame: A Pandas DataFrame containing the data from the telco
            dataset is returned.
    '''

    # If the file is cached, read from the .csv file
    if os.path.exists(_telco_file) and use_cache:
        return pd.read_csv(_telco_file)
    
    # Otherwise read from the mysql database
    else:
        df = pd.read_sql(_get_telco_sql(), get_db_url(_telco_db))
        df.to_csv(_telco_file, index = False)
        return df