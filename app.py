import streamlit as st
import requests

'''
# TaxiFareModel front
'''


with st.form(key='arguments'):

    pickup_date = st.date_input('pickup datetime')
    pickup_time = st.time_input('pickup time')
    pickup_datetime = f'{pickup_date} {pickup_time}'

    pickup_longitude = st.number_input('pickup_longitude', value=40.7614327)
    pickup_latitude = st.number_input('pickup_latitude', value=40.7614327)
    dropoff_longitude = st.number_input('dropoff_longitude', value=40.7614327)
    dropoff_latitude = st.number_input('dropoff_latitude', value=40.7614327)
    passenger_count = st.number_input('passenger_count', value=2)

    st.form_submit_button('Lets Predict')


url = 'https://taxifare.lewagon.ai/predict'

if url == 'https://taxifare.lewagon.ai/predict':

    params = dict(pickup_datetime=pickup_datetime,
                  pickup_longitude=pickup_longitude,
                  pickup_latitude=pickup_latitude,
                  dropoff_longitude=dropoff_longitude,
                  dropoff_latitude=dropoff_latitude,
                  passenger_count=passenger_count
                  )

    response = requests.get(url, params)

    prediction = response.json()

    pred = prediction['fare']

st.header(f'{pred}')
