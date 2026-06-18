import streamlit as st


def flight_card(flight):

    st.subheader("✈️ Flight Information")

    col1, col2 = st.columns(2)

    altitude = flight.get("altitude_ft")
    speed = flight.get("velocity_kmh")
    latitude = flight.get("latitude")
    longitude = flight.get("longitude")

    with col1:
        st.metric("🛫 Callsign", flight.get("callsign", "N/A"))
        st.metric("🌍 Country", flight.get("country", "N/A"))
        st.metric(
            "📏 Altitude",
            f"{altitude:.0f} ft" if altitude is not None else "N/A"
        )

    with col2:
        speed = flight.get("velocity_kmh")

        st.metric(
            "🚀 Speed",
            f"{speed:.0f} km/h" if speed is not None else "N/A"
        )
        st.metric(
            "📍 Latitude",
            f"{latitude:.3f}" if latitude is not None else "N/A"
        )
        st.metric(
            "📍 Longitude",
            f"{longitude:.3f}" if longitude is not None else "N/A"
        )