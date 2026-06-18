import streamlit as st
from api import get_all_flights,search_flight
from components.metric import show_metrics
from components.cards import flight_card


st.set_page_config(
    page_title="SkyVi",
    page_icon="✈️",
    layout="wide"
)
data = get_all_flights()

st.title("✈️ SkyVi")
st.caption("Skyward Vision")
st.markdown("### Real-Time Aviation Intelligence Dashboard")
st.info(
    "Track live flights, analyze aviation data, and gain real-time insights from around the world."
)

st.divider()
show_metrics(data)
st.divider()

st.subheader("🔍 Flight Search")

flight_number = st.text_input(
    "Enter Flight Number",
    placeholder="e.g. AI101, EK515, BA256"
)

if st.button("Track Flight"):
    if flight_number:
        flight = search_flight(flight_number)
        if flight:
            st.success("✅ Flight Found!")
            flight_card(flight)
        else:
            st.error("❌ Flight not found.")
    else:
        st.warning("Please enter a flight number.")