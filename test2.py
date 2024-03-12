import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import seaborn as sns
from datetime import datetime, timedelta
import time

import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

##====================================================================================##
df = pd.read_csv('../dff_season_240229.csv')
df_winter = df[df['season'] == 3]

#####
fig3 = plt.figure(figsize = (20, 8))
sns.set_style('darkgrid')

sns.boxplot(y='activity', x='hour', data=df_winter, \
            palette = 'Spectral' ,linewidth = 3,width = 0.8\
            #hue='area'/ Spectral
            )

anomaly_df = df[df['date'].isin(['2024-02-04'])]
sns.lineplot(
    data=anomaly_df, x='hour', y='activity',
    label='2024-02-04', marker="o", linewidth=0.5,
    color='red', alpha=1
)

plt.title('Activity_NewSpring', size = 15)
plt.xticks(range(24))
plt.ylim(0,0.025)

plt.legend(loc='upper left', fontsize= 12)

#####

tab1, tab2 = st.tabs(["📈 Chart", "🗃 Data"])

with tab1:
    st.header("A tab with a chart")
    st.pyplot(fig3)

##====================================================================================##

with tab2:
    st.header("A tab2")
    col1, col2 = st.columns([3, 1])

    fig2 = plt.figure(figsize = (20, 8))
    sns.set_style('darkgrid')

    sns.boxplot(y='activity', x='hour', data=df_winter, \
                palette = 'Spectral' ,linewidth = 3,width = 0.8\
                #hue='area'/ Spectral
                )

    anomaly_df = df[df['date'].isin(['2024-02-04'])]
    sns.lineplot(
        data=anomaly_df, x='hour', y='activity',
        label='2024-02-04', marker="o", linewidth=0.5,
        color='red', alpha=1
    )

    plt.title('Activity_NewSpring', size = 15)
    plt.xticks(range(24))
    plt.ylim(0,0.025)

    plt.legend(loc='upper left', fontsize= 12)

    col1.title("Col1")
    col1.pyplot(fig2)

    ##====================================================================================##

    fig =go.Figure(go.Sunburst(
    ids=[
        "2동", "3동", "4동", "5동",
        "1106", "1065", "1062", "1102", "1089", "2048", "1077", "2005",
        "0079", "1098", "1086", "1075", "1032", "1069",
        "3007", "3003", "2084", "2085", "2045", "2061", "2099", "2028", "2063",
        "2032", "2056", "2023", "2067", "2066", "2050",
        "3043", "3052", "3048", "3053", "3057", "3045", "3058", "3059", "3056", "3055",
        "7071", "7099", "9102", "8040", "9023"
    ],
    labels= [
        "2동", "3동", "4동", "5동",
        "1106", "1065", "1062", "1102", "1089", "2048", "1077", "2005",
        "0079", "1098", "1086", "1075", "1032", "1069", #14
        "3007", "3003", "2084", "2085", "2045", "2061", "2099", "2028", "2063",
        "2032", "2056", "2023", "2067", "2066", "2050", #15
        "3043", "3052", "3048", "3053", "3057", "3045", "3058", "3059", "3056", "3055", #10
        "7071", "7099", "9102", "8040", "9023" #5
    ],
    parents=[
        "", "", "", "", 
        "2동","2동","2동","2동","2동","2동","2동","2동","2동","2동","2동","2동","2동","2동",
        "3동","3동","3동","3동","3동","3동","3동","3동","3동","3동","3동","3동","3동","3동","3동",
        "4동","4동","4동","4동","4동","4동","4동","4동","4동","4동",
        "5동","5동","5동","5동","5동"
    ],
    ))
    fig.update_layout(margin = dict(t=0, l=0, r=0, b=0))


    col2.subheader("Streamlit Tutorial")
    col2.plotly_chart(fig)