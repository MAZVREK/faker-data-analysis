import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(page_title='Faker Matches Data Analysis during International MSI 2022',
                    page_icon=':video_game:',
                    layout="wide"
)

df = pd.read_csv('data.csv')


st.sidebar.header('Choose your filters here:')

champion = st.sidebar.multiselect(
    "Select champion:",
    options=df['Champion'].unique(),
    default=df['Champion'].unique()
)

vs_champion = st.sidebar.multiselect(
    "Select Vs champion:",
    options=df['VsChampion'].unique(),
    default=df['VsChampion'].unique()
)


enemy = st.sidebar.multiselect(
    "Enemy team:",
    options=df['Vs'].unique(),
    default=df['Vs'].unique()
)

side = st.sidebar.multiselect(
    "Side:",
    options=df['Side'].unique(),
    default=df['Side'].unique()
)


df_filtered = df.query(
    "Champion == @champion & VsChampion == @vs_champion & Vs == @enemy & Side == @side"
)

st.title(':video_game: Faker Matches Data Analysis during International MSI 2022')
st.markdown('##')

total_matches = int(len(df_filtered))
average_kda = round(df_filtered['KDA'].mean(), 1)
average_minions = round(df_filtered['CS'].mean(), 1)
win_rate = round(df_filtered['W/L'].value_counts()['Win']/total_matches * 100, 1)
first_column, second_column, third_column, fourth_column = st.columns(4)

with first_column:
    st.subheader('Total matches:')
    st.subheader(f'{total_matches} :computer:')

with second_column:
    st.subheader('Average KDA:')
    st.subheader(f'{average_kda} :skull:')

with third_column:
    st.subheader('Average minions:')
    st.subheader(f'{average_minions} :ghost:')

with fourth_column:
    st.subheader('Average winrate:')
    st.subheader(f'{win_rate} :trophy:')

st.markdown('---')

st.dataframe(df_filtered)

# DELETES DEFAULT STREAMLIT FOOTER
st.markdown("""
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """, unsafe_allow_html=True)
