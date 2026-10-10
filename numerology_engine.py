import re

# 1. Standard Birthdate Methods
def clean_date(date_str: str) -> str:
    return "".join(re.findall(r'\d', date_str))

def calculate_ruling_number(date_digits: str) -> str:
    total = sum(int(digit) for digit in date_digits)
    if total == 11 or total == 22:
        return "11" if total == 11 else "22/4"
    while total > 11:
        total = sum(int(d) for d in str(total))
        if total == 11:
            return "11"
    if total == 22:
        return "22/4"
    return str(total)

def generate_birth_chart(date_digits: str) -> dict:
    chart = {i: 0 for i in range(1, 10)}
    for digit in date_digits:
        num = int(digit)
        if 1 <= num <= 9:
            chart[num] += 1
    return chart

def analyze_arrows(chart: dict) -> dict:
    lines = {
        "1-2-3": "Arrow of Plan",
        "4-5-6": "Arrow of Will",
        "7-8-9": "Arrow of Activity",
        "1-5-9": "Arrow of Determination",
        "3-5-7": "Arrow of Spiritual Openness"
    }
    arrows_present = []
    arrows_absent = []
    for line, name in lines.items():
        digits = [int(x) for x in line.split('-')]
        presence = [chart[d] > 0 for d in digits]
        if all(presence):
            arrows_present.append(name)
        elif not any(presence):
            if name == "Arrow of Plan": arrows_absent.append("Arrow of Frustration")
            elif name == "Arrow of Will": arrows_absent.append("Arrow of Delays")
            elif name == "Arrow of Activity": arrows_absent.append("Arrow of Passivity")
            elif name == "Arrow of Determination": arrows_absent.append("Arrow of Indecision")
            elif name == "Arrow of Spiritual Openness": arrows_absent.append("Arrow of Enquiring Mind")
    return {"arrows_of_individuality": arrows_present, "arrows_of_emptiness": arrows_absent}

def get_full_profile(date_str: str) -> dict:
    digits = clean_date(date_str)
    if not digits:
        return {"error": "Invalid date format provided."}
    chart = generate_birth_chart(digits)
    arrows = analyze_arrows(chart)
    ruling_num = calculate_ruling_number(digits)
    return {
        "birthdate_digits": digits,
        "ruling_number": ruling_num,
        "birth_chart_grid": chart,
        "arrows_present": arrows["arrows_of_individuality"],
        "arrows_absent": arrows["arrows_of_emptiness"]
    }

# 2. NEW: Pythagorean Full Name Matrix Methods
PYTHAGOREAN_MAP = {
    'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9,
    'J': 1, 'K': 2, 'L': 3, 'M': 4, 'N': 5, 'O': 6, 'P': 7, 'Q': 8, 'R': 9,
    'S': 1, 'T': 2, 'U': 3, 'V': 4, 'W': 5, 'X': 6, 'Y': 7, 'Z': 8
}

def reduce_name_number(total: int) -> str:
    """Reduces name values while preserving Master Numbers 11 and 22."""
    if total == 11 or total == 22:
        return str(total)
    while total > 9:
        total = sum(int(d) for d in str(total))
        if total == 11 or total == 22:
            return str(total)
    return str(total)

def calculate_name_matrix(full_name: str) -> dict:
    """Calculates Expression, Soul Urge, and Personality values from a full name string."""
    clean_name = "".join(re.findall(r'[A-Z]', full_name.upper()))
    if not clean_name:
        return {"error": "Name contains no valid alphabetic characters."}
        
    vowels = "AEIOU"
    expression_total = 0
    soul_urge_total = 0
    personality_total = 0
    
    for char in clean_name:
        val = PYTHAGOREAN_MAP.get(char, 0)
        expression_total += val
        if char in vowels:
            soul_urge_total += val
        else:
            personality_total += val
            
    return {
        "expression": reduce_name_number(expression_total),
        "soul_urge": reduce_name_number(soul_urge_total),
        "personality": reduce_name_number(personality_total)
    }
