import streamlit as st

st.set_page_config(
    page_title="SkyVi",
    page_icon="✈️",
    layout="wide"
)

st.title("✈️ SkyVi")
st.caption("Skyward Vision")
st.markdown("### Real-Time Aviation Intelligence Dashboard")
st.info(
    "Track live flights, analyze aviation data, and gain real-time insights from around the world."
)

st.divider()

col1, col2, col3 = st.columns(3)
with col1:
    st.metric("🛫 Flights Tracked", "--")
with col2:
    st.metric("✈️ Aircraft", "--")
with col3:
    st.metric("🌍 Airports", "--")
st.divider()

st.subheader("🔍 Flight Search")

flight_number = st.text_input(
    "Enter Flight Number",
    placeholder="e.g. AI101, EK515, BA256"
)

if st.button("Track Flight"):
    if flight_number:
        st.success(f"Searching live data for ✈️ {flight_number.upper()}...")
    else:
        st.warning("Please enter a flight number.")