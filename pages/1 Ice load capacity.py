import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

ice_density = 917 # kg/m³ 


# Adding a toggle switch to the sidebar
toggle = st.sidebar.checkbox('Ice float')

    # Displaying the state of the toggle switch
if toggle: # ICE FLOAT
      
        st.header('Static load capacity of ice float')

        thickness = st.sidebar.slider('Thickness of ice (cm)', 0, 150, 10)
                
        length = st.sidebar.slider('Lenght of ice float (m)', 0.0, 10.0, 2.0, step=0.5)
        width = st.sidebar.slider('Width of icefloat (m)', 0.0, 10.0, 2.0, step=0.5)

        volume = round(thickness /100 * length * width, 2)

        'Ice density:', ice_density, 'kg/m³'
        'Ice thickness:', thickness, 'cm'
        st.write('The volume of the ice float is', volume, 'm³')

        mass = round(volume * 917, 2) #density of ice
        'The mass of the ice float is', mass, 'kg'

        bouancy = volume * 1000 #density of water
        st.write('The bouancy of the ice float is', bouancy, 'kg')

        ice_float_load_capacity = round(bouancy - mass,2)
        st.write('The load capacity of the ice float is', ice_float_load_capacity, 'kg')

else: # NO ICE FLOAT
        
        thickness = st.sidebar.slider('Thickness of ice (cm)', 0, 50, 10)
        deepness = st.sidebar.slider('water deepness (m)', 0, 50, 3)
        
        st.header('Static load capacity of ice')
                
        'Ice density:', ice_density, 'kg/m³'
        'Ice thickness:', thickness, 'cm'
        
        load_capacity = 5 * thickness ** 2 
        'The load capacity of the ice is', load_capacity, 'kg'

        # calculate the radius of influence, round to 2 decimal places
        radius_of_influence = round(0.51 * thickness ** 0.75, 2)

        'Radius of influence is ', radius_of_influence , 'm'
        
        st.header('Dynamic load capacity of ice')
        'Moving on ice creates pressure waves, that have a resonance frequency.'
        
        # wave speed = 3.1 * sqr(deepness)
        wave_speed_ms = round(3.1 * np.sqrt(deepness), 2)
        wave_speed_kmh = round(wave_speed_ms * 3.6, 2)
        st.write('The wave speed is', wave_speed_ms, 'm/s')
        st.write('The wave speed is', wave_speed_kmh, 'km/h')
        
        st.divider()
        
        st.latex('''
            Load \space capacity = 5 * thickness \space (cm)^2
            ''')
        
        # display the formula for the radius of influence
        st.latex('''
            Radius \space of \space influence = 0.51 * thickness \space (cm)^{3/4}
            ''')

        # display the formula for the wave speed
        st.latex('''
            Wave \space speed \space (m/s) = 3.1 * \sqrt{\smash[b]{deepness \space (m)}})
            ''')

