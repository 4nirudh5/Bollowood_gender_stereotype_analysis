import streamlit as st
import pickle
import pandas as pd
import numpy as np
from streamlit_option_menu import option_menu

selected = option_menu(
    menu_title = None,
    options = ["Male Centrality","Female Centrality","About"], 
    icons = ["person","person","house"], 
    menu_icon = "menu-button", 
    orientation = "horizontal",
)

if selected == "Male Centrality":
    st.title('Predict your Centrality')
    st.subheader('Enter the details')
    model = pickle.load(open('male.sav','rb'))
    
    def mcm(input_data):
        na = np.asarray(input_data)
        d = na.reshape(1,-1)
        
        prediction = model.predict(d)
        return prediction


    def main():

        MENTIONS1 = st.text_input('MENTIONS')
        TOTAL_CENTRALITY1 = st.text_input('TOTAL_CENTRALITY')
        COUNT1 = st.text_input('COUNT')

          

        male_mention_centrality = ''
        if st.button('Get Centrality'):
           male_mention_centrality  = mcm([MENTIONS1,TOTAL_CENTRALITY1,COUNT1])  
        st.success(male_mention_centrality)
    
    if __name__ == '__main__':
        main()

if selected == "Female Centrality":
    st.title('Predict your Centrality')
    st.subheader('Enter the details')
    model = pickle.load(open('female.sav','rb'))
    
    def mcf(input_data):
        na = np.asarray(input_data)
        d = na.reshape(1,-1)
        
        prediction = model.predict(d)
        return prediction


    def main():

        MENTIONS = st.text_input('MENTIONS')
        TOTAL_CENTRALITY = st.text_input('TOTAL_CENTRALITY')
        COUNT = st.text_input('COUNT')

          

        female_mention_centrality = ''
        if st.button('Get Centrality'):
            female_mention_centrality  = mcf([MENTIONS,TOTAL_CENTRALITY,COUNT])  
        st.success(female_mention_centrality)


    if __name__ == '__main__':
        main()

if selected == "About":
    #st.title('About')
    st.title('Hi, Anirudh here :smiley:')
    st.subheader('Hope this app was useful to you :innocent:')
    st.write('The app helps you find the centrality of the cast with a few parameters!')
    st.write('[More projects in GITHUB >](https://github.com/4nirudh5)')
