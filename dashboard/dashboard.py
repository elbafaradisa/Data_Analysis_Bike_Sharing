import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

sns.set(style='dark') 


# Load dataset
day_df = pd.read_csv('cleaned_day_df.csv')
hour_df = pd.read_csv('cleaned_hour_df.csv')

# Mengubah nama value
day_df = day_df.replace({'season' : {1 : 'Spring', 2 : 'Summer', 3 : 'Fall', 4 : 'Winter'}},)
day_df = day_df.replace({'weathersit' : {1 : 'clear and few clouds', 2 : 'Mist and cloudy', 3 : 'Light snow or rain', 4 : 'Heavy rain'}})
day_df = day_df.replace({'holiday' : {0 : 'Not holiday', 1 : 'Holiday'}})
day_df = day_df.replace({'workingday' : {0 : 'Not workingday', 1 : 'Workingday'}})


# daily_total_rent_df
def create_daily_total_rent_df(df):
   daily_total_rent_df = df.resample(rule='D', on='dteday').agg({
      'cnt' : 'sum'
   })
   daily_total_rent_df = daily_total_rent_df.reset_index()
   daily_total_rent_df.rename(columns={
      'dteday' : 'Rental Date',
      'cnt' : 'Total User'
   }, inplace=True)

   return daily_total_rent_df

# daily_registerd_user_df
def create_daily_registered_rent_df(df):
   daily_registered_rent_df = df.resample(rule='D', on='dteday').agg({
      'registered' : 'sum'
   })
   daily_registered_rent_df = daily_registered_rent_df.reset_index()
   daily_registered_rent_df.rename(columns={
      'dteday' : 'Rental Date',
      'registered' : 'Registered User'
   }, inplace=True)

   return daily_registered_rent_df

# daily_casual_user_df
def create_daily_casual_rent_df(df):
   daily_casual_rent_df = df.resample(rule='D', on='dteday').agg({
      'casual' : 'sum'
   })
   daily_casual_rent_df = daily_casual_rent_df.reset_index()
   daily_casual_rent_df.rename(columns={
      'dteday' : 'Rental Date',
      'casual' : 'Casual User'
   }, inplace=True)

   return daily_casual_rent_df

# season_rent_df
def create_season_rent_df(df):
   season_rent_df = df.groupby('season').agg({
      'casual': 'sum',
      'registered': 'sum'
   })
   season_rent_df = season_rent_df.reset_index()
   season_rent_df.rename(columns={
      'casual' : 'Casual User',
      'registered' : 'Registered User'
   }, inplace=True)

   return season_rent_df

# weather_rent_df
def create_weather_rent_df(df):
   weather_rent_df = df.groupby('weathersit').agg({
      'casual': 'sum',
      'registered': 'sum'
   })
   weather_rent_df = weather_rent_df.reset_index()
   weather_rent_df.rename(columns={
      'casual' : 'Casual User',
      'registered' : 'Registered'
   }, inplace=True)

   return weather_rent_df

# holiday_rent_df
def create_holiday_rent_df(df):
   holiday_rent_df = df.groupby('holiday').agg({
      'casual': 'sum',
      'registered': 'sum'
   })
   holiday_rent_df = holiday_rent_df.reset_index()
   holiday_rent_df.rename(columns={
      'casual' : 'Casual User',
      'registered' : 'Registered'
   }, inplace=True)

   return holiday_rent_df

# workingday_rent_df
def create_workingday_rent_df(df):
   workingday_rent_df = df.groupby('workingday').agg({
      'casual': 'sum',
      'registered': 'sum'
   })
   workingday_rent_df = workingday_rent_df.reset_index()
   workingday_rent_df.rename(columns={
      'casual' : 'Casual User',
      'registered' : 'Registered'
   }, inplace=True)

   return workingday_rent_df

# hour_rent_df
def create_hour_rent_df(df):
   hour_rent_df = df.groupby('hr').agg({
      'casual' : 'sum',
      'registered' : 'sum'
   })
   hour_rent_df = hour_rent_df.reset_index()
   hour_rent_df.rename(columns={
      'hr' : 'Hour',
      'casual' : 'Casual User',
      'registered' : 'Registered User'
   }, inplace=True)

   return hour_rent_df

# Mengubah tipe data dteday menjadi datetime
day_df.sort_values('dteday', inplace=True)
day_df.reset_index(inplace=True)
day_df['dteday'] = pd.to_datetime(day_df['dteday'])

# Membuat komponen filter
min_date = day_df['dteday'].min()
max_date = day_df['dteday'].max()

with st.sidebar:

   #Mengambil start_date dan end_date dari date_input
   start_date, end_date = st.date_input(
      label='Rentang Waktu', min_value=min_date,
      max_value=max_date,
      value=[min_date, max_date]
   )

main_df = day_df[(day_df['dteday'] >= str(start_date)) &
         (day_df['dteday'] <= str(end_date))]

main_hour_df = hour_df[(hour_df['dteday'] >= str(start_date)) &
         (hour_df['dteday'] <= str(end_date))]

# DataFrame dari helper function
daily_total_rent_df = create_daily_total_rent_df(main_df)
daily_registered_rent_df = create_daily_registered_rent_df(main_df)
daily_casual_rent_df = create_daily_casual_rent_df(main_df)
season_rent_df = create_season_rent_df(main_df)
weather_rent_df = create_weather_rent_df(main_df)
holiday_rent_df = create_holiday_rent_df(main_df)
workingday_rent_df = create_workingday_rent_df(main_df)
hour_rent_df = create_hour_rent_df(main_hour_df)

# Membuat Header
st.header('Bike Sharing Dashboard')

# Informasi daily rental
st.subheader('Daily Rental')

col1, col2, col3 = st.columns(3)

with col1:
   registered_user = daily_registered_rent_df['Registered User'].sum()
   st.metric('Registered User', value = registered_user)

with col2:
   casual_user = daily_casual_rent_df['Casual User'].sum()
   st.metric('Casual User', value = casual_user)

with col3:
   total_user = daily_total_rent_df['Total User'].sum()
   st.metric('Total User', value = total_user)

# Monthly rental of all users
st.subheader('Monthly Rentals of All Users')
fig, ax = plt.subplots(figsize=(16,8))
ax.plot(
   daily_total_rent_df['Rental Date'].values,
   daily_total_rent_df['Total User'].values,
   marker='o',
   color='#90CAF9'
)
ax.tick_params(axis='y', labelsize=20)
ax.tick_params(axis='x', labelsize=15)
st.pyplot(fig)

# Monthly rental based on user type
st.subheader('Monthly Rental Based on Users Type')
fig, ax = plt.subplots(figsize=(16,8))
ax.plot(
   daily_registered_rent_df['Rental Date'].values,
   daily_registered_rent_df['Registered User'].values,
   marker='o',
   color='#90CAF9'
)
ax.plot(
   daily_casual_rent_df['Rental Date'].values,
   daily_casual_rent_df['Casual User'].values,
   marker='o',
   color='#D3D3D3'
)
ax.tick_params(axis='y', labelsize=20)
ax.tick_params(axis='x', labelsize=15)
st.pyplot(fig)

# Seasonly rental & weatherly rental
st.subheader('Number of User Based on Season & Weather')

col1, col2 = st.columns(2)

with col1:
   fig, ax = plt.subplots(figsize=(20,10))
   season_rent_df.plot(x='season', kind='bar', title='Seasonly Rental', rot=0, ax=ax)

   plt.xlabel(None)
   ax.tick_params(axis='y', labelsize=20)
   ax.tick_params(axis='x', labelsize=15)
   st.pyplot(fig)

with col2:
   fig, ax = plt.subplots(figsize=(20,10))
   weather_rent_df.plot(x='weathersit', kind='bar', title='Weatherly Rental', rot=0, ax=ax)

   plt.xlabel(None)
   ax.tick_params(axis='y', labelsize=20)
   ax.tick_params(axis='x', labelsize=15)
   st.pyplot(fig)

# Reantal based on holiday and workingday
st.subheader("Rental Based on Holiday and Workingday")

col1, col2 = st.columns(2)

with col1:
   fig, ax = plt.subplots(figsize=(20,10))
   holiday_rent_df.plot(x='holiday', kind='bar', title='Holiday Rental', rot=0, ax=ax)

   plt.xlabel(None)
   ax.tick_params(axis='y', labelsize=20)
   ax.tick_params(axis='x', labelsize=15)
   st.pyplot(fig)

with col2:
   fig, ax = plt.subplots(figsize=(20,10))
   workingday_rent_df.plot(x='workingday', kind='bar', title='Workingday Rental', rot=0, ax=ax)

   plt.xlabel(None)
   ax.tick_params(axis='y', labelsize=20)
   ax.tick_params(axis='x', labelsize=15)
   st.pyplot(fig)

# Rental hour
st.subheader('Hourly Rental Based on Users Type')
fig, ax = plt.subplots(figsize=(16,8))
ax.plot(
   hour_rent_df['Hour'].values,
   hour_rent_df['Registered User'].values,
   marker='o',
   color='#90CAF9'
)
ax.plot(
   hour_rent_df['Hour'].values,
   hour_rent_df['Casual User'].values,
   marker='o',
   color='#D3D3D3'
)
ax.tick_params(axis='y', labelsize=20)
ax.tick_params(axis='x', labelsize=15)
st.pyplot(fig)

st.caption('Copyright © Elba Faradisa 2023')