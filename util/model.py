####################
#
#   model.py
#   --------
#   
#   Description:
#       Provides functions for creating and testing machine
#       learning models.
#
#   Fields:
#       None
#
#   Functions:
#       create_baseline_model(column)
#       measure_model_performance(y_true, *y_pred, positive_label = 1)
#       split_into_X_and_y(df: pd.core.frame.DataFrame)
#       create_models(df: pd.core.frame.DataFrame)
#       visualize_performance_of_models(df)
#       make_predictions_on_test(df)
#
####################

import pandas as pd

from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score

####################

def create_baseline_model(column: pd.core.series.Series) -> pd.core.series.Series:
    '''
        Returns a pandas series containing the most common
        value in the target variable that is of the same
        size as the provided column. This series serves as
        the baseline model to which to compare any machine
        learning models.

        Parameters
        ----------
        column: Series
            A pandas series containing the target variable
            for a machine learning project.

        Returns
        -------
        Series: A pandas series with the same size as 
            column filled with the most common value in
            column.
    '''

    most_common_value = column.mode()[0]
    return pd.Series([most_common_value] * column.size)

####################

def measure_model_performance(y_true: pd.core.series.Series, *y_pred, positive_label = 1, labels = None) -> pd.core.frame.DataFrame:
    '''
        Returns a dataframe containing the accuracy, precision,
        and recall scores for the model predictions provided.

        Parameters
        ----------
        y_true: Series
            A pandas series containing the true values for the
            target variable being predicted.

        *y_pred: Series or Array
            One or more pandas series or numpy arrays containing
            the predictions for the target variable.

        positive_label: int or string, default 1
            The positive value for the target variable.

        labels: list of strings, default None
            The labels to use as the name for each model. If not
            provided the default will be a numeric index starting
            from 0.

        Returns
        -------
        DataFrame: A pandas dataframe containing the accuracy,
            precision, and recall scores for each set of predictions
            provided in y_pred.
    '''

    scores = []
    
    for index, predictions in enumerate(y_pred):
        scores.append({
            'model' : index if not labels else labels[index],
            'accuracy' : accuracy_score(y_true, predictions),
            'precision' : precision_score(y_true, predictions, pos_label = positive_label, zero_division = 0),
            'recall' : recall_score(y_true, predictions, pos_label = positive_label, zero_division = 0)
        })
        
    df = pd.DataFrame(scores)
    return df.set_index('model')

def split_into_X_and_y(df: pd.core.frame.DataFrame):
    '''
        Split the dataframe into X and y where X is the
        dataframe with the selected features included and
        y is the target variable.

        Parameters
        ----------
        df: DataFrame
            The expected argument is a pandas dataframe containing the
            Telco customer dataset.

        Returns
        -------
        DataFrame, DataFrame: Two dataframes, one with the selected
            features another with the target variable.
    '''

    features = [
        'monthly_charges',
        'tenure',
        'contract_type_one_year',
        'contract_type_two_year',
        'payment_type_credit_card_automatic',
        'payment_type_electronic_check',
        'payment_type_mailed_check'
    ]
    return df[features], df.churn

def create_models(df: pd.core.frame.DataFrame, random_seed = 24):
    '''
        Create a decision tree model, a random forest model,
        and a k nearest neighbors model using the provided
        dataframe.

        Parameters
        ----------
        df: DataFrame
            The expected argument is a pandas dataframe containing the
            Telco customer dataset.

        Returns
        -------
        dict: A dictionary containing the name and trained model of
            each model created.
    '''

    X, y = split_into_X_and_y(df)

    model_1 = DecisionTreeClassifier(max_depth = 5, random_state = random_seed)
    model_1.fit(X, y)

    model_2 = RandomForestClassifier(max_depth = 5, random_state = random_seed)
    model_2.fit(X, y)

    model_3 = KNeighborsClassifier(n_neighbors = 10, weights = 'uniform')
    model_3.fit(X, y)

    return {
        'Baseline' : None,
        'Decision Tree' : model_1,
        'Random Forest' : model_2,
        'K Nearest Neighbors' : model_3
    }

def visualize_performance_of_models(df: pd.core.frame.DataFrame, models) -> pd.core.frame.DataFrame:
    '''
        Return a dataframe containing the accuracy, precision, and
        recall scores for each of our models.

        Parameters
        ----------
        df: DataFrame
            The expected argument is a pandas dataframe containing the
            Telco customer dataset.

        models: sklearn models
            One or more trained sklearn machine learning models with
            names for each model.

        Returns
        -------
        DataFrame: A dataframe containing the metric scores for each
            model.
    '''

    X, y = split_into_X_and_y(df)
    models['Baseline'] = create_baseline_model(y)
    
    metrics = measure_model_performance(
        y,
        models['Baseline'],
        models['Decision Tree'].predict(X),
        models['Random Forest'].predict(X),
        models['K Nearest Neighbors'].predict(X),
        positive_label = 'Yes',
        labels = list(models.keys())
    )

    return metrics

def make_predictions_on_test(df: pd.core.frame.DataFrame, original_df: pd.core.frame.DataFrame, model) -> pd.core.frame.DataFrame:
    '''
        Returns the accuracy, precision, and recall score
        for the model provided tested on the test dataset.
        Additionally, writes the resulting predictions to
        the predictions.csv file.

        Parameters
        ----------
        df: DataFrame
            The expected argument is a pandas dataframe containing the
            Telco customer dataset. This should be the test dataset.

        model: sklearn model
            An sklearn machine learning model. This should be the model
            chosen as the best performing model.

        Returns
        -------
        DataFrame: A dataframe containing the metric scores for the
            model.
    '''

    X, y = split_into_X_and_y(df)

    metrics = measure_model_performance(
        y,
        model.predict(X),
        positive_label = 'Yes',
        labels = ['Decision Tree']
    )

    write_predictions_to_file(
        y,
        model.predict_proba(X),
        model.predict(X),
        original_df
    )

    return metrics

def write_predictions_to_file(y, prob, pred, customers):
    '''
        Write predictions to predictions.csv
    '''

    predictions = pd.DataFrame(
        {
            'index' : y.index,
            'probability' : list(pd.DataFrame(prob)[1]),
            'prediction' : list(pred)
        }
    )

    columns = ['customer_id', 'probability', 'prediction']
    customers['index'] = customers.index
    predictions = customers.merge(predictions, left_on = ['index'], right_on = ['index'])[columns]

    predictions.to_csv('predictions.csv', index = False)

def percentage_of_customers_that_churned(df: pd.core.frame.DataFrame) -> None:
    '''
        Return the percentage of customers that churned in the
        provided dataframe.

        Parameters
        ----------
        df: DataFrame
            The expected argument is a pandas dataframe containing the
            Telco customer dataset.
    '''

    percentage = (df.churn == 'Yes').mean()
    print('Percentage of customers in the test dataset that churned:')
    print(f'{percentage:.2%}')

def reduced_percentage(original: float, reduction: float):
    '''
        Print the reduced percentage of the given percentage using
        the second given percentage.

        Parameters
        ----------
        original: float
            The starting percentage we are reducing.

        reduction: float
            The amount in percentage to reduce original by.
    '''

    print('Percentage of customers in the test dataset that churned')
    print('with the 41% we identified not churning:')
    print(f'{original - original * reduction:.2%}')