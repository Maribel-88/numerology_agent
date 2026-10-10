# app.py
import streamlit as st
from build_db import generate_gemini_numerology_reading
from numerology_engine import get_full_profile, calculate_personal_year, get_zodiac_sign  # Added zodiac function
from pdf_generator import create_numerology_pdf
import numerology_data
from datetime import datetime

st.set_page_config(
    page_title="CosmicVibe - Advanced Pythagorean Numerology AI",
    page_icon="🔮",
    layout="centered"
)

# --- 🌌 HIGH-CONTRAST COSMIC STYLE INJECTION ---
st.markdown(
    """
    <style>
    .stApp {
        background-color: #0b081a !important;
    }
    h1, h2, h3, h4, h5, h6, label, p, span {
        color: #f1ecff !important;
    }
    [data-testid="stMarkdownContainer"] p, [data-testid="stMarkdownContainer"] li {
        color: #ffffff !important;
        font-size: 1.05rem !important;
        line-height: 1.6 !important;
    }
    [data-testid="stForm"] {
        background-color: #120e2b !important;
        border: 2px solid #5a3d96 !important;
        border-radius: 12px !important;
        padding: 20px !important;
    }
    .stTextInput input, input[type="text"] {
        color: #ffffff !important;
        background-color: #1b163d !important;
        border: 1px solid #7d5bb5 !important;
        border-radius: 6px !important;
        -webkit-text-fill-color: #ffffff !important;
        font-weight: 600 !important;
    }
    div[data-testid="stDateInput"] div {
        background-color: #1b163d !important;
        border: 2px solid #7d5bb5 !important;
        border-radius: 6px !important;
    }
    div[data-testid="stDateInput"] input {
        color: #ffffff !important;
        background-color: transparent !important;
        -webkit-text-fill-color: #ffffff !important;
        font-weight: 600 !important;
    }
    button[data-testid="baseButton-formSubmit"] {
        background-color: #4b1a8a !important;
        color: #ffffff !important;
        border: 2px solid #9966ff !important;
        border-radius: 8px !important;
        font-weight: bold !important;
        padding: 10px 20px !important;
        box-shadow: 0 0 12px rgba(153, 102, 255, 0.4) !important;
    }
    .matrix-box {
        background: #19143a !important;
        border: 2px solid #8a2be2 !important;
        border-radius: 12px !important;
        padding: 15px !important;
        text-align: center !important;
        margin-bottom: 10px !important;
    }
    .matrix-label {
        font-size: 0.85rem !important;
        color: #b3a7ff !important;
        text-transform: uppercase !important;
        font-weight: bold !important;
    }
    .matrix-value {
        font-size: 2.0rem !important;
        font-weight: 800 !important;
        color: #00ffff !important; 
    }
    .year-box {
        background: linear-gradient(90deg, #1f1440 0%, #29124d 100%) !important;
        border-left: 5px solid #ff00ff !important;
        padding: 20px !important;
        border-radius: 8px !important;
        margin-top: 15px !important;
        box-shadow: 0 4px 15px rgba(255, 0, 255, 0.1) !important;
    }
    /* 🔮 NEW: Styled callout card for your Zodiac Sign */
    .zodiac-box {
        background: linear-gradient(90deg, #0e2042 0%, #152e5c 100%) !important;
        border-left: 5px solid #00ffff !important;
        padding: 15px 20px !important;
        border-radius: 8px !important;
        margin-bottom: 20px !important;
        box-shadow: 0 4px 15px rgba(0, 255, 255, 0.1) !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("🔮 CosmicVibe Advanced AI Agent")
st.subheader("Unified Birthdate & Full Name Matrix — Dr. David A. Phillips System")

st.divider()

if "reading_cache" not in st.session_state:
    st.session_state.reading_cache = None
if "cached_name" not in st.session_state:
    st.session_state.cached_name = ""
if "cached_date" not in st.session_state:
    st.session_state.cached_date = ""

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

if submit_button:
    if not full_name_input.strip():
        st.warning("⚠️ Please enter your full birth name to calculate your name matrix!")
    else:
        formatted_date = selected_date.strftime("%d/%m/%Y")
        
        with st.spinner("Decoding your alphanumeric cosmic grids... Please wait..."):
            reading_output = generate_gemini_numerology_reading(formatted_date, full_name_input)
            st.session_state.reading_cache = reading_output
            st.session_state.cached_name = full_name_input
            st.session_state.cached_date = formatted_date

if st.session_state.reading_cache:
    st.divider()
    
    # 🌟 NEW FEATURE LAYER: ZODIAC ELEMENT ELEMENT GRID INFOCARD
    zodiac_profile = get_zodiac_sign(st.session_state.cached_date)
    
    st.markdown(
        f"""
        <div class="zodiac-box">
            <h4 style='margin-top:0; color:#ccffff !important;'>✨ ASTROLOGICAL ALIGNMENT DETECTED</h4>
            <p style='font-size:1.2rem; margin:0; color:#ffffff !important;'>
                Your Sun Sign: <b>{zodiac_profile['emoji']} {zodiac_profile['sign']}</b> 
                <span style='margin-left:15px; font-size:0.95rem; color:#a3e6ff !important;'>Element: <b>{zodiac_profile['element']}</b></span>
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    # --- Personal Year Cycle Forecast ---
    st.write("### 📅 Your Personal Year Cycle Forecast")
    target_year = st.slider("Select Target Year to Forecast:", min_value=2020, max_value=2035, value=2026, step=1)
    
    py_num = calculate_personal_year(st.session_state.cached_date, target_year)
    py_meaning = numerology_data.PERSONAL_YEARS.get(py_num, "General timeline mapping.")
    
    st.markdown(
        f"""
        <div class="year-box">
            <h4 style='margin-top:0; color:#ffccff !important;'>🌟 FORECAST FOR CALENDAR YEAR {target_year}</h4>
            <p style='font-size:1.15rem; font-weight:bold; color:#00ffff !important; margin-bottom:5px;'>Your Personal Year Number: {py_num}</p>
            <p style='margin:0; font-style:italic; color:#ffffff !important;'>{py_meaning}</p>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    st.divider()
    
    # --- Visual 3x3 Birth Chart Grid Matrix Box ---
    st.write("### 📊 Your Pythagorean Birth Chart Grid")
    
    raw_profile = get_full_profile(st.session_state.cached_date)
    grid_data = raw_profile.get("birth_chart_grid", {i: 0 for i in range(1, 10)})
    
    def make_cell(num):
        count = grid_data.get(num, 0)
        return str(num) * count if count > 0 else "-"

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

    r1_c1, r1_c2, r1_c3 = st.columns(3)
    with r1_c1: render_glow_box("Mind (3)", make_cell(3))
    with r1_c2: render_glow_box("Mind (6)", make_cell(6))
    with r1_c3: render_glow_box("Mind (9)", make_cell(9))
    
    r2_c1, r2_c2, r2_c3 = st.columns(3)
    with r2_c1: render_glow_box("Soul (2)", make_cell(2))
    with r2_c2: render_glow_box("Soul (5)", make_cell(5))
    with r2_c3: render_glow_box("Soul (8)", make_cell(8))
    
    r3_c1, r3_c2, r3_c3 = st.columns(3)
    with r3_c1: render_glow_box("Physical (1)", make_cell(1))
    with r3_c2: render_glow_box("Physical (4)", make_cell(4))
    with r3_c3: render_glow_box("Physical (7)", make_cell(7))
    
    st.divider()
    
    # --- PDF Download Hub ---
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
    st.markdown(st.session_state.reading_cache)

st.caption("Powered by Google Gemini 3.8 Flash & Your Custom Pythagorean Local Engine.")
