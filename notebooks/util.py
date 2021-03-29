import numpy as np
import pandas as pd

def process_flat_type(df):
    df['flat_type'] = df['flat_type'].str.replace('-', ' ') # there are some flat_type encoded as 4-room and 4 room
    df.flat_type_ord = df.flat_type.map({
        '1_room':1,
        '2_room':2,
        '3_room':3,
        '4_room':4,
        '5_room':5,
        'executive':6,
        'multi_generation': 7
    })

    df = pd.get_dummies(df, columns=["flat_type"], drop_first=False)
    df.drop(columns = 'flat_type_multi generation')
    return df

def process_basic(df):
    df['year'] = df.month.str[:4].astype('int')
    df['lease_duration'] = df['year']-df['lease_commence_date']
    df['storey'] = (df.storey_range.str[-2:].astype('int') + df.storey_range.str[:2].astype('int'))/2
    df = pd.get_dummies(df, columns=["town"], drop_first=False)
    df = pd.get_dummies(df, columns=["flat_model"], drop_first=False)
    return df

def count_poi(df, poi, dist, feat):
    df[feat] = (poi < dist).sum(axis=1)
    return df

def join_pop(df, pop):
    return df.join(pop[['subzone', 'avg']], lsuffix='subzone', rsuffix='subzone')

def drop_cols(df):
    df.drop(columns=['subzonesubzone', 'latitude', 'longitude', 'region'], inplace=True)
    df.drop(columns = ['elevation', 'eco_category'], inplace=True) # confirm drop
    df.drop(columns = ['month', 'storey_range', 'block', 'street_name', 'planning_area', 'lease_commence_date'], inplace=True) # to discuss
    return df
