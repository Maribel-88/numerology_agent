# app.py
import streamlit as st
from build_db import generate_gemini_numerology_reading
from numerology_engine import get_full_profile  # Import the core logic directly for the grid
from pdf_generator import create_numerology_pdf
from datetime import datetime

st.set_page_config(
    page_title="CosmicVibe - Advanced Pythagorean Numerology AI",
    page_icon="✨",
    layout="centered"
)

st.title("✨ CosmicVibe Advanced AI Agent")
st.subheader("Unified Birthdate & Full Name Matrix — Dr. David A. Phillips System")
st.write("Enter your details below to generate your complete Pythagorean spiritual profile and interactive chart matrix.")

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
    
    # --- BRAND NEW FEATURE: Visual 3x3 Birth Chart Grid Matrix Box ---
    st.write("### 📊 Your Pythagorean Birth Chart Grid")
    st.caption("Dr. Phillips' Three Planes of Human Experience: Mind (Top), Soul (Middle), Physical (Bottom)")
    
    # Pull the exact raw calculated profile math figures dynamically
    raw_profile = get_full_profile(st.session_state.cached_date)
    grid_data = raw_profile.get("birth_chart_grid", {i: 0 for i in range(1, 10)})
    
    # Generate visual string blocks for the matrix cells (e.g., "33" if two 3s exist, or "-" if empty)
    def make_cell(num):
        count = grid_data.get(num, 0)
        return str(num) * count if count > 0 else "-"

    # Render Dr. Phillips' Exact 3x3 Layout Grid Rows using Streamlit Columns layout
    # Row 1: Mind Plane (3, 6, 9)
    r1_c1, r1_c2, r1_c3 = st.columns(3)
    with r1_c1: st.metric(label="🧠 Mind Cell (3)", value=make_cell(3))
    with r1_c2: st.metric(label="🧠 Mind Cell (6)", value=make_cell(6))
    with r1_c3: st.metric(label="🧠 Mind Cell (9)", value=make_cell(9))
    
    # Row 2: Soul Plane (2, 5, 8)
    r2_c1, r2_c2, r2_c3 = st.columns(3)
    with r2_c1: st.metric(label="❤️ Soul Cell (2)", value=make_cell(2))
    with r2_c2: st.metric(label="❤️ Soul Cell (5)", value=make_cell(5))
    with r2_c3: st.metric(label="❤️ Soul Cell (8)", value=make_cell(8))
    
    # Row 3: Physical Plane (1, 4, 7)
    r3_c1, r3_c2, r3_c3 = st.columns(3)
    with r3_c1: st.metric(label="🧱 Physical Cell (1)", value=make_cell(1))
    with r3_c2: st.metric(label="🧱 Physical Cell (4)", value=make_cell(4))
    with r3_c3: st.metric(label="🧱 Physical Cell (7)", value=make_cell(7))
    
    st.divider()
    
    # --- PDF Download Hub Layout Box ---
    st.write("### 📥 Save Your Blueprint Profile Report")
    
    pdf_data = create_numerology_pdf(
        st.session_state.cached_name,
        st.session_state.cached_date,
        st.session_state.reading_cache
    )
    
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
