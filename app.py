from matplotlib.pyplot import title
import streamlit as st
import pickle
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Dashboard", page_icon=":bar-chart:", layout="centered")

# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")   

st.title('Dashboard')

##-- Global Data, This is home data--##
world = st.sidebar.button('Global Data')
if world:
    global_total_case = pickle.load(open('pkl file/global/global_total_case.pkl','rb'))
    global_total_cure = pickle.load(open('pkl file/global/global_total_cure.pkl','rb'))
    global_total_death = pickle.load(open('pkl file/global/global_total_death.pkl','rb'))
    global_cured_rate = pickle.load(open('pkl file/global/global_cured_rate.pkl','rb'))
    global_death_rate = pickle.load(open('pkl file/global/global_death_rate.pkl','rb'))
    confirmed = global_total_case['Total Cases'].sum()
    cure = global_total_cure['Total Recovered'].sum()
    death = global_total_death['Total Deaths'].sum()
    active = confirmed - (cure+death)

    data = { 'Rate':[81.5,1.4,17.1]}     
    col1,col2,col3,col4 = st.columns(4)
    with col1:
        st.metric(label='Confirmed', value=confirmed)
    with col2:
        st.metric(label='Recovered', value=cure, delta='81.5%')
    with col3:
        st.metric(label='Active', value=confirmed, delta='1.4%')
    with col4:
        st.metric(label='Death', value=death, delta='17.11%')
    
    #--- Total cases---#

    col1,col2 = st.columns(2)
    with col1:
        #----Total cases----#
        fig = px.bar(global_total_case, y='Total Cases', x='Continents', text_auto='.2s',
            title="Continent wise cases")
        fig.update_traces(textfont_size=12, textangle=0, textposition="inside", cliponaxis=False)
        fig.update_layout(plot_bgcolor='black')
        fig.update_xaxes(showgrid=False)
        fig.update_yaxes(showgrid=False)
        st.plotly_chart(fig, use_container_width=True)
    with col2:
        #----Total case rate----#
        global_total_case_rate = pickle.load(open('pkl file/global/global_total_case_rate.pkl','rb'))    
        fig = px.bar(global_total_case_rate, y='rate', x='Continents', text_auto='.1s', title="Continent wise cases")
        fig.update_traces(textfont_size=12, textangle=0, textposition="inside", cliponaxis=False)
        fig.update_layout(plot_bgcolor='black')
        fig.update_xaxes(showgrid=False)
        fig.update_yaxes(showgrid=False)
        st.plotly_chart(fig, use_container_width=True)
    
    #---Cure data---#

    col1,col2 = st.columns(2)
    with col1:
        #----Total Cured Data----#
        fig = px.bar(global_total_cure, y='Total Recovered', x='Continents', text_auto='.1s', title="Continent wise cases")
        fig.update_traces(textfont_size=12, textangle=0, textposition="inside", cliponaxis=False)
        fig.update_layout(plot_bgcolor='black')
        fig.update_xaxes(showgrid=False)
        fig.update_yaxes(showgrid=False)
        st.plotly_chart(fig, use_container_width=True)
    with col2:
        #----Cured rate----#
        fig = px.bar(global_cured_rate, y='cure_rate', x='Continents', text_auto='.1s', title="Continent wise cases")
        fig.update_traces(textfont_size=12, textangle=0, textposition="inside", cliponaxis=False)
        fig.update_layout(plot_bgcolor='black')
        fig.update_xaxes(showgrid=False)
        fig.update_yaxes(showgrid=False)
        st.plotly_chart(fig, use_container_width=True)
    
    #---Death data---#

    col1,col2 = st.columns(2)
    with col1:
        #----Total death data---#
        fig = px.bar(global_total_death, y='Total Deaths', x='Continents', text_auto='.1s', title="Continent wise cases")
        fig.update_traces(textfont_size=12, textangle=0, textposition="inside", cliponaxis=False)
        fig.update_layout(plot_bgcolor='black')
        fig.update_xaxes(showgrid=False)
        fig.update_yaxes(showgrid=False)
        st.plotly_chart(fig, use_container_width=True)
    with col2:
        #----Death rate----#
        fig = px.bar(global_death_rate, y='death_rate', x='Continents', text_auto='.1s', title="Continent wise cases")
        fig.update_traces(textfont_size=12, textangle=0, textposition="inside", cliponaxis=False)
        fig.update_layout(plot_bgcolor='black')
        fig.update_xaxes(showgrid=False)
        fig.update_yaxes(showgrid=False)
        st.plotly_chart(fig, use_container_width=True)

#---- INDIA DATA----#
india = st.sidebar.button('India Data')
if india:
    month_wise_confirmed = pickle.load(open('pkl file/india/month_wise_confirmed.pkl','rb'))
    month_wise_cured = pickle.load(open('pkl file/india/month_wise_cured.pkl','rb'))
    month_wise_cured_rate = pickle.load(open('pkl file/india/month_wise_cured_rate.pkl','rb'))
    month_wise_death = pickle.load(open('pkl file/india/month_wise_death.pkl','rb'))
    month_wise_death_rate = pickle.load(open('pkl file/india/month_wise_death_rate.pkl','rb'))
    
    #-----Month wise confirmed data----#
    
    fig = px.line(month_wise_confirmed, x='Date', y='Confirmed', markers=True, title='Monyhly data on covid cases')
    fig.update_layout(plot_bgcolor='black')
    fig.update_xaxes(showgrid=False)
    fig.update_yaxes(showgrid=False)
    st.plotly_chart(fig, use_container_width=True)
        
    #-----Month wise cured data----#

    fig = px.line(month_wise_cured, x='Date', y='Cured', markers=True, title='Monthly Cured Data')
    fig.update_layout(plot_bgcolor='black')
    fig.update_xaxes(showgrid=False)
    fig.update_yaxes(showgrid=False)
    st.plotly_chart(fig, use_container_width=True)   

    #----Month wise cured rate data----#

    fig = px.line(month_wise_cured_rate, x='Date', y='cured_rate', markers=True, title='Monthly Cured Rate')
    fig.update_layout(plot_bgcolor='black')
    fig.update_xaxes(showgrid=False)
    fig.update_yaxes(showgrid=False)
    st.plotly_chart(fig, use_container_width=True) 

    #----Month wise death  data-----#

    fig = px.line(month_wise_death, x='Date', y='Deaths', markers=True, title='Monthly Death data')
    fig.update_layout(plot_bgcolor='black')
    fig.update_xaxes(showgrid=False)
    fig.update_yaxes(showgrid=False)
    st.plotly_chart(fig, use_container_width=True) 

    #----Month wise death rate data----#
    fig = px.line(month_wise_death_rate, x='Date', y='death_rate', markers=True, title='Monthly Death Rate')
    fig.update_layout(plot_bgcolor='black')
    fig.update_xaxes(showgrid=False)
    fig.update_yaxes(showgrid=False)
    st.plotly_chart(fig, use_container_width=True) 
   
#----STATE DATA----#

state = st.sidebar.button('State Data')
if state:
    state_confirmed = pickle.load(open('pkl file/state/state_confirmed.pkl','rb'))
    state_cured = pickle.load(open('pkl file/state/state_cured.pkl','rb'))
    state_cured_rate = pickle.load(open('pkl file/state/state_cured_rate.pkl','rb'))
    state_death = pickle.load(open('pkl file/state/state_death.pkl','rb'))
    state_death_rate = pickle.load(open('pkl file/state/state_death_rate.pkl','rb'))
    
    #----State Confirmed Data----#
    fig = px.bar(state_confirmed, x='State', y='Confirmed', title="State wise cases")
    fig.update_traces(textfont_size=12, textangle=0, textposition="inside", cliponaxis=False)
    fig.update_layout(plot_bgcolor='black')
    fig.update_xaxes(showgrid=False)
    fig.update_yaxes(showgrid=False)
    st.plotly_chart(fig, use_container_width=True)

    #-----State Cured Data----#
    fig = px.bar(state_cured, x='State', y='Cured', title="State Cured Data")
    fig.update_traces(textfont_size=12, textangle=0, textposition="inside", cliponaxis=False)
    fig.update_layout(plot_bgcolor='black')
    fig.update_xaxes(showgrid=False)
    fig.update_yaxes(showgrid=False)   
    st.plotly_chart(fig, use_container_width=True)

    #-----State Cured Rate Data----#
    fig = px.bar(state_cured_rate, x='State', y='Recovered Rate', title="State Recovered Rate ")
    fig.update_traces(textfont_size=12, textangle=0, textposition="inside", cliponaxis=False)
    fig.update_layout(plot_bgcolor='black')
    fig.update_xaxes(showgrid=False)
    fig.update_yaxes(showgrid=False)   
    st.plotly_chart(fig, use_container_width=True)    

    #----State Death Data----#
    fig = px.bar(state_death, x='State', y='Deaths', title="State Mortality data ")
    fig.update_traces(textfont_size=12, textangle=0, textposition="inside", cliponaxis=False)
    fig.update_layout(plot_bgcolor='black')
    fig.update_xaxes(showgrid=False)
    fig.update_yaxes(showgrid=False)   
    st.plotly_chart(fig, use_container_width=True)    
    
    #----State Death rate-----#
    fig = px.bar(state_death_rate, x='State', y='Mortality Rate', title="State Mortality Rate ")
    fig.update_traces(textfont_size=12, textangle=0, textposition="inside", cliponaxis=False)
    fig.update_layout(plot_bgcolor='black')
    fig.update_xaxes(showgrid=False)
    fig.update_yaxes(showgrid=False)   
    st.plotly_chart(fig, use_container_width=True)      

#-----UT Data-----#
ut = st.sidebar.button('UT Data')
if ut:
    #-----Loading DataFrames-----#

    ut_confirmed = pickle.load(open('pkl file/ut/ut_confirmed.pkl','rb'))
    ut_cured = pickle.load(open('pkl file/ut/ut_cured.pkl','rb'))
    ut_cured_rate = pickle.load(open('pkl file/ut/ut_cured_rate.pkl','rb'))
    ut_death = pickle.load(open('pkl file/ut/ut_death.pkl','rb'))
    ut_death_rate = pickle.load(open('pkl file/ut/ut_death_rate.pkl','rb'))
     
    #------UT Confirmed Cases  

    col1,col2 = st.columns(2)
    with col1:
        fig = px.bar(ut_confirmed, y='Confirmed', x='UT', text_auto='.1s', title="UT Confirmed Cases")
        fig.update_traces(textfont_size=12, textangle=0, textposition="inside", cliponaxis=False)
        fig.update_layout(plot_bgcolor='black')
        fig.update_xaxes(showgrid=False)
        fig.update_yaxes(showgrid=False)
        st.plotly_chart(fig, use_container_width=True)
    with col2:
        st.dataframe(ut_confirmed)
    
    #-----UT Cured Data-----#

    col1,col2 = st.columns(2)
    with col1:
        fig = px.bar(ut_cured, y='Cured', x='UT', text_auto='.1s', title="UT Cured Data")
        fig.update_traces(textfont_size=12, textangle=0, textposition="inside", cliponaxis=False)
        fig.update_layout(plot_bgcolor='black')
        fig.update_xaxes(showgrid=False)
        fig.update_yaxes(showgrid=False)
        st.plotly_chart(fig, use_container_width=True)
    with col2:
        st.dataframe(ut_cured)
    
    #-----UT Cured Rate-----#
    
    col1,col2 = st.columns(2)        
    with col1:
        fig = px.bar(ut_cured_rate, y='Recovered Rate', x='UT', text_auto='.1s', title="UT Recovered Data")
        fig.update_traces(textfont_size=12, textangle=0, textposition="inside", cliponaxis=False)
        fig.update_layout(plot_bgcolor='black')
        fig.update_xaxes(showgrid=False)
        fig.update_yaxes(showgrid=False)
        st.plotly_chart(fig, use_container_width=True)
    with col2:
        st.dataframe(ut_cured)    

    #-----UT Death Data-----#

    col1,col2 = st.columns(2)
    with col1:
        fig = px.bar(ut_death, y='Deaths', x='UT', text_auto='.1s', title="UT Death data")
        fig.update_traces(textfont_size=12, textangle=0, textposition="inside", cliponaxis=False)
        fig.update_layout(plot_bgcolor='black')
        fig.update_xaxes(showgrid=False)
        fig.update_yaxes(showgrid=False)
        st.plotly_chart(fig, use_container_width=True)
    with col2:
        st.dataframe(ut_death)  
    
    #-----UT Death Rate-----#

    col1,col2 = st.columns(2)
    with col1:
        fig = px.bar(ut_death_rate, y='Mortality Rate', x='UT', text_auto='.1s', title="UT Death Rate")
        fig.update_traces(textfont_size=12, textangle=0, textposition="inside", cliponaxis=False)
        fig.update_layout(plot_bgcolor='black')
        fig.update_xaxes(showgrid=False)
        fig.update_yaxes(showgrid=False)
        st.plotly_chart(fig, use_container_width=True)
    with col2:
        st.dataframe(ut_death_rate)  

#-----Top10 Data-----#

top10 = st.sidebar.button('Trending Data')
if top10:
    #------Loading Data-----#

    top10_state_confirmed = pickle.load(open('pkl file/top10/top10_state_confirmed.pkl','rb'))
    top10_cured_state = pickle.load(open('pkl file/top10/top10_cured_state.pkl','rb'))
    top10_cured_rate = pickle.load(open('pkl file/top10/top10_cured_rate.pkl','rb'))
    top10_noncured_rate = pickle.load(open('pkl file/top10/top10_noncured_rate.pkl','rb'))
    top10_death_state = pickle.load(open('pkl file/top10/top10_death_state.pkl','rb'))
    top10_death_rate = pickle.load(open('pkl file/top10/top10_death_rate.pkl','rb'))
    
    #-----Top10 State Confirmed-----#
    col1,col2 = st.columns(2)
    with col1:
        fig = px.bar(top10_state_confirmed, y='Confirmed', x='State', text_auto='.1s', title="Top-10 State Of COVID Cases")
        fig.update_traces(textfont_size=12, textangle=0, textposition="inside", cliponaxis=False)
        fig.update_layout(plot_bgcolor='black')
        fig.update_xaxes(showgrid=False)
        fig.update_yaxes(showgrid=False)
        st.plotly_chart(fig, use_container_width=True)
    with col2:
        st.dataframe(top10_state_confirmed)
    
    #-----Top10 Cured State----#
    col1,col2 = st.columns(2)
    with col1:
        fig = px.bar(top10_cured_state, y='Cured', x='State', text_auto='.1s', title='Top-10 Recovered States')
        fig.update_traces(textfont_size=12, textangle=0, textposition="inside", cliponaxis=False)
        fig.update_layout(plot_bgcolor='black')
        fig.update_xaxes(showgrid=False)
        fig.update_yaxes(showgrid=False)
        st.plotly_chart(fig, use_container_width=True)
    with col2:
        st.dataframe(top10_cured_state)

    #----Top10 High Recovered Rtae State----#
    col1,col2 = st.columns(2)
    with col1:
        fig = px.bar(top10_cured_rate, y='Recovered Rate', x='State', text_auto='.1s', title='Top-10 High Recovered Rate States')
        fig.update_traces(textfont_size=12, textangle=0, textposition="inside", cliponaxis=False)
        fig.update_layout(plot_bgcolor='black')
        fig.update_xaxes(showgrid=False)
        fig.update_yaxes(showgrid=False)
        st.plotly_chart(fig, use_container_width=True)
    with col2:
        st.dataframe(top10_cured_rate)

    #-----Top10 Low Recovered Rate State-----#
    col1,col2 = st.columns(2)
    with col1:
        fig = px.bar(top10_noncured_rate, y='Cured Rate', x='State', text_auto='.1s', title='Top-10 Low Recovered Rate States')
        fig.update_traces(textfont_size=12, textangle=0, textposition="inside", cliponaxis=False)
        fig.update_layout(plot_bgcolor='black')
        fig.update_xaxes(showgrid=False)
        fig.update_yaxes(showgrid=False)
        st.plotly_chart(fig, use_container_width=True)
    with col2:
        st.dataframe(top10_noncured_rate)

    #-----Top10 High no of Deaths State----#
    col1,col2 = st.columns(2)
    with col1:
        fig = px.bar(top10_death_state, y='Deaths', x='State', text_auto='.1s', title='Top-10 High No. of Death States')
        fig.update_traces(textfont_size=12, textangle=0, textposition="inside", cliponaxis=False)
        fig.update_layout(plot_bgcolor='black')
        fig.update_xaxes(showgrid=False)
        fig.update_yaxes(showgrid=False)
        st.plotly_chart(fig, use_container_width=True)
    with col2:
        st.dataframe(top10_death_state)    

    #-----Top10 High Mortality Rate-----#
    col1,col2 = st.columns(2)
    with col1:
        fig = px.bar(top10_death_rate, y='Mortality Rate', x='State', text_auto='.1s', title='Top-10 High Mortality Rate States')
        fig.update_traces(textfont_size=12, textangle=0, textposition="inside", cliponaxis=False)
        fig.update_layout(plot_bgcolor='black')
        fig.update_xaxes(showgrid=False)
        fig.update_yaxes(showgrid=False)
        st.plotly_chart(fig, use_container_width=True)
    with col2:
        st.dataframe(top10_death_rate)    