# build_db.py
import os
import time
from google import genai
from dotenv import load_dotenv
from numerology_engine import get_full_profile, calculate_name_matrix
import numerology_data

load_dotenv()

# Native client initialization - pulls key automatically from backend environment variables
client = genai.Client()

def generate_gemini_numerology_reading(birth_date: str, full_name: str) -> str:
    """Calculates individual profile and generates an interpretation via Gemini 3.8 Flash."""
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
        f"--- PROFILE SUMMARY DATA ---\n"
        f"User Full Name: {full_name}\n"
        f"User Birthdate: {birth_date}\n\n"
        f"1. Ruling Number: {ruling_num} ({ruling_text})\n"
        f"2. Core Vocational Lanes: {vocation_text}\n"
        f"3. Expression/Destiny Number: {exp_num} ({exp_text})\n"
        f"4. Soul Urge/Heart Desire Number: {soul_num} ({soul_text})\n"
        f"5. Personality Number: {pers_num} ({pers_text})\n"
        f"Active Arrows: {', '.join(date_profile['arrows_present'])}\n"
        f"Absent Arrows: {', '.join(date_profile['arrows_absent'])}\n"
    )

    try:
        response = client.models.generate_content(
            model="gemini-3.8-flash",
            contents=f"Generate a comprehensive spiritual analysis:\n\n{facts_payload}",
            config=genai.types.GenerateContentConfig(
                system_instruction=(
                    "You are 'CosmicVibe', an expert spiritual guide trained in the "
                    "Pythagorean numerology system of Dr. David A. Phillips.\n\n"
                    "Organize the analysis cleanly using separate Markdown headings for: "
                    "Your Ruling Number, Your Structural Birth Chart Matrix, Your Destiny Expression, "
                    "Your Soul's Desire, Your Public Personality, and Your Aligned Vocations & Career Paths."
                ),
                temperature=0.7
            )
        )
        return response.text
    except Exception as e:
        return f"Gemini connection failed. Error Details: {e}"


# 👥 DUAL ENGINE COMPATIBILITY ORCHESTRATOR PIPELINE METHOD
def generate_gemini_compatibility_reading(name1: str, date1: str, name2: str, date2: str) -> str:
    """Computes dual metrics locally and triggers a unified structural relationship analysis via Gemini 3.8."""
    p1_date = get_full_profile(date1)
    p2_date = get_full_profile(date2)
    p1_name = calculate_name_matrix(name1)
    p2_name = calculate_name_matrix(name2)
    
    if "error" in p1_date or "error" in p2_date: return "⚠️ Error processing birthdate values."
    if "error" in p1_name or "error" in p2_name: return "⚠️ Error processing name matrix values."
    
    r1, r2 = p1_date["ruling_number"], p2_date["ruling_number"]
    e1, e2 = p1_name["expression"], p2_name["expression"]
    s1, s2 = p1_name["soul_urge"], p2_name["soul_urge"]
    
    # Clean up fractions like '22/4' to safely pull pure numeric strings for arithmetic reductions
    n1_clean = r1.split('/')[0]
    n2_clean = r2.split('/')[0]
    
    # FIXED: Safe explicit comparison blocks to remove structural math parser leaks
    try:
        diff = abs(int(n1_clean) - int(n2_clean))
        if diff == 0 or diff == 2 or diff == 4 or diff == 6:
            comp_type = "NATURAL"
        elif diff == 1 or diff == 3 or diff == 5:
            comp_type = "COMPLEMENT"
        else:
            comp_type = "CHALLENGE"
    except:
        comp_type = "NATURAL"
        
    baseline_verdict = numerology_data.COMPATIBILITY_MATRICES.get(comp_type, "General connection.")
    
    compatibility_payload = (
        f"--- ALIGNMENT PROFILE FOR RELATIONSHIP MATRIX ---\n"
        f"Person 1: {name1} (Birthdate: {date1})\n"
        f"- Ruling Number: {r1}\n- Expression: {e1}\n- Soul Urge: {s1}\n\n"
        f"Person 2: {name2} (Birthdate: {date2})\n"
        f"- Ruling Number: {r2}\n- Expression: {e2}\n- Soul Urge: {s2}\n\n"
        f"Local Engine Core Assessment Matrix Verdict: {baseline_verdict}\n"
    )

    try:
        response = client.models.generate_content(
            model="gemini-3.8-flash",
            contents=f"Please analyze the romantic or collaborative compatibility of this dual matrix profile:\n\n{compatibility_payload}",
            config=genai.types.GenerateContentConfig(
                system_instruction=(
                    "You are 'CosmicVibe', an expert relationship guide trained exclusively in "
                    "the Pythagorean spiritual systems of Dr. David A. Phillips.\n\n"
                    "CRITICAL INSTRUCTIONS:\n"
                    "1. Evaluate how their Ruling Numbers interact. Break down areas of natural flow or communication friction.\n"
                    "2. Examine their Soul Urges (Inner Desires) to map out their hidden heart connections.\n"
                    "3. Present the blueprint response with elegant Markdown layouts including headings for: "
                    "The Core Matrix Verdict, Spiritual Synergies, Evolutionary Growth Hurdles, and Your Relationship Action Plan.\n"
                    "4. Maintain an encouraging, clear, non-fatalistic, and inspiring tone throughout."
                ),
                temperature=0.7
            )
        )
        return response.text
    except Exception as e:
        return f"Gemini Compatibility Module Failed. Error Details: {e}"
