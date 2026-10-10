# app.py
import streamlit as st
from build_db import generate_gemini_numerology_reading
from numerology_engine import get_full_profile
from pdf_generator import create_numerology_pdf
from datetime import datetime

st.set_page_config(
    page_title="CosmicVibe - Advanced Pythagorean Numerology AI",
    page_icon="🔮",
    layout="centered"
)

# --- 🌌 MYSTICAL DARK-MODE STYLE INJECTION ---
st.markdown(
    """
    <style>
    /* Main background theme config */
    .stApp {
        background: linear-gradient(135deg, #0d0b21 0%, #161233 50%, #080614 100%) !important;
        color: #e0dbff !important;
    }
    
    /* Input form layout box styling */
    [data-testid="stForm"] {
        background-color: rgba(25, 20, 55, 0.55) !important;
        border: 1px solid rgba(147, 112, 219, 0.4) !important;
        border-radius: 12px !important;
        box-shadow: 0 4px 20px rgba(147, 112, 219, 0.15) !important;
    }

    /* Headings adjustments */
    h1, h2, h3, h4, h5, h6, label, p, span, [data-testid="stWidgetLabel"] p {
        color: #f1ecff !important;
    }

    /* 🌟 CRITICAL FIX: Target input text boxes, date pickers, and their text streams */
    input[type="text"], input[type="date"], .stTextInput input, div[data-baseweb="input"] input {
        color: #ffffff !important; /* Forces typed text to be bright white */
        background-color: #17123a !important; /* Deep dark purple input background */
        -webkit-text-fill-color: #ffffff !important; /* Fix for safari/chrome text overrides */
        font-weight: 500 !important;
    }

    /* Force the placeholder text to be a legible muted lavender */
    input::placeholder {
        color: #a399e6 !important;
        opacity: 1;
    }

    /* Add a glowing neon purple border when clicking inside an input box */
    input:focus, div[data-baseweb="input"]:focus-within {
        border-color: #bf8aff !important;
        box-shadow: 0 0 10px rgba(191, 138, 255, 0.6) !important;
    }

    /* Custom classes for the 3x3 Grid Containers with Neon Purple Glow */
    .matrix-box {
        background: rgba(30, 22, 65, 0.6) !important;
        border: 2px solid #8a2be2 !important;
        border-radius: 12px !important;
        padding: 20px !important;
        text-align: center !important;
        box-shadow: 0 0 15px rgba(138, 43, 226, 0.6), inset 0 0 10px rgba(138, 43, 226, 0.3) !important;
        margin-bottom: 15px !important;
    }

    .matrix-label {
        font-size: 0.85rem !important;
        color: #b3a7ff !important;
        text-transform: uppercase !important;
        letter-spacing: 1px !important;
        margin-bottom: 5px !important;
        font-weight: bold !important;
    }

    .matrix-value {
        font-size: 2.2rem !important;
        font-weight: 800 !important;
        color: #00ffff !important; /* Glowing Neon Cyan values */
        text-shadow: 0 0 10px rgba(0, 255, 255, 0.8) !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("🔮 CosmicVibe Advanced AI Agent")
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
    
    # --- Visual 3x3 Birth Chart Grid Matrix Box ---
    st.write("### 📊 Your Pythagorean Birth Chart Grid")
    st.caption("Dr. Phillips' Three Planes of Human Experience: Mind (Top), Soul (Middle), Physical (Bottom)")
    
    # Pull the exact raw calculated profile math figures dynamically
    raw_profile = get_full_profile(st.session_state.cached_date)
    grid_data = raw_profile.get("birth_chart_grid", {i: 0 for i in range(1, 10)})
    
    # Generate visual string blocks for the matrix cells
    def make_cell(num):
        count = grid_data.get(num, 0)
        return str(num) * count if count > 0 else "-"

    # Helper helper wrapper block to render custom styled glowing TOML html markup injection
    def render_glow_box(label, value):
        st.markdown(
            f"""
            <div class="matrix-box">
                <div class="matrix-label">{label}</div>
                <div class="matrix-value">{value}</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    # Render Dr. Phillips' Exact 3x3 Layout Grid Rows using HTML Injection inside columns
    # Row 1: Mind Plane (3, 6, 9)
    r1_c1, r1_c2, r1_c3 = st.columns(3)
    with r1_c1: render_glow_box("Mind (3)", make_cell(3))
    with r1_c2: render_glow_box("Mind (6)", make_cell(6))
    with r1_c3: render_glow_box("Mind (9)", make_cell(9))
    
    # Row 2: Soul Plane (2, 5, 8)
    r2_c1, r2_c2, r2_c3 = st.columns(3)
    with r2_c1: render_glow_box("Soul (2)", make_cell(2))
    with r2_c2: render_glow_box("Soul (5)", make_cell(5))
    with r2_c3: render_glow_box("Soul (8)", make_cell(8))
    
    # Row 3: Physical Plane (1, 4, 7)
    r3_c1, r3_c2, r3_c3 = st.columns(3)
    with r3_c1: render_glow_box("Physical (1)", make_cell(1))
    with r3_c2: render_glow_box("Physical (4)", make_cell(4))
    with r3_c3: render_glow_box("Physical (7)", make_cell(7))
    
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
