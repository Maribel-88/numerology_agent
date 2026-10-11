# numerology_data.py

RULING_NUMBERS = {
    "2": "Ruling Number 2 represents deep intuition, sensitivity, and a desire for harmony. You excel at mediation and supporting roles.",
    "3": "Ruling Number 3 focuses on the Mind Plane. You possess strong mental agility, memory, and a bright, critical intelligence.",
    "4": "Ruling Number 4 values practicality, organization, and building stable physical or structural foundations.",
    "5": "Ruling Number 5 sits at the center of the Soul Plane. It expresses an intense need for freedom, love, and artistic expression.",
    "6": "Ruling Number 6 rules creativity but carries the threat of deep worry, anxiety, and over-protectiveness when out of balance.",
    "7": "Ruling Number 7 represents the temple and sacrifice. Deep learning is acquired via real, practical experiences and life tests.",
    "8": "Ruling Number 8 signals independence and spiritual wisdom expressed directly through intuitive, loving actions.",
    "9": "Ruling Number 9 combines ambition and high idealism. It sits at the action end of the Mind Plane, driving deep responsibility.",
    "10": "Ruling Number 10 indicates a dynamic, highly adaptable individual with strong leadership potential or deep superficiality.",
    "11": "Ruling Number 11 is a highly spiritual vibration bringing enhanced intuition, sensitivity, and psychic potential.",
    "22/4": "The Master Number 22/4 is the 'Master Builder.' It holds immense physical capability guided by high spiritual vision."
}

VOCATIONS = {
    "2": "Diplomacy, mediation, administrative support, human resources, counseling, and fields requiring deep empathy without heavy commercial pressure.",
    "3": "Academia, professional writing, journalism, science, data analysis, planning, strategic management, and public speaking.",
    "4": "Architecture, structural engineering, accounting, operations management, construction, specialized trades, and organizational leadership.",
    "5": "Arts and entertainment, travel industries, sales, public relations, design, performance, and creative entrepreneurship.",
    "6": "Healing arts, medicine, nursing, teaching, humanitarian roles, home design, fine arts, and community management.",
    "7": "Research science, philosophy, law, legal analysis, teaching, spiritual guidance, and technical troubleshooting.",
    "8": "Independent business ownership, artistic direction, financial planning, independent consulting, and organizational oversight.",
    "9": "Public service, politics, global human rights work, structural philosophy, large-scale arts, and educational leadership.",
    "10": "Sales leadership, corporate executive roles, performance art, dynamic public-facing fields, and venture design.",
    "11": "Spiritual leadership, alternative medicine, deep psychology, inspiring cultural roles, and intuitive educational development.",
    "22/4": "Large-scale real estate development, infrastructure engineering, political leadership, institutional building, and global entrepreneurship."
}

PERSONAL_YEARS = {
    "1": "Year 1: New Beginnings and Pioneering Energy. A year of high adaptability, adjustments, planting fresh seeds, and initiating independent projects.",
    "2": "Year 2: Development, Cooperation, and Patience. A slower cycle focusing on building spiritual balance, emotional growth, and partnerships.",
    "3": "Year 3: Mental Expansion and Expression. The mind plane becomes highly active. Excellent for travel, studies, and creative communication projects.",
    "4": "Year 4: Stabilization and Foundation. A year to secure resources, organize your physical life, rest, and build long-term material stability.",
    "5": "Year 5: Freedom, Transition, and Dynamic Change. A central peak cycle that breaks old restrictions, heightens emotional desires, and brings sudden movements.",
    "6": "Year 6: Creativity, Domesticity, and Responsibility. Focus is directed onto home balance, artistic pursuits, family protection, and human service.",
    "7": "Year 7: Introspection, Personal Sacrifice, and Deep Teaching. A year designed for internal reflection, specialized learning, and absorbing wisdom from life tests.",
    "8": "Year 8: Spiritual Independence and Financial Power. A dynamic year of action, self-realization, and executing business strategies with absolute integrity.",
    "9": "Year 9: The Peak of Completion and Global Transformation. A massive transitional close to the 9-year cycle. Time to clear away the past and plan future horizons.",
    "11": "Year 11: Master Spiritual Awakening. A highly intuitive year bringing heightened sensitivity, prophetic insight, and inner illumination.",
    "22": "Year 22: Master Foundation Building. Massive practical capabilities match global ideals to manifest monumental physical structures."
}

EXPRESSION_NUMBERS = {
    "1": "Expression Number 1 signals a pioneering spirit. You are driven to lead, create independent pathways, and manifest unique ideas.",
    "2": "Expression Number 2 highlights cooperative qualities. Your natural lane is diplomacy, cultivating partnerships, and fostering teamwork.",
    "3": "Expression Number 3 radiates joyful expression. You excel in communication, creative arts, and uplifting others with mental vitality.",
    "4": "Expression Number 4 embodies dedicated manifestation. You bring order, solid structures, and trustworthy execution to any venture.",
    "5": "Expression Number 5 is a versatile catalyst. You thrive on change, exploration, progressive concepts, and sensory freedom.",
    "6": "Expression Number 6 is the caretaker archetype. You find your purpose in nurturing, creative artistry, domestic responsibility, and healing.",
    "7": "Expression Number 7 is the analytical seeker. You are meant to uncover inner truths, specialize in deep knowledge, and trust your inner voice.",
    "8": "Expression Number 8 commands material mastery. You are wired for executive leadership, financial responsibility, and balancing commercial power with ethics.",
    "9": "Expression Number 9 represents global humanitarianism. Your path centers on idealistic service, artistic completion, and broad social compassion.",
    "11": "Expression Number 11 is a master intuitive bridge. You bring spiritual insights down to earth, acting as an inspirational beacon.",
    "22": "Expression Number 22 is the master builder. You possess the practical grit to transform massive global visions into concrete reality."
}

SOUL_URGE_NUMBERS = {
    "1": "Your soul secretly craves absolute independence, personal achievement, and being number one in your chosen field.",
    "2": "Your soul longs for peace, gentle validation, unconditional love, and deep emotional companionship above all else.",
    "3": "Your inner self yearns for artistic expression, joyful presentation, wit, and space to share your mental inspirations.",
    "4": "Your heart finds comfort in absolute order, predictability, steady loyalty, and tangible physical foundations.",
    "5": "Your soul carries a deep hunger for adventure, frequent travel, unhindered freedom, and dynamic life shifts.",
    "6": "Your core desire is to look after loved ones, create a beautiful, harmonious home, and be appreciated for your protection.",
    "7": "Your innermost self seeks absolute silence, spiritual truth, intellectual perfection, and the answer to life's mysteries.",
    "8": "Your heart secretly desires structural authority, financial independence, status, and recognition for your executive capability.",
    "9": "Your soul is deeply fulfilled by selfless giving, universal consciousness, cosmic healing, and helping the greater human collective.",
    "11": "Your master soul vibration yearns for true spiritual enlightenment, psychic development, and sharing profound insights.",
    "22": "Your master soul yearns to orchestrate large-scale structural movements that change the physical infrastructure of society."
}

PERSONALITY_NUMBERS = {
    "1": "The world sees you as dominant, independent, confidence, and a clear self-starter who commands a room.",
    "2": "Others perceive you as reliable, gentle, diplomatic, modest, and a peaceful presence who works well behind the scenes.",
    "3": "You present as vibrant, charismatic, witty, charming, and highly expressive in social groups.",
    "4": "The public perceives you as serious, intensely organized, practical, industrious, and down-to-earth.",
    "5": "You appear to others as exciting, fashionable, physically engaging, adventurous, and dynamic.",
    "6": "You project an aura of warmth, maternal/paternal protection, domestic responsibility, and comforting advice.",
    "7": "The outside world views you as mysterious, quiet, aristocratic, introverted, and highly intellectual.",
    "8": "You project a powerful look of authority, success, capability, material competence, and executive strength.",
    "9": "Others see you as warm, highly generous, broad-minded, charismatic, and deeply philosophical or artistic."
}

ARROWS = {
    "Arrow of Plan": "Active Arrow of Plan (1-2-3): You possess a structured approach to life, excelling at planning and logical progression.",
    "Arrow of Frustration": "Arrow of Frustration (Missing 1-2-3): You are prone to feeling misunderstood or experiencing delays in your plans.",
    "Arrow of Will": "Active Arrow of Will (4-5-6): You exhibit remarkable persistence, drive, and stubborn determination to get things done.",
    "Arrow of Delays": "Arrow of Delays (Missing 4-5-6): You frequently encounter circumstantial stagnation, testing your patience.",
    "Arrow of Activity": "Active Arrow of Activity (7-8-9): You need constant physical action, travel, or engagement to feel fulfilled.",
    "Arrow of Passivity": "Arrow of Passivity (Missing 7-8-9): You lean towards an inner, quiet existence, sometimes struggling with motivation.",
    "Arrow of Determination": "Active Arrow of Determination (1-5-9): You show absolute resolve, grit, and resilience in overcoming life challenges.",
    "Arrow of Indecision": "Arrow of Indecision (Missing 1-5-9): You find yourself hesitating or stalling when major lifecycle choices surface.",
    "Arrow of Spiritual Openness": "Active Arrow of Spiritual Openness (3-5-7): You possess a natural spiritual connection, deep empathy, and philosophical balance.",
    "Arrow of Enquiring Mind": "Arrow of Enquiring Mind (Missing 3-5-7): You examine the world analytically, demanding facts over blind faith."
}

# Append this to the very bottom of numerology_data.py

COMPATIBILITY_MATRICES = {
    "NATURAL": "This connection represents a Natural Harmony vibration. Your core energetic fields slide together effortlessly, offering instant mutual understanding, shared evolutionary goals, and an easy flow of daily supportive energy.",
    "CHALLENGE": "This connection represents a Spiritual Growth Lesson. Your core matrices hold highly contrasting vibrations. While this creates intense immediate attraction, it is designed by your souls to spark deep patience, clear communication breakthroughs, and compromise.",
    "COMPLEMENT": "This connection represents a Complementary Matrix. You fill each other's empty chart planes. Where one person lacks structure or emotional focus, the other brings natural capability, making you an exceptionally powerful building team."
}

# Append this directly to the very bottom of numerology_data.py

LUCKY_COLORS = {
    "2": {"color": "Midnight Blue & Soft Silver", "hex": "#1e3a8a", "meaning": "Enhances your deep natural intuition, filters out emotional overstimulation, and anchors peace."},
    "3": {"color": "Bright Citron Yellow & Royal Purple", "hex": "#eab308", "meaning": "Fires up mental agility, expands self-expression, and clears creative blocks on the mind plane."},
    "4": {"color": "Forest Green & Terracotta Earth", "hex": "#15803d", "meaning": "Brings grounding energy, physical structural focus, stability, and organizational calm."},
    "5": {"color": "Neon Turquoise & Aquamarine", "hex": "#06b6d4", "meaning": "Resonates with freedom, creative flow, artistic adaptability, and smooth life transitions."},
    "6": {"color": "Crimson Ruby & Soft Rose", "hex": "#be123c", "meaning": "Stimulates the caretaker archetype, nurturing protection, domestic creativity, and unconditional love."},
    "7": {"color": "Amethyst Violet & Royal Purple", "hex": "#6d28d9", "meaning": "Deepens philosophical reflection, historical research clarity, and protects your spiritual energy field."},
    "8": {"color": "Polished Charcoal & Deep Gold", "hex": "#374151", "meaning": "Commands executive authority, commercial material competence, independent power, and ethical balance."},
    "9": {"color": "Brilliant Scarlet & Pure White", "hex": "#dc2626", "meaning": "Ignites global humanitarian ambition, broad-minded social idealism, and drives deep responsibility."},
    "10": {"color": "Sunfire Orange & Gold", "hex": "#ea580c", "meaning": "Amplifies your dynamic adaptability, leadership potential, and highly charismatic social presence."},
    "11": {"color": "Iridescent Pearl & Pure Violet", "hex": "#a855f7", "meaning": "Channels master spiritual illumination, cosmic psychic sensitivity, and keeps your aura grounded."},
    "22/4": {"color": "Deep Emerald & Platinum", "hex": "#047857", "meaning": "The Master Builder vibration. Supports the practical grid strength needed to materialize monumental global infrastructure visions."}
}
