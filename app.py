# app.py
import streamlit as st
from build_db import generate_gemini_numerology_reading, generate_gemini_compatibility_reading
from numerology_engine import get_full_profile, calculate_personal_year, get_zodiac_sign
from pdf_generator import create_numerology_pdf
import numerology_data
from datetime import datetime

st.set_page_config(
    page_title="CosmicVibe - Advanced Pythagorean Numerology AI",
    page_icon="🔮",
    layout="centered"
)

# --- 🌌 COMPREHENSIVE TEXT VISIBILITY & FRAMEWORK OVERRIDE ---
st.markdown(
    """
    <style>
    /* Direct block background canvas override */
    .stApp {
        background-color: #0b081a !important;
    }
    
    /* FIXING THE SIDEBAR COLORING & TEXT ACCENTS */
    section[data-testid="stSidebar"] {
        background-color: #120e2b !important; /* Deep dark purple sidebar background */
        border-right: 1px solid rgba(147, 112, 219, 0.3) !important;
    }
    
    section[data-testid="stSidebar"] p, section[data-testid="stSidebar"] span, section[data-testid="stSidebar"] label {
        color: #f1ecff !important; /* Forces sidebar labels to be clear and readable */
    }
    
    /* Global high-visibility text rules */
    h1, h2, h3, h4, h5, h6, label, p, span {
        color: #f1ecff !important;
    }

    /* Target reading block output texts explicitly */
    [data-testid="stMarkdownContainer"] p, [data-testid="stMarkdownContainer"] li {
        color: #ffffff !important;
        font-size: 1.05rem !important;
        line-height: 1.6 !important;
    }
    
    /* Input form layout box outline */
    [data-testid="stForm"] {
        background-color: #120e2b !important;
        border: 2px solid #5a3d96 !important;
        border-radius: 12px !important;
        padding: 20px !important;
    }

    /* NAME TEXT BOX ACCENT */
    .stTextInput input, input[type="text"] {
        color: #ffffff !important;
        background-color: #1b163d !important;
        border: 1px solid #7d5bb5 !important;
        border-radius: 6px !important;
        -webkit-text-fill-color: #ffffff !important;
        font-weight: 600 !important;
    }

    /* DATE PICKER BOX ACCENT OVERRIDE */
    div[data-testid="stDateInput"] div {
        background-color: #1b163d !important;
        border: 1px solid #7d5bb5 !important;
        border-radius: 6px !important;
    }
    
    div[data-testid="stDateInput"] input {
        color: #ffffff !important;
        background-color: transparent !important;
        -webkit-text-fill-color: #ffffff !important;
        font-weight: 600 !important;
    }

    /* FIXING THE CAST/ENTER BUTTON STYLING AND ICON COLOR */
    button[data-testid="baseButton-formSubmit"] {
        background: linear-gradient(90deg, #4b1a8a 0%, #6622cc 100%) !important;
        color: #ffffff !important; /* Crisp white button text */
        border: 1px solid #9966ff !important;
        border-radius: 8px !important;
        font-weight: bold !important;
        padding: 10px 20px !important;
        box-shadow: 0 0 12px rgba(153, 102, 255, 0.4) !important;
        transition: all 0.3s ease !important;
    }
    
    /* Force the button text/emoji inside to stay white instead of gray */
    button[data-testid="baseButton-formSubmit"] p, button[data-testid="baseButton-formSubmit"] span {
        color: #ffffff !important;
    }

    button[data-testid="baseButton-formSubmit"]:hover {
        background: linear-gradient(90deg, #5a24a3 0%, #7733ee 100%) !important;
        border-color: #b388ff !important;
        box-shadow: 0 0 18px rgba(179, 136, 255, 0.7) !important;
    }

    /* TAB NAVIGATION BAR TEXT VISIBILITY OVERRIDES */
    div[data-testid="stTabs"] button [data-testid="stMarkdownContainer"] p {
        color: #c4bbff !important; /* Forces INACTIVE tab text to be light visible purple-gray */
        font-weight: 600 !important;
        font-size: 1.0rem !important;
    }
    
    div[data-testid="stTabs"] button[aria-selected="true"] [data-testid="stMarkdownContainer"] p {
        color: #00ffff !important; /* Forces ACTIVE tab text to be high-contrast glowing cyan */
        text-shadow: 0 0 8px rgba(0, 255, 255, 0.5) !important;
    }
    
    /* Border underline alignment logic for the navigation bar tabs */
    div[data-testid="stTabs"] button {
        border-bottom: 2px solid rgba(147, 112, 219, 0.2) !important;
    }
    div[data-testid="stTabs"] button[aria-selected="true"] {
        border-bottom: 2px solid #00ffff !important;
    }

    /* Clean Structural 3x3 Chart Blocks */
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
    
    .year-box, .zodiac-box {
        background: linear-gradient(90deg, #1f1440 0%, #29124d 100%) !important; 
        border-left: 5px solid #ff00ff !important; 
        padding: 20px !important; 
        border-radius: 8px !important; 
        margin-top: 15px !important; 
        box-shadow: 0 4px 15px rgba(255, 0, 255, 0.1) !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("🔮 CosmicVibe Advanced AI Agent")
st.write("Unlock your unique Pythagorean configurations and interpersonal matrix structures.")

# --- SIDEBAR LANGUAGE MENU WIDGET ---
with st.sidebar:
    st.write("### 🌐 Language Hub")
    selected_language = st.selectbox(
        "Choose Presentation Language:",
        options=["English", "Español (Spanish)", "Français (French)", "Filipino", "Deutsch (German)", "Italiano (Italian)"],
        index=0
    )
    st.divider()
    st.caption("The AI Persona Engine automatically translates all generated narrative blocks into your selected language.")

# --- Tab Layout ---
tab1, tab2 = st.tabs(["👤 Individual Blueprint", "👥 Relationship Compatibility"])

# ================= TAB 1: INDIVIDUAL BLUEPRINT ENGINE =================
with tab1:
    if "reading_cache" not in st.session_state: 
        st.session_state.reading_cache = None
    if "cached_name" not in st.session_state: 
        st.session_state.cached_name = ""
    if "cached_date" not in st.session_state: 
        st.session_state.cached_date = ""

    with st.form("numerology_form"):
        full_name_input = st.text_input("Your Full Birth Name (First, Middle, Last):", placeholder="e.g., JOHN BENJAMIN SMITH")
        default_date = datetime(1985, 5, 12)
        selected_date = st.date_input("Your Date of Birth:", value=default_date, min_value=datetime(1920, 1, 1), max_value=datetime.today())
        submit_button = st.form_submit_button("Cast Blueprint Reading 🔮", use_container_width=True)

    if submit_button:
        if not full_name_input.strip():
            st.warning("⚠️ Please enter your name!")
        else:
            formatted_date = selected_date.strftime("%d/%m/%Y")
            with st.spinner("Decoding cosmic grids..."):
                reading_output = generate_gemini_numerology_reading(formatted_date, full_name_input, selected_language)
                st.session_state.reading_cache = reading_output
                st.session_state.cached_name = full_name_input
                st.session_state.cached_date = formatted_date

    if st.session_state.reading_cache:
        st.divider()
        
        # Render Zodiac Box
        z_profile = get_zodiac_sign(st.session_state.cached_date)
        st.markdown(f'<div class="zodiac-box"><h4 style="margin:0; color:#00ffff !important;">✨ {z_profile["emoji"]} SUN SIGN: {z_profile["sign"].upper()} (Element: {z_profile["element"]})</h4></div>', unsafe_allow_html=True)
        
        # Render Personal Year Tracker
        st.write("### 📅 Your Personal Year Cycle Forecast")
        target_year = st.slider("Select Target Year:", min_value=2020, max_value=2035, value=2026, step=1)
        py_num = calculate_personal_year(st.session_state.cached_date, target_year)
        py_meaning = numerology_data.PERSONAL_YEARS.get(py_num, "")
        st.markdown(f'<div class="year-box"><p style="margin:0; font-weight:bold; color:#ff00ff !important;">Personal Year Number: {py_num}</p><p style="margin:5px 0 0 0; font-style:italic;">{py_meaning}</p></div>', unsafe_allow_html=True)
        
        st.divider()
        
        # Render 3x3 Grid
        st.write("### 📊 Your Pythagorean Birth Chart Grid")
        raw_profile = get_full_profile(st.session_state.cached_date)
        grid_data = raw_profile.get("birth_chart_grid", {i: 0 for i in range(1, 10)})
        
        def make_cell(num): 
            return str(num) * grid_data.get(num, 0) if grid_data.get(num, 0) > 0 else "-"
            
        def render_glow_box(label, value): 
            st.markdown(f'<div class="matrix-box"><div class="matrix-label">{label}</div><div class="matrix-value">{value}</div></div>', unsafe_allow_html=True)
        
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
        
        # Export PDF Setup
        pdf_data = create_numerology_pdf(st.session_state.cached_name, st.session_state.cached_date, st.session_state.reading_cache)
        st.download_button(label="Download Professional PDF Report 📄", data=bytes(pdf_data), file_name=f"Report_{st.session_state.cached_name.replace(' ', '_')}.pdf", mime="application/pdf", use_container_width=True)
        
        st.divider()
        st.markdown(st.session_state.reading_cache)

# ================= TAB 2: DUAL MATRIX COMPATIBILITY LAYER =================
with tab2:
    if "comp_cache" not in st.session_state: 
        st.session_state.comp_cache = None
    
    st.write("### 👥 Calculate Dual Matrix Intersections")
    st.write("Examine how your numbers blend, collide, and support another person's matrix paths.")
    
    with st.form("compatibility_form"):
        col1, col2 = st.columns(2)
        with col1:
            st.write("#### Person 1 (You)")
            name1_in = st.text_input("First Person Full Name:", key="n1")
            date1_in = st.date_input("First Person Birthday:", value=datetime(1985, 5, 12), key="d1")
        with col2:
            st.write("#### Person 2 (Partner/Peer)")
            name2_in = st.text_input("Second Person Full Name:", key="n2")
            date2_in = st.date_input("Second Person Birthday:", value=datetime(1988, 8, 18), key="d2")
            
        submit_comp = st.form_submit_button("Calculate Aligned Intersection Matrix ⚡", use_container_width=True)
        
    if submit_comp:
        if not name1_in.strip() or not name2_in.strip():
            st.warning("⚠️ Please provide full birth names for both profiles to trigger comparison.")
        else:
            d1_fmt = date1_in.strftime("%d/%m/%Y")
            d2_fmt = date2_in.strftime("%d/%m/%Y")
            
            with st.spinner("Weaving comparative data pathways..."):
                comp_output = generate_gemini_compatibility_reading(name1_in, d1_fmt, name2_in, d2_fmt, selected_language)
                st.session_state.comp_cache = comp_output

    if st.session_state.comp_cache:
        st.divider()
        st.write("### 🔮 CosmicVibe Unified Compatibility Assessment")
        st.markdown(st.session_state.comp_cache)

st.caption("Powered by Google Gemini 3.8 Flash & Your Custom Pythagorean Local Engine.")
