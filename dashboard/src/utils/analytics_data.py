import boto3
import streamlit as st
import pandas as pd
from boto3.dynamodb.types import TypeDeserializer


def get_analytics_data():
    # Connect to dynamodb
    dynamodb = boto3.client(
        "dynamodb",
        aws_access_key_id=st.secrets['AWS']["AWS_ACCESS_KEY_ID"],
        aws_secret_access_key=st.secrets['AWS']["AWS_SECRET_ACCESS_KEY"],
        region_name=st.secrets['AWS']["AWS_REGION_NAME"]
    )
    df_dicts = {}
    
    # get top 25 data
    response_top_25 = dynamodb.scan(TableName="anime-dashboard-top-25")
    
    # convert to pandas dataframe
    df_dicts['top_25'] = parse_analytics_data(response_top_25['Items'])
    
    
    return df_dicts


def _deserialize(data):
    deserializer = TypeDeserializer()
    return {k: deserializer.deserialize(v) for k, v in data.items()}

def parse_analytics_data(data):
    deserialized_data = [_deserialize(x) for x in data]
    data = [pd.json_normalize(x, 'data', ['timestamp']) for x in deserialized_data]
    return pd.concat(data, ignore_index=True)