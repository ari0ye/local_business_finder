import streamlit as st
from categories import CATEGORY_MAP
from location_manager import get_coordinates
from business_finder import find_businesses
from streamlit_folium import st_folium
import folium
import pandas as pd  # Needed for table formatting

# --- Page Config ---
st.set_page_config(
    page_title="Local Business Finder",
    layout="wide"
)

st.title("LOCAL BUSINESS FINDER")
st.caption("Find businesses near a given location, powered by Geoapify API.")

# --- Sidebar Search ---
st.sidebar.header("SEARCH")
address = st.sidebar.text_input("Enter address or location")  # User input for address
selected_category = st.sidebar.selectbox("Choose category", list(CATEGORY_MAP.keys()))  # Category selection
search_button = st.sidebar.button("Search")  # Search trigger button

# --- Session state ---
if 'results' not in st.session_state:
    st.session_state.results = None  # Initialize results in session state

# --- Perform Search ---
if search_button:
    if address and selected_category:
        lat, lon = get_coordinates(address)  # Get latitude and longitude from address
        if lat and lon:
            businesses = find_businesses(lat, lon, CATEGORY_MAP[selected_category])  # Find businesses nearby
            if businesses:
                st.session_state.results = {
                    "category": selected_category,
                    "lat": lat,
                    "lon": lon,
                    "businesses": businesses
                }
            else:
                st.warning("No businesses found.")  # No results found
        else:
            st.error("Could not get coordinates for the provided address.")  # Invalid address
    else:
        st.error("Please provide both an address and category.")  # Missing input

# --- Display Results ---
if st.session_state.results:
    results = st.session_state.results

    # KPIs
    c1, c2, c3 = st.columns(3)
    c1.metric("Category", results["category"])
    c2.metric("Businesses Found", len(results["businesses"]))
    c3.metric("Coordinates", f"{results['lat']:.4f}, {results['lon']:.4f}")

    st.divider()

    tab1, tab2 = st.tabs(["📋 Table View", "🗺️ Map View"])

    with tab1:
        # Prepare table data with clickable website/email links
        table_data = []
        for b in results["businesses"]:
            website_link = f'<a href="{b.website}" target="_blank">Visit Website</a>' if b.website else ""
            email_link = f'<a href="mailto:{b.email}">{b.email}</a>' if b.email else ""
            table_data.append({
                "Name": b.name,
                "Address": b.address,
                "Website": website_link,
                "Email": email_link
            })

        df = pd.DataFrame(table_data)
        st.markdown(df.to_html(escape=False, index=False), unsafe_allow_html=True)  # Render table with HTML links

    with tab2:
        # Show businesses on a map using Folium
        m = folium.Map(location=[results["lat"], results["lon"]], zoom_start=14)
        for b in results["businesses"]:
            folium.Marker(
                [b.lat, b.lon],
                popup=f"<b>{b.name}</b><br>{b.address}",
                tooltip=b.name
            ).add_to(m)
        st_folium(m, width=900, height=500)  # Display map in Streamlit
