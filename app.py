import streamlit as st
import pandas as pd
from help import fetch_medal_tally
from preprocessing import preprocess
import streamlit as st
from streamlit_folium import folium_static
import folium
st.set_page_config(layout='wide')
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.figure_factory as ff
import numpy as np
import plotly.graph_objects as go
"Data Analysis of Olympics Data"

maps = pd.read_csv("map.csv")
df = pd.read_csv("athlete_events.csv")
region_df = pd.read_csv("noc_regions.csv")

df = preprocess(df,region_df)
#print(df.columns)
#print(df.shape)
#medal_tally = pd.concat([df,pd.get_dummies(df['Medal'])],axis=1)
menu = st.radio('Select an option:', ['Medal Tally','Overall Analysis','Countrywise Analysis', 'Athletewise Analysis','Medal Tally Plot'])


if menu == 'Medal Tally':
    st.header("Medal Tally")
    #years,country = helper.country_year_list(df)
    years = ['overall',1896,
             1900,
             1904,
             1908,
             1906,
             1912,
             1920,
             1924,
             1928,
             1932,
             1936,
             1948,
             1952,
             1956,
             1960,
             1964,
             1968,
             1972,
             1976,
             1980,
             1984,
             1988,
             1992,
             1996,
             2000,
             2004,
             2008,
             2012,
             2016]
    country = ['overall','Afghanistan', 'Albania', 'Algeria', 'American Samoa', 'Andorra',
       'Angola', 'Antigua', 'Argentina', 'Armenia', 'Aruba', 'Australia',
       'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain', 'Bangladesh',
       'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin', 'Bermuda',
       'Bhutan', 'Boliva', 'Bosnia and Herzegovina', 'Botswana', 'Brazil',
       'Brunei', 'Bulgaria', 'Burkina Faso', 'Burundi', 'Cambodia',
       'Cameroon', 'Canada', 'Cape Verde', 'Cayman Islands',
       'Central African Republic', 'Chad', 'Chile', 'China', 'Colombia',
       'Comoros', 'Cook Islands', 'Costa Rica', 'Croatia', 'Cuba',
       'Curacao', 'Cyprus', 'Czech Republic',
       'Democratic Republic of the Congo', 'Denmark', 'Djibouti',
       'Dominica', 'Dominican Republic', 'Ecuador', 'Egypt',
       'El Salvador', 'Equatorial Guinea', 'Eritrea', 'Estonia',
       'Ethiopia', 'Fiji', 'Finland', 'France', 'Gabon', 'Gambia',
       'Georgia', 'Germany', 'Ghana', 'Greece', 'Grenada', 'Guam',
       'Guatemala', 'Guinea', 'Guinea-Bissau', 'Guyana', 'Haiti',
       'Honduras', 'Hungary', 'Iceland', 'India',
       'Individual Olympic Athletes', 'Indonesia', 'Iran', 'Iraq',
       'Ireland', 'Israel', 'Italy', 'Ivory Coast', 'Jamaica', 'Japan',
       'Jordan', 'Kazakhstan', 'Kenya', 'Kiribati', 'Kosovo', 'Kuwait',
       'Kyrgyzstan', 'Laos', 'Latvia', 'Lebanon', 'Lesotho', 'Liberia',
       'Libya', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'Macedonia',
       'Madagascar', 'Malawi', 'Malaysia', 'Maldives', 'Mali', 'Malta',
       'Marshall Islands', 'Mauritania', 'Mauritius', 'Mexico',
       'Micronesia', 'Moldova', 'Monaco', 'Mongolia', 'Montenegro',
       'Morocco', 'Mozambique', 'Myanmar', 'Namibia', 'Nauru', 'Nepal',
       'Netherlands', 'New Zealand', 'Nicaragua', 'Niger', 'Nigeria',
       'North Korea', 'Norway', 'Oman', 'Pakistan', 'Palau', 'Palestine',
       'Panama', 'Papua New Guinea', 'Paraguay', 'Peru', 'Philippines',
       'Poland', 'Portugal', 'Puerto Rico', 'Qatar', 'Republic of Congo',
       'Romania', 'Russia', 'Rwanda', 'Saint Kitts', 'Saint Lucia',
       'Saint Vincent', 'Samoa', 'San Marino', 'Sao Tome and Principe',
       'Saudi Arabia', 'Senegal', 'Serbia', 'Seychelles', 'Sierra Leone',
       'Slovakia', 'Slovenia', 'Solomon Islands', 'Somalia',
       'South Africa', 'South Korea', 'South Sudan', 'Spain', 'Sri Lanka',
       'Sudan', 'Suriname', 'Swaziland', 'Sweden', 'Switzerland', 'Syria',
       'Taiwan', 'Tajikistan', 'Tanzania', 'Thailand', 'Timor-Leste',
       'Togo', 'Tonga', 'Trinidad', 'Tunisia', 'Turkey', 'Turkmenistan',
       'UK', 'USA', 'Uganda', 'Ukraine', 'United Arab Emirates',
       'Uruguay', 'Uzbekistan', 'Vanuatu', 'Venezuela', 'Vietnam',
       'Virgin Islands, British', 'Virgin Islands, US', 'Yemen', 'Zambia',
       'Zimbabwe']
    selected_year = st.selectbox("Select Year",years)
    selected_country = st.selectbox("Select Country", country)
    ans=fetch_medal_tally(df, selected_year, selected_country)
    st.table(ans)
elif menu == 'Overall Analysis':
    map = folium.Map(location=[maps.latitude.mean(), maps.longitude.mean()],
            zoom_start=1, control_scale=True)
    for index, location_info in maps.iterrows():
        folium.Marker([location_info["latitude"], location_info["longitude"]], popup=location_info["City"]).add_to(map)
    editions = len(df.Year.unique())
    cities = len(df.City.unique())
    sports = len(df.Sport.unique())
    events = len(df.Event.unique())
    athletes = len(df.Name.unique())
    nations = len(df.region.unique())
    st.title("Top Statistics")
    col1, col2,col3,col4 = st.columns([4, 1,1,1])
    with col1:
        st.header("Cities that has hosted Olympics")
        folium_static(map)
    with col2:
        st.header("Hosts")
        st.title(cities)
    with col3:
        st.header("Sports")
        st.title(sports)
    with col4:
        st.header("Editions")
        st.title(editions)
    col1, col2, col3 = st.columns(3)
    with col1:
        st.header("Events")
        st.title(events)
    with col2:
        st.header("Nations")
        st.title(nations)
    with col3:
        st.header("Athletes")
        st.title(athletes)
    col3,col4 = st.columns(2)

elif menu == 'Countrywise Analysis':
    country = ['Afghanistan', 'Albania', 'Algeria', 'American Samoa', 'Andorra',
               'Angola', 'Antigua', 'Argentina', 'Armenia', 'Aruba', 'Australia',
               'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain', 'Bangladesh',
               'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin', 'Bermuda',
               'Bhutan', 'Boliva', 'Bosnia and Herzegovina', 'Botswana', 'Brazil',
               'Brunei', 'Bulgaria', 'Burkina Faso', 'Burundi', 'Cambodia',
               'Cameroon', 'Canada', 'Cape Verde', 'Cayman Islands',
               'Central African Republic', 'Chad', 'Chile', 'China', 'Colombia',
               'Comoros', 'Cook Islands', 'Costa Rica', 'Croatia', 'Cuba',
               'Curacao', 'Cyprus', 'Czech Republic',
               'Democratic Republic of the Congo', 'Denmark', 'Djibouti',
               'Dominica', 'Dominican Republic', 'Ecuador', 'Egypt',
               'El Salvador', 'Equatorial Guinea', 'Eritrea', 'Estonia',
               'Ethiopia', 'Fiji', 'Finland', 'France', 'Gabon', 'Gambia',
               'Georgia', 'Germany', 'Ghana', 'Greece', 'Grenada', 'Guam',
               'Guatemala', 'Guinea', 'Guinea-Bissau', 'Guyana', 'Haiti',
               'Honduras', 'Hungary', 'Iceland', 'India',
               'Individual Olympic Athletes', 'Indonesia', 'Iran', 'Iraq',
               'Ireland', 'Israel', 'Italy', 'Ivory Coast', 'Jamaica', 'Japan',
               'Jordan', 'Kazakhstan', 'Kenya', 'Kiribati', 'Kosovo', 'Kuwait',
               'Kyrgyzstan', 'Laos', 'Latvia', 'Lebanon', 'Lesotho', 'Liberia',
               'Libya', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'Macedonia',
               'Madagascar', 'Malawi', 'Malaysia', 'Maldives', 'Mali', 'Malta',
               'Marshall Islands', 'Mauritania', 'Mauritius', 'Mexico',
               'Micronesia', 'Moldova', 'Monaco', 'Mongolia', 'Montenegro',
               'Morocco', 'Mozambique', 'Myanmar', 'Namibia', 'Nauru', 'Nepal',
               'Netherlands', 'New Zealand', 'Nicaragua', 'Niger', 'Nigeria',
               'North Korea', 'Norway', 'Oman', 'Pakistan', 'Palau', 'Palestine',
               'Panama', 'Papua New Guinea', 'Paraguay', 'Peru', 'Philippines',
               'Poland', 'Portugal', 'Puerto Rico', 'Qatar', 'Republic of Congo',
               'Romania', 'Russia', 'Rwanda', 'Saint Kitts', 'Saint Lucia',
               'Saint Vincent', 'Samoa', 'San Marino', 'Sao Tome and Principe',
               'Saudi Arabia', 'Senegal', 'Serbia', 'Seychelles', 'Sierra Leone',
               'Slovakia', 'Slovenia', 'Solomon Islands', 'Somalia',
               'South Africa', 'South Korea', 'South Sudan', 'Spain', 'Sri Lanka',
               'Sudan', 'Suriname', 'Swaziland', 'Sweden', 'Switzerland', 'Syria',
               'Taiwan', 'Tajikistan', 'Tanzania', 'Thailand', 'Timor-Leste',
               'Togo', 'Tonga', 'Trinidad', 'Tunisia', 'Turkey', 'Turkmenistan',
               'UK', 'USA', 'Uganda', 'Ukraine', 'United Arab Emirates',
               'Uruguay', 'Uzbekistan', 'Vanuatu', 'Venezuela', 'Vietnam',
               'Virgin Islands, British', 'Virgin Islands, US', 'Yemen', 'Zambia',
               'Zimbabwe']
    selected_country = st.selectbox("Select Country", country)
    st.title("Medal over the years of " + selected_country)
    df.dropna(subset=['Medal'], inplace=True)
    temp_df = df[df['region'] == selected_country]
    temp_df.drop_duplicates(subset=['Team', 'NOC', 'Games', 'Year', 'City', 'Sport', 'Event', 'Medal'], inplace=True)
    dff = temp_df.groupby('Year').count()['Medal']
    dff = dff.to_frame().reset_index()
    fig = px.line(dff, x="Year", y="Medal")
    st.plotly_chart(fig)
    st.title(selected_country + " excels in the following sports")
    fig1, ax = plt.subplots(figsize=(20, 20))
    pt = temp_df.pivot_table(index='Sport', columns='Year', values='Medal', aggfunc='count').fillna(0)
    ax = sns.heatmap(pt, annot=True)
    st.pyplot(fig1)
    st.title("Top 10 athletes of " + selected_country)
    x = temp_df['Name'].value_counts().reset_index().head(10).merge(df, left_on='index', right_on='Name', how='left')[
        ['index', 'Name_x', 'Sport']].drop_duplicates('index')
    x.rename(columns={'index': 'Name', 'Name_x': 'Medals'}, inplace=True)
    #print(x)
    st.table(x)
elif menu == 'Athletewise Analysis':
    temp_df_m=df[df['Sex']=='M']
    temp_df_f = df[df['Sex'] == 'F']
    temp_df_f=temp_df_f[["Sex","Year"]]
    temp_df_m = temp_df_m[["Sex", "Year"]]
    df_gender_m=temp_df_m.groupby(['Year']).count().sort_values('Year',ascending=True).reset_index()
    df_gender_f=temp_df_f.groupby(['Year']).count().sort_values('Year',ascending=True).reset_index()
    final = df_gender_m.merge(df_gender_f, on='Year', how='left')
    final.fillna(0, inplace=True)
    final.rename(columns={'Sex_x': 'Male', 'Sex_y': 'Female'}, inplace=True)
    figs = px.line(final, x="Year", y=["Male", "Female"])
    figs.update_layout(autosize=False, width=1000, height=600)
    st.title("Participation Of Men And Women Over The Years")
    st.plotly_chart(figs)
    df.dropna(subset=['Age'],inplace=True)
    athlete = df.drop_duplicates(subset=["Name", "region"])
    st1 = athlete['Age']
    st2 =athlete[athlete["Medal"]=="Gold"]["Age"]
    st3 = athlete[athlete["Medal"]=="Silver"]["Age"]
    st4 = athlete[athlete["Medal"]=="Bronze"]["Age"]
    figg = ff.create_distplot([st1,st2,st3,st4], ["Overall Age Distribution","Gold Medal Age distribution","Silver Medal Age distribution","Bronze Medal Age distribution"], show_hist=False, show_rug=False)
    figg.update_layout(autosize=False, width=1000, height=600)
    st.title("Distribution of Age")
    #figg= plt.plotly_chart(figsize=(20, 20))
    st.plotly_chart(figg)
    athlete = df.drop_duplicates(subset=["Name", "region"])
    x = []
    name = []
    famous_sports = ['Basketball', 'Judo', 'Football', 'Tug-Of-War', 'Athletics',
                     'Swimming', 'Badminton', 'Sailing', 'Gymnastics',
                     'Art Competitions', 'Handball', 'Weightlifting', 'Wrestling',
                     'Water Polo', 'Hockey', 'Rowing', 'Fencing',
                     'Shooting', 'Boxing', 'Taekwondo', 'Cycling', 'Diving', 'Canoeing',
                     'Tennis', 'Golf', 'Softball', 'Archery',
                     'Volleyball', 'Synchronized Swimming', 'Table Tennis', 'Baseball',
                     'Rhythmic Gymnastics', 'Rugby Sevens',
                     'Beach Volleyball', 'Triathlon', 'Rugby', 'Polo', 'Ice Hockey']
    for sport in famous_sports:
        temp_df = athlete[athlete['Sport'] == sport]
        x.append(temp_df[temp_df['Medal'] == 'Gold']['Age'].dropna())
        name.append(sport)
    fi=ff.create_distplot(x, name, show_hist=False, show_rug=False)
    fi.update_layout(autosize=False, width=1500, height=800)
    st.title("Distribution of Age For Various Sports")
    st.plotly_chart(fi)
    st.title('Height Vs Weight')
    sport_list=athlete["Sport"].unique()
    sport_list.tolist()
    selected_sport = st.selectbox('Select a Sport', sport_list)
    #athlete_df = df.drop_duplicates(subset=['Name', 'region'])
    athlete['Medal'].fillna('No Medal', inplace=True)
    temp_df = athlete[athlete['Sport'] == selected_sport]
    figss, ax1 = plt.subplots()
    figss,ax1 = plt.subplots()
    ax1 = sns.scatterplot(temp_df['Weight'],temp_df['Height'],hue=temp_df['Medal'],style=temp_df['Sex'],s=40)
    st.pyplot(figss)
elif menu == 'Medal Tally Plot':
    st.header("Medal Tally Plot")
    #years,country = helper.country_year_list(df)
    years = [1896,
             1900,
             1904,
             1908,
             1906,
             1912,
             1920,
             1924,
             1928,
             1932,
             1936,
             1948,
             1952,
             1956,
             1960,
             1964,
             1968,
             1972,
             1976,
             1980,
             1984,
             1988,
             1992,
             1996,
             2000,
             2004,
             2008,
             2012,
             2016]
    country = ['Afghanistan', 'Albania', 'Algeria', 'American Samoa', 'Andorra',
       'Angola', 'Antigua', 'Argentina', 'Armenia', 'Aruba', 'Australia',
       'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain', 'Bangladesh',
       'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin', 'Bermuda',
       'Bhutan', 'Boliva', 'Bosnia and Herzegovina', 'Botswana', 'Brazil',
       'Brunei', 'Bulgaria', 'Burkina Faso', 'Burundi', 'Cambodia',
       'Cameroon', 'Canada', 'Cape Verde', 'Cayman Islands',
       'Central African Republic', 'Chad', 'Chile', 'China', 'Colombia',
       'Comoros', 'Cook Islands', 'Costa Rica', 'Croatia', 'Cuba',
       'Curacao', 'Cyprus', 'Czech Republic',
       'Democratic Republic of the Congo', 'Denmark', 'Djibouti',
       'Dominica', 'Dominican Republic', 'Ecuador', 'Egypt',
       'El Salvador', 'Equatorial Guinea', 'Eritrea', 'Estonia',
       'Ethiopia', 'Fiji', 'Finland', 'France', 'Gabon', 'Gambia',
       'Georgia', 'Germany', 'Ghana', 'Greece', 'Grenada', 'Guam',
       'Guatemala', 'Guinea', 'Guinea-Bissau', 'Guyana', 'Haiti',
       'Honduras', 'Hungary', 'Iceland', 'India',
       'Individual Olympic Athletes', 'Indonesia', 'Iran', 'Iraq',
       'Ireland', 'Israel', 'Italy', 'Ivory Coast', 'Jamaica', 'Japan',
       'Jordan', 'Kazakhstan', 'Kenya', 'Kiribati', 'Kosovo', 'Kuwait',
       'Kyrgyzstan', 'Laos', 'Latvia', 'Lebanon', 'Lesotho', 'Liberia',
       'Libya', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'Macedonia',
       'Madagascar', 'Malawi', 'Malaysia', 'Maldives', 'Mali', 'Malta',
       'Marshall Islands', 'Mauritania', 'Mauritius', 'Mexico',
       'Micronesia', 'Moldova', 'Monaco', 'Mongolia', 'Montenegro',
       'Morocco', 'Mozambique', 'Myanmar', 'Namibia', 'Nauru', 'Nepal',
       'Netherlands', 'New Zealand', 'Nicaragua', 'Niger', 'Nigeria',
       'North Korea', 'Norway', 'Oman', 'Pakistan', 'Palau', 'Palestine',
       'Panama', 'Papua New Guinea', 'Paraguay', 'Peru', 'Philippines',
       'Poland', 'Portugal', 'Puerto Rico', 'Qatar', 'Republic of Congo',
       'Romania', 'Russia', 'Rwanda', 'Saint Kitts', 'Saint Lucia',
       'Saint Vincent', 'Samoa', 'San Marino', 'Sao Tome and Principe',
       'Saudi Arabia', 'Senegal', 'Serbia', 'Seychelles', 'Sierra Leone',
       'Slovakia', 'Slovenia', 'Solomon Islands', 'Somalia',
       'South Africa', 'South Korea', 'South Sudan', 'Spain', 'Sri Lanka',
       'Sudan', 'Suriname', 'Swaziland', 'Sweden', 'Switzerland', 'Syria',
       'Taiwan', 'Tajikistan', 'Tanzania', 'Thailand', 'Timor-Leste',
       'Togo', 'Tonga', 'Trinidad', 'Tunisia', 'Turkey', 'Turkmenistan',
       'UK', 'USA', 'Uganda', 'Ukraine', 'United Arab Emirates',
       'Uruguay', 'Uzbekistan', 'Vanuatu', 'Venezuela', 'Vietnam',
       'Virgin Islands, British', 'Virgin Islands, US', 'Yemen', 'Zambia',
       'Zimbabwe']
    selected_year = st.selectbox("Select Year",years)
    selected_country = st.selectbox("Select Country", country)
    ans=fetch_medal_tally(df, selected_year, selected_country)
    ans.fillna(0)
    g = np.array(ans.Gold)
    s = np.array(ans.Silver)
    b = np.array(ans.Bronze)
    #print(len(g))
    #print(s)
    #print(b)
    if len(g)== 0 or len(s)==0 or len(b) == 0:
        print("Loading Data")
    else:
        st.title("Medal Distribution for " + selected_country + " in " + str(selected_year) )
        y=[]
        y.append(int(g))
        y.append(int(s))
        y.append(int(b))
        x=["Gold","Silver","Bronze"]
        #print(x)
        #print(y)
        fig22 = go.Figure([go.Bar(x=x, y=y)])
        st.plotly_chart(fig22)

