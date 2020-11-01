import streamlit as st
import pandas as pd
import plotly.express as px

st.set_option('deprecation.showPyplotGlobalUse', False)

snap = pd.read_csv('two_month_snapshot.csv', index_col=0)

@st.cache(allow_output_mutation=True)
def plotly_covid_rate(states=['North Carolina']):
    state_dictionary = {}
    title_string = 'COVID-19 Cases for '
    for state in states:
        state_df = snap[snap['state'] == state]
        state_df['date'] = pd.to_datetime(state_df['date'])
        state_df.set_index('date', inplace=True)
        state_dictionary[state] = state_df['zeroed_cases']
        title_string += state + ' '
    fig = px.line(title='COVID-19 Cases: July 1 - September 1')
    for state, series in state_dictionary.items():
        fig.add_scatter(x=state_df.index, y = series, name=state)
    fig.update_layout(xaxis_title='Date', yaxis_title='Cases')
    return fig