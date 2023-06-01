import pickle
import streamlit as st
import requests

def recommend(vehicle):
    index = vehicles[vehicles['city'] == vehicle].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_vehicles_name =[]
    recommended_owners_name =[]
    for i in distances[1:6]:
        recommended_vehicles_name.append(vehicles.iloc[i[0]].Brand)
        recommended_owners_name.append(vehicles.iloc[i[0]].ownerid)
    return recommended_vehicles_name,recommended_owners_name

st.header("Vahan Rent")
vehicles = pickle.load(open('artificats/vehicle_list.pkl','rb'))
similarity = pickle.load(open('artificats/similarity.pkl','rb'))

vehicle_list = vehicles['city'].values
selected_vehicle= st.selectbox(
    'Enter Location',
    vehicle_list
)

if st.button('show recommendation'):
    recommended_vehicles_name,recommended_owners_name = recommend(selected_vehicle)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_vehicles_name[0])
        st.text(recommended_owners_name[0])
    with col2:
        st.text(recommended_vehicles_name[1])
        st.text(recommended_owners_name[1])
    with col3:
        st.text(recommended_vehicles_name[2])
        st.text(recommended_owners_name[2])
    with col4:
        st.text(recommended_vehicles_name[3])
        st.text(recommended_owners_name[3])            
    with col5:
        st.text(recommended_vehicles_name[4])
        st.text(recommended_owners_name[4])
