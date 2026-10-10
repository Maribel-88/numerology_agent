# app.py
import streamlit as st
from build_db import generate_gemini_numerology_reading
from pdf_generator import create_numerology_pdf  # Import our brand new PDF writer module
from datetime import datetime

st.set_page_config(
    page_title="CosmicVibe - Advanced Pythagorean Numerology AI",
    page_icon="✨",
    layout="centered"
)

st.title("✨ CosmicVibe Advanced AI Agent")
st.subheader("Unified Birthdate & Full Name Matrix — Dr. David A. Phillips System")
st.write("Enter your details below to generate and export your complete Pythagorean spiritual profile.")

st.divider()

# Instantiate continuous storage variables inside Streamlit session configurations
if "reading_cache" not in st.session_state:
    st.session_state.reading_cache = None
if "cached_name" not in st.session_state:
    st.session_state.cached_name = ""
if "cached_date" not in st.session_state:
    st.session_state.cached_date = ""

# Input interface elements form setup
with st.form("numerology_form"):
    full_name_input = st.text_input(
        "Your Full Birth Name (First, Middle, Last):",
        placeholder="e.g., JOHN BENJAMIN SMITH"
    )
    
    default_date = datetime(1985, 5, 12)
    selected_date = st.date_input(
        "Your Date of Birth:",
        value=default_date,
        min_value=datetime(1920, 1, 1),
        max_value=datetime.today()
    )
    
    submit_button = st.form_submit_button("Cast Unified Matrix Reading 🔮", use_container_width=True)

# Form Trigger Actions
if submit_button:
    if not full_name_input.strip():
        st.warning("⚠️ Please enter your full birth name to calculate your name matrix!")
    else:
        formatted_date = selected_date.strftime("%d/%m/%Y")
        
        with st.spinner("Decoding your alphanumeric cosmic grids... Please wait..."):
            # Execute core agent pipeline computation stream
            reading_output = generate_gemini_numerology_reading(formatted_date, full_name_input)
            
            # Cache outputs locally inside active state contexts
            st.session_state.reading_cache = reading_output
            st.session_state.cached_name = full_name_input
            st.session_state.cached_date = formatted_date

# Persistent display container block layer configuration logic
if st.session_state.reading_cache:
    st.divider()
    
    # --- BRAND NEW FEATURE: Dynamic PDF Download Hub Layout Box ---
    st.write("### 📥 Save Your Blueprint Profile Report")
    
    # Generate the raw data binary stream directly across the layout cache
    pdf_data = create_numerology_pdf(
        st.session_state.cached_name,
        st.session_state.cached_date,
        st.session_state.reading_cache
    )
    
    # Streamlit standard secure internal binary asset downloader pipeline downloader block module
    st.download_button(
        label="Download Professional PDF Report 📄",
        data=bytes(pdf_data),
        file_name=f"Numerology_Report_{st.session_state.cached_name.replace(' ', '_')}.pdf",
        mime="application/pdf",
        use_container_width=True
    )
    
    st.divider()
    
    # Print raw markdown interpretation directly on screen
    st.markdown(st.session_state.reading_cache)

st.caption("Powered by Google Gemini 3.8 Flash & Your Custom Pythagorean Local Engine.")
