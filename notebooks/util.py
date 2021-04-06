import numpy as np
import pandas as pd

def process_flat_type(df):
    df['flat_type'] = df['flat_type'].str.replace('-', ' ')
    df = pd.get_dummies(df, columns=["flat_type"], drop_first=False)
    df.drop(columns = 'flat_type_multi generation')
    return df

def process_basic(df):
    df['year'] = df.month.str[:4].astype('int')
    df['lease_duration'] = df['year']-df['lease_commence_date']
    df['storey'] = (df.storey_range.str[-2:].astype('int') + df.storey_range.str[:2].astype('int'))/2
    df = pd.get_dummies(df, columns=['flat_model', 'town', 'year'], drop_first=True)
    return df

def count_poi(df, poi, dist, feat):
    df[feat] = (poi < dist).sum(axis=1)
    return df

def join_pop(df, pop):
    return df.join(pop[['subzone', 'avg']], lsuffix='subzone', rsuffix='subzone')

def drop_cols(df):
    df.drop(columns=['subzone', 'latitude', 'longitude', 'region'], inplace=True)
    df.drop(columns = ['elevation', 'eco_category'], inplace=True) # confirm drop
    df.drop(columns = ['month', 'storey_range', 'block', 'street_name', 'planning_area', 'lease_commence_date'], inplace=True) # to discuss
    return df
