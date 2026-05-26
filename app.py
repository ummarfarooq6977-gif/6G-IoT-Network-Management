import streamlit as st
from simulation import generate_state
from optimizer import optimize

st.title("6G IoT Network Management Dashboard")
state = generate_state()
result = optimize(state)
st.write("Current State", state)
st.write("Optimized Allocation", result)
