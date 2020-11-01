import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
import us
from covid_plot_function import plotly_covid_rate
st.set_option('deprecation.showPyplotGlobalUse', False)


snap = pd.read_csv('two_month_snapshot.csv', index_col=0)
mask = pd.read_csv('sme.csv')

#st.dataframe(snap.head())
state_list = ['Alabama',
 'Alaska',
 'Arizona',
 'Arkansas',
 'California',
 'Colorado',
 'Connecticut',
 'Delaware',
 'Florida',
 'Georgia',
 'Hawaii',
 'Idaho',
 'Illinois',
 'Indiana',
 'Iowa',
 'Kansas',
 'Kentucky',
 'Louisiana',
 'Maine',
 'Maryland',
 'Massachusetts',
 'Michigan',
 'Minnesota',
 'Mississippi',
 'Missouri',
 'Montana',
 'Nebraska',
 'Nevada',
 'New Hampshire',
 'New Jersey',
 'New Mexico',
 'New York',
 'North Carolina',
 'North Dakota',
 'Ohio',
 'Oklahoma',
 'Oregon',
 'Pennsylvania',
 'Rhode Island',
 'South Carolina',
 'South Dakota',
 'Tennessee',
 'Texas',
 'Utah',
 'Vermont',
 'Virginia',
 'Washington',
 'West Virginia',
 'Wisconsin',
 'Wyoming']


descriptors = ['an awesome place to live!', 'a pretty cool state!', 'very boring...', 'a very fun state to visit!']

st.title('Plot COVID-19 Rates by State.')
st.subheader('This app helps visualize COVID-19 case rates for any number of states between July 1st, 2020 and September 1st, 2020. The time frame is informed by the NY Times mask usage survey issued in early July. For more information on the survey or this project, please visit the links below.')

st.markdown("[New York Times](https://github.com/nytimes/covid-19-data/tree/master/mask-use)")
st.markdown("[Decoding COVID-19: Alex Fioto, Vivian Nguyen, Varun Mohan](https://github.com/ga-dsir824-collab/project-5)")
num_states = st.text_input('How many states do you want to plot?')

successes = ['That is my favorite number!', 'That is my lucky number!', 
             f'AI will take over the world in {num_states} years', 
             'That\'s how old my dog is!', 'That\'s how many cats I have!', 
             f'Nice choice!', f'{num_states}? Really?', f'{num_states} little monkey\'s jumping on the bed.'
              ]

if not num_states:
    st.warning('Can I get your number?')
    st.stop()
st.success(np.random.choice(successes))

states = []

for i in range(1, int(num_states) +1):
    state = st.text_input(f'Enter state {i}')
    if not state:
        st.warning('Please input a state')
        st.stop()
    if state not in state_list:
        st.warning('Please check spelling, remember to capitalize, and remember to eat your vegetables!')
        st.stop()
    states.append(state)
    st.success(f'{state} is {np.random.choice(descriptors)}')

mapper = us.states.mapping('name', 'abbr')

new_df = pd.DataFrame()
for state in states:
    df = mask[mask['STATE'] == mapper.get(state)]
    new_df = pd.concat([new_df, df])
    
new_df = new_df[['STATE', 'mask_negative', 'mask_positive', 'NEVER', 'RARELY', 'SOMETIMES', 'FREQUENTLY', 'ALWAYS']]

#st.subheader('If you check the box below the dataframe displays the proportions of each chosen state\'s mask survey results.')
see_data = st.checkbox('Click for New York Times Mask data')
if see_data:
    st.dataframe(new_df)


figure = plotly_covid_rate(states)

figure