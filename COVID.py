import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objs as go
import streamlit as st
from plotly.subplots import make_subplots
import plotly.graph_objects as go


cov = pd.read_csv('country_vaccinations.csv')
temp = pd.read_csv('country_vaccinations.csv')[['country', 'date', 'daily_vaccinations']].dropna()
st.sidebar.title('Sidebar')
xiren_result = cov.country.unique()
selected_boxy = st.sidebar.selectbox(
    'Select one of the following:',
    ('Start', 'Automatic Line Chart', 'Analysis 1')    
)


if selected_boxy == 'Start':
    st.title('Covid-19 World Vaccination Progress')
    st.subheader('What is COVID-19?')
    st.image('OIP.jpg')
    st.markdown('COVID-19 is a new strain of coronavirus that has not been previously identified in humans. The COVID-19 is the cause of an outbreak of respiratory illness first detected in Wuhan, Hubei province, China')
    st.markdown('This deadly virus made a devastating effect on humanity and has killed over 5 mililion people from all around the world. Some are even children.')
    st.markdown('But we still have hope, a little below 7 billion people have taken the vaccine, to stop the virus from killing more people.')


if selected_boxy == 'Automatic Line Chart':
    st.title('Automatic Line Chart')
    def graph_generator(country):
        half_done = temp.loc[temp['country'] == country,['daily_vaccinations','date']]
        half_done['daily_vaccinations_cummulative'] = np.cumsum(half_done['daily_vaccinations'])
        return st.plotly_chart(px.line(half_done, x = 'date', y = 'daily_vaccinations_cummulative', title = 'Generated Line Graph'))
    noob = st.selectbox(
        'Select a country to produce a line chart of:',
        ('Afghanistan', 'Albania', 'Algeria', 'Andorra', 'Angola', 'Anguilla', 'Antigua and Barbuda', 'Argentina', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Bermuda', 'Bhutan', 'Bolivia', 'Brazil', 'Bulgaria', 'Cambodia', 'Canada', 'Cape Verde', 'Cayman Islands', 'Chile', 'China', 'Colombia', 'Costa Rica', "Cote d'Ivoire", 'Croatia', 'Cyprus', 'Czechia', 'Denmark', 'Dominica', 'Dominican Republic', 'Ecuador', 'Egypt', 'El Salvador', 'England', 'Equatorial Guinea', 'Estonia', 'Faeroe Islands', 'Falkland Islands', 'Finland', 'France', 'Gabon', 'Gambia', 'Georgia', 'Germany', 'Ghana', 'Gibraltar', 'Greece', 'Greenland', 'Grenada', 'Guatemala', 'Guernsey', 'Guinea', 'Guyana', 'Honduras', 'Hong Kong', 'Hungary', 'Iceland', 'India', 'Indonesia', 'Iran', 'Iraq', 'Ireland', 'Isle of Man', 'Israel', 'Italy', 'Jamaica', 'Japan', 'Jersey', 'Jordan', 'Kazakhstan', 'Kenya', 'Kuwait', 'Laos', 'Latvia', 'Lebanon', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'Macao', 'Malawi', 'Malaysia', 'Maldives', 'Malta', 'Mauritius', 'Mexico', 'Moldova', 'Monaco', 'Mongolia', 'Montenegro', 'Montserrat', 'Morocco', 'Mozambique', 'Myanmar', 'Namibia', 'Nepal', 'Netherlands', 'New Zealand', 'Nigeria', 'North Macedonia', 'Northern Cyprus', 'Northern Ireland', 'Norway', 'Oman', 'Pakistan', 'Palestine', 'Panama', 'Paraguay', 'Peru', 'Philippines', 'Poland', 'Portugal', 'Qatar', 'Romania', 'Russia', 'Rwanda', 'Saint Helena', 'Saint Kitts and Nevis', 'Saint Lucia', 'Saint Vincent and the Grenadines', 'San Marino', 'Sao Tome and Principe', 'Saudi Arabia', 'Scotland', 'Senegal', 'Serbia', 'Seychelles', 'Sierra Leone', 'Singapore', 'Slovakia', 'Slovenia', 'South Africa', 'South Korea', 'Spain', 'Sri Lanka', 'Suriname', 'Sweden', 'Switzerland', 'Taiwan', 'Thailand', 'Togo', 'Trinidad and Tobago', 'Tunisia', 'Turkey', 'Turks and Caicos Islands', 'Uganda', 'Ukraine', 'United Arab Emirates', 'United Kingdom', 'United States', 'Uruguay', 'Venezuela', 'Vietnam', 'Wales', 'Zimbabwe')
        )
    graph_generator(noob)
    st.markdown('Tip: enter full screen mode for better effects.')
    

if selected_boxy == 'Analysis 1':
    st.title('The First Analysis')
    st.markdown('I will do analysis on the column "daily_vaccinations".')
    st.plotly_chart(px.bar(cov, x = 'country', y = 'daily_vaccinations', hover_name = 'country', title = 'Bar plot of the daily vaccinations'))
    st.markdown('As you can see in this plot, the country with the most vaccinations is the United States, at that time.')
    st.markdown('The other countries that are above 1B are: China, England, India and the United Kingdom.')
    st.markdown('We can infer a lot of very interesting information of the countries from this graph.')
    if st.checkbox('Point 1'):
        st.markdown("If we use the full screen option with the Plotly graph, and zoom into the bottom stems of the bars, we can see that all of the countries' vaccination progress started little by little.")
        st.markdown('All of the countries started from at least 0.5 million jabs. But as the countries boost up their vaccination campaigns, some of the countries still continued at a very slow pace.')
    if st.checkbox('Point 2'):
        st.markdown('From this, we can see how the power of the countries can vary.')
        st.markdown("The countries that start slowly and doesn't speed up vaccinations, like the UAE, are typically small countries. For big countries like China and the US, the vaccination progress shoot up.")
        if st.checkbox("Don't mis-take things!"):
            st.subheader('Be careful!')
            st.markdown('We should look at the question in different ways. Maybe bigger countries like China has more population, and therefore the virus will spread faster. If the virus spreads faster, maybe we will need more vaccines.')
