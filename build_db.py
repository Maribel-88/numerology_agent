# build_db.py
import os
import time
from google import genai
from dotenv import load_dotenv
from numerology_engine import get_full_profile, calculate_name_matrix
import numerology_data

load_dotenv()
client = genai.Client()

def generate_gemini_numerology_reading(birth_date: str, full_name: str, language: str = "English") -> str:
    """Calculates profile and instructs Gemini to generate a response in the user's targeted language."""
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
        f"User Birthdate: {birth_date}\n"
        f"Target Translation Language: {language}\n\n" # Injected language property
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
            contents=f"Generate a comprehensive spiritual analysis in {language}:\n\n{facts_payload}",
            config=genai.types.GenerateContentConfig(
                system_instruction=(
                    "You are 'CosmicVibe', an expert spiritual guide trained in the "
                    "Pythagorean numerology system of Dr. David A. Phillips.\n\n"
                    f"CRITICAL REQUIREMENT: You must write the entire analysis exclusively in the {language} language.\n\n"
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


def generate_gemini_compatibility_reading(name1: str, date1: str, name2: str, date2: str, language: str = "English") -> str:
    """Computes dual metrics locally and triggers a unified relationship analysis in the user's targeted language."""
    p1_date = get_full_profile(date1)
    p2_date = get_full_profile(date2)
    p1_name = calculate_name_matrix(name1)
    p2_name = calculate_name_matrix(name2)
    
    if "error" in p1_date or "error" in p2_date: return "⚠️ Error processing birthdate values."
    if "error" in p1_name or "error" in p2_name: return "⚠️ Error processing name matrix values."
    
    r1, r2 = p1_date["ruling_number"], p2_date["ruling_number"]
    e1, e2 = p1_name["expression"], p2_name["expression"]
    s1, s2 = p1_name["soul_urge"], p2_name["soul_urge"]
    
    n1_clean = r1.split('/')
    n2_clean = r2.split('/')
    
    try:
        diff = abs(int(n1_clean[0]) - int(n2_clean[0]))
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
        f"Target Translation Language: {language}\n\n" # Injected language property
        f"Person 1: {name1} (Birthdate: {date1})\n"
        f"- Ruling Number: {r1}\n- Expression: {e1}\n- Soul Urge: {s1}\n\n"
        f"Person 2: {name2} (Birthdate: {date2})\n"
        f"- Ruling Number: {r2}\n- Expression: {e2}\n- Soul Urge: {s2}\n\n"
        f"Local Engine Core Assessment Matrix Verdict: {baseline_verdict}\n"
    )

    try:
        response = client.models.generate_content(
            model="gemini-3.8-flash",
            contents=f"Please analyze the romantic or collaborative compatibility of this dual matrix profile in {language}:\n\n{compatibility_payload}",
            config=genai.types.GenerateContentConfig(
                system_instruction=(
                    "You are 'CosmicVibe', an expert relationship guide trained exclusively in "
                    "the Pythagorean spiritual systems of Dr. David A. Phillips.\n\n"
                    f"CRITICAL REQUIREMENT: You must write the entire analysis exclusively in the {language} language.\n\n"
                    "Present the blueprint response with elegant Markdown layouts including headings for: "
                    "The Core Matrix Verdict, Spiritual Synergies, Evolutionary Growth Hurdles, and Your Relationship Action Plan."
                ),
                temperature=0.7
            )
        )
        return response.text
    except Exception as e:
        return f"Gemini Compatibility Module Failed. Error Details: {e}"
