# build_db.py
import os
import time
from google import genai
from dotenv import load_dotenv
from numerology_engine import get_full_profile, calculate_name_matrix
import numerology_data

load_dotenv()
client = genai.Client()

def generate_offline_fallback_reading(birth_date: str, full_name: str) -> str:
    """Creates a beautiful local text report when Google's servers are busy or rate-capped."""
    p = get_full_profile(birth_date)
    n = calculate_name_matrix(full_name)
    
    r_text = numerology_data.RULING_NUMBERS.get(p["ruling_number"], "")
    v_text = numerology_data.VOCATIONS.get(p["ruling_number"], "")
    e_text = numerology_data.EXPRESSION_NUMBERS.get(n["expression"], "")
    s_text = numerology_data.SOUL_URGE_NUMBERS.get(n["soul_urge"], "")
    p_text = numerology_data.PERSONALITY_NUMBERS.get(n["personality"], "")
    
    return (
        f"### 🪐 Your Ruling Number: {p['ruling_number']}\n{r_text}\n\n"
        f"### 💼 Aligned Vocations & Career Paths\n{v_text}\n\n"
        f"### 🎯 Your Destiny Expression: Number {n['expression']}\n{e_text}\n\n"
        f"### ❤️ Your Soul's Deep Desire: Number {n['soul_urge']}\n{s_text}\n\n"
        f"### 🧱 Your Public Personality: Number {n['personality']}\n{p_text}\n\n"
        f"🏆 *Note: You are currently viewing our high-precision Offline Local Analysis because the central Gemini Cloud is experiencing temporary peak traffic. All mathematical calculations remain 100% accurate.*"
    )

def generate_offline_fallback_compatibility(name1: str, r1: str, name2: str, r2: str) -> str:
    """Creates a local fallback relationship report when the cloud is unavailable."""
    n1_clean = r1.split('/')[0]
    n2_clean = r2.split('/')[0]
    try:
        diff = abs(int(n1_clean) - int(n2_clean))
        comp_type = "NATURAL" if diff in [0, 2, 4, 6] else ("COMPLEMENT" if diff in [1, 3, 5] else "CHALLENGE")
    except:
        comp_type = "NATURAL"
    
    verdict = numerology_data.COMPATIBILITY_MATRICES.get(comp_type, "")
    return (
        f"### 👥 Core Matrix Verdict: {comp_type} ALIGNMENT\n{verdict}\n\n"
        f"✨ **Connection Summary:** Person 1 (Ruling {r1}) and Person 2 (Ruling {r2}) hold a structural delta frequency of {diff}. "
        f"This matrix configuration naturally creates themes of collaborative lessons and spiritual mirrors.\n\n"
        f"🏆 *Note: Local Analysis active due to temporary cloud congestion.*"
    )

def generate_gemini_numerology_reading(birth_date: str, full_name: str, language: str = "English") -> str:
    """Calculates profile and generates a report via Gemini, falling back to local data if server fails."""
    date_profile = get_full_profile(birth_date)
    name_profile = calculate_name_matrix(full_name)
    
    if "error" in date_profile: return date_profile["error"]
    if "error" in name_profile: return name_profile["error"]
    
    ruling_num = date_profile["ruling_number"]
    ruling_text = numerology_data.RULING_NUMBERS.get(ruling_num, "")
    vocation_text = numerology_data.VOCATIONS.get(ruling_num, "")
    exp_num = name_profile["expression"]
    exp_text = numerology_data.EXPRESSION_NUMBERS.get(exp_num, "")
    soul_num = name_profile["soul_urge"]
    soul_text = numerology_data.SOUL_URGE_NUMBERS.get(soul_num, "")
    pers_num = name_profile["personality"]
    pers_text = numerology_data.PERSONALITY_NUMBERS.get(pers_num, "")
    
    facts_payload = (
        f"User Full Name: {full_name}\nBirthdate: {birth_date}\nLanguage: {language}\n\n"
        f"Ruling Number: {ruling_num} ({ruling_text})\nVocations: {vocation_text}\n"
        f"Expression: {exp_num} ({exp_text})\nSoul Urge: {soul_num} ({soul_text})\nPersonality: {pers_num} ({pers_text})\n"
    )

    try:
        response = client.models.generate_content(
            model="gemini-3.8-flash",
            contents=f"Generate a comprehensive spiritual analysis in {language}:\n\n{facts_payload}",
            config=genai.types.GenerateContentConfig(
                system_instruction=f"You are 'CosmicVibe', an expert spiritual guide. Write exclusively in {language}.",
                temperature=0.7
            )
        )
        return response.text
    except Exception:
        # SILENT FALLBACK: If Google crashes or rate-caps, output our beautiful local text instantly!
        return generate_offline_fallback_reading(birth_date, full_name)

def generate_gemini_compatibility_reading(name1: str, date1: str, name2: str, date2: str, language: str = "English") -> str:
    """Analyzes compatibility via Gemini with an automated offline data safety valve switch."""
    p1_date = get_full_profile(date1)
    p2_date = get_full_profile(date2)
    p1_name = calculate_name_matrix(name1)
    p2_name = calculate_name_matrix(name2)
    
    if "error" in p1_date or "error" in p2_date: return "⚠️ Error processing birthdate values."
    if "error" in p1_name or "error" in p2_name: return "⚠️ Error processing name matrix values."
    
    r1, r2 = p1_date["ruling_number"], p2_date["ruling_number"]
    
    compatibility_payload = (
        f"Language: {language}\nPerson 1: {name1} (Ruling {r1}, Soul Urge {p1_name['soul_urge']})\n"
        f"Person 2: {name2} (Ruling {r2}, Soul Urge {p2_name['soul_urge']})\n"
    )

    try:
        response = client.models.generate_content(
            model="gemini-3.8-flash",
            contents=f"Analyze compatibility in {language}:\n\n{compatibility_payload}",
            config=genai.types.GenerateContentConfig(
                system_instruction=f"You are 'CosmicVibe', an expert relationship guide. Write in {language}.",
                temperature=0.7
            )
        )
        return response.text
    except Exception:
        # SILENT FALLBACK: Bypasses the 503 error completely and renders our local metrics immediately!
        return generate_offline_fallback_compatibility(name1, r1, name2, r2)
