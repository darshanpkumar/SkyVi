import streamlit as st


def show_metrics(data):
    if data:
        total_flights = len(data.get("states", []))

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("🛫 Flights Tracked", total_flights)

        with col2:
            st.metric("✈ Aircraft", total_flights)

        with col3:
            st.metric("🟢 API Status", "Live")

    else:
        st.error("Unable to fetch live flight data.")