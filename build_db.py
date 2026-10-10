# build_db.py
import os
import time
from google import genai
from dotenv import load_dotenv
from numerology_engine import get_full_profile, calculate_name_matrix
import numerology_data

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
if api_key:
    api_key = api_key.strip("'\"")

client = genai.Client()

def generate_gemini_numerology_reading(birth_date: str, full_name: str) -> str:
    """Combines profile values and injects Dr. Phillips' vocation maps to generate an aligned report."""
    
    date_profile = get_full_profile(birth_date)
    name_profile = calculate_name_matrix(full_name)
    
    if "error" in date_profile: return date_profile["error"]
    if "error" in name_profile: return name_profile["error"]
    
    ruling_num = date_profile["ruling_number"]
    ruling_text = numerology_data.RULING_NUMBERS.get(ruling_num, "")
    vocation_text = numerology_data.VOCATIONS.get(ruling_num, "General professional fields.")
    
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
        f"Active Arrows: {', '.join(date_profile['arrows_present']) if date_profile['arrows_present'] else 'None'}\n"
        f"Absent Arrows: {', '.join(date_profile['arrows_absent']) if date_profile['arrows_absent'] else 'None'}\n"
    )

    print("🤖 Communicating with your Free Gemini 3.8 Persona Engine... Please wait...")

    max_retries = 3
    base_delay = 2 
    
    for attempt in range(max_retries):
        try:
            response = client.models.generate_content(
                model="gemini-3.8-flash",
                contents=f"Please generate a comprehensive spiritual analysis combining my name, birthdate, and career data:\n\n{facts_payload}",
                config=genai.types.GenerateContentConfig(
                    system_instruction=(
                        "You are 'CosmicVibe', an expert spiritual guide trained in the "
                        "Pythagorean numerology system of Dr. David A. Phillips.\n\n"
                        "INSTRUCTIONS:\n"
                        "1. Address the user directly using an empathetic, inspiring tone.\n"
                        "2. Do NOT alter any calculation figures provided to you. Treat them as absolute facts.\n"
                        "3. Organize the analysis cleanly using separate Markdown headings for: Your Ruling Number, Your Structural Birth Chart Matrix, Your Destiny Expression, Your Soul's Desire, Your Public Personality, and Your Aligned Vocations & Career Paths.\n"
                        "4. In the Vocation section, break down the specific professions and work styles recommended by Dr. Phillips based on their numbers."
                    ),
                    temperature=0.7
                )
            )
            return response.text
            
        except Exception as e:
            if "503" in str(e) or "UNAVAILABLE" in str(e):
                if attempt < max_retries - 1:
                    time.sleep(base_delay)
                    base_delay *= 2 
                    continue
            return f"Gemini connection failed. Error Details: {e}"
