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

# --- 🌌 TWINKLING STARFIELD & MYSTICAL ACCENTS OVERRIDE ---
st.markdown(
    """
    <style>
    /* Main application container with a deep space cosmic base layer */
    .stApp {
        background: radial-gradient(circle at 50% 50%, #110e2e 0%, #09071a 70%, #03020a 100%) !important;
        position: relative;
        overflow: hidden;
    }
    
    /* Create an animated twinkling star layer behind everything */
    .stApp::before {
        content: "";
        position: absolute;
        top: 0; left: 0; width: 100%; height: 100%;
        background-image: 
            radial-gradient(white, rgba(255,255,255,.2) 2px, transparent 40px),
            radial-gradient(white, rgba(255,255,255,.15) 1px, transparent 30px),
            radial-gradient(white, rgba(255,255,255,.1) 2px, transparent 40px);
        background-size: 550px 550px, 350px 350px, 250px 250px;
        background-position: 0 0, 40px 60px, 130px 270px;
        opacity: 0.4;
        animation: cosmicTwinkle 120s linear infinite;
        z-index: 0;
        pointer-events: none;
    }
    
    @keyframes cosmicTwinkle {
        from { background-position: 0 0, 40px 60px, 130px 270px; }
        to { background-position: 550px 1100px, 350px 700px, 250px 500px; }
    }

    /* Force all app text to sit forward cleanly over our background graphics */
    p, li, span, label, div, h1, h2, h3, h4, h5, h6, [data-testid="stMarkdownContainer"] {
        color: #f1ecff !important;
        position: relative;
        z-index: 1;
    }

    /* Bright high-contrast silver text layout block for readings */
    [data-testid="stMarkdownContainer"] p, [data-testid="stMarkdownContainer"] li {
        color: #f8f6ff !important;
        font-size: 1.05rem !important;
        line-height: 1.6 !important;
    }
    
    /* Input form layout block container styling */
    [data-testid="stForm"] {
        background-color: rgba(20, 15, 48, 0.75) !important;
        border: 1px solid rgba(147, 112, 219, 0.5) !important;
        border-radius: 12px !important;
        box-shadow: 0 0 25px rgba(147, 112, 219, 0.2) !important;
        position: relative;
        z-index: 1;
    }

    /* Input elements text value fixes */
    input[type="text"], input[type="date"], .stTextInput input, div[data-baseweb="input"] input, div[data-baseweb="select"] {
        color: #ffffff !important;
        background-color: #0c0824 !important;
        font-weight: 600 !important;
    }

    /* Calendar overlay fixes */
    div[role="listbox"], div[role="menu"], div[data-baseweb="calendar"] {
        background-color: #110d33 !important;
        color: #ffffff !important;
    }
    
    div[data-baseweb="calendar"] button {
        color: #ffffff !important;
    }

    input::placeholder {
        color: #9d92f2 !important;
        opacity: 1 !important;
    }

    /* Visual 3x3 Grid Matrix Box Accents */
    .matrix-box {
        background: rgba(22, 16, 54, 0.85) !important;
        border: 2px solid #8a2be2 !important;
        border-radius: 12px !important;
        padding: 20px !important;
        text-align: center !important;
        box-shadow: 0 0 20px rgba(138, 43, 226, 0.6), inset 0 0 10px rgba(138, 43, 226, 0.3) !important;
        margin-bottom: 15px !important;
    }

    .matrix-label {
        font-size: 0.85rem !important;
        color: #c4bbff !important;
        text-transform: uppercase !important;
        letter-spacing: 1px !important;
        margin-bottom: 5px !important;
        font-weight: bold !important;
    }

    .matrix-value {
        font-size: 2.2rem !important;
        font-weight: 800 !important;
        color: #00ffff !important; 
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
    
    st.write("### 📊 Your Pythagorean Birth Chart Grid")
    st.caption("Dr. Phillips' Three Planes of Human Experience: Mind (Top), Soul (Middle), Physical (Bottom)")
    
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
