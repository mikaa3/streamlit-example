import streamlit as st
import numpy as np
import matplotlib.pyplot as plt




st.header('Loading capacity of ice')



st.latex('''
    loading \space capacity = 5 * thickness \space (cm)^2
    ''')

thickness = st.sidebar.slider('Thickness of ice (cm)', 0, 100, 10)
load_capacity = 5 * thickness ** 2
st.write('The load capacity of the ice is', load_capacity, 'kg')

# calculate the radius of influence, round to 2 decimal places

radius_of_influence = round(0.5 * thickness ** 0.75, 2)

st.latex('''
    radius \space of \space influence = 0.5 * thickness \space (cm)^{3/4}
    ''')







st.write('Radius of influence is ', radius_of_influence,' m')









 # Adding a toggle switch to the sidebar
toggle = st.sidebar.checkbox('Jäälautta')

    # Displaying the state of the toggle switch
if toggle:
        st.success("The toggle is ON!")
        st.header('Loadin capacity of ice')

        length = st.sidebar.slider('Lenght of ice float (m)', 0.0, 10.0, 2.0, step=0.5)
        width = st.sidebar.slider('Width of icefloat (m)', 0.0, 10.0, 2.0, step=0.5)

        volume = round(thickness /100 * length * width, 2)
        st.write('The volume of the ice float is', volume, 'm^3')

        mass = round(volume * 917, 2) #density of ice
        st.write('The mass of the ice float is', mass, 'kg (density of ice = 917 kg/m^3)')

        bouancy = volume * 1000 #density of water
        st.write('The bouancy of the ice float is', bouancy, 'kg')

        ice_float_load_capacity = round(bouancy - mass,2)
        st.write('The load capacity of the ice float is', ice_float_load_capacity, 'kg')


        
else:
        st.error("The toggle is OFF!")





on = st.toggle('Jäälautta?')

if on:
    st.write('Feature activated!')


    st.write('Ice floating on water')
    st.write('The fraction of ice floating on water is given by the formula:')
    st.write('Fraction = 1 - (density of ice) / density of water)')
    st.write('Density of ice = 917 kg/m^3')
    st.write('Density of water = 1000 kg/m^3')

    fraction = round(1 - (917 / 1000), 2)
    st.write('The fraction of ice floating above water is', fraction)
