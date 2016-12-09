
import pandas as pd



def make_df_filter(column,filter_set,dropna=True):
    """ Generates filter function for filtering out unneeded values from specified dataframe column. """

    def filter_column(df,dropna=dropna):
        ret_df=df.set_index([column]).ix[filter_set].reset_index()

        if dropna:
            return ret_df.dropna()
        else:
            return ret_df

    return filter_column


def make_subtractor(index_columns,signal_columns,back_label="back"):
    """
    Generate back subtraction function for pandas DataFrame. Generates function that will take in dataframe,
    will subtract mean of all back values from all other values.

    :param index_columns:
    :param back_columns:
    :param back_value:
    :return:
    """

    def subtract_back(df):
        """
        Subtracts background values from luciferase signal measurements.
        """
        column_back_values = {}
        for column in signal_columns:
            column_back_values[column] = df.set_index(index_columns)[column][back_label].mean()

        subtracted_series = []
        for column in signal_columns:
            back_mean = column_back_values[column]
            subtracted_series.append(
                df.set_index(index_columns)[column].apply(lambda x: x - back_mean))

        df_res = pd.concat(subtracted_series, axis=1).reset_index()
        df_res = df_res[~(df_res.Konstruktid == back_label)]
        return df_res

    return subtract_back


def make_meanscalculator(index_columns,signal_column):
    """Calculates signal column means"""

    def calculate_means(df):
        return df.groupby(index_columns)[signal_column].mean().reset_index()
    return calculate_means

