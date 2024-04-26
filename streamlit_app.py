import streamlit as st

st.write('Loadin capacity of ice')
st.write('Loading capacity (kg) = 5 * thickness (cm) ^2')

thickness = st.slider('Thickness of ice (cm)', 0, 200, 10)
load = 5 * thickness ** 2
st.write('The load capacity of the ice is', load, 'kg')

st.write('❄️')
