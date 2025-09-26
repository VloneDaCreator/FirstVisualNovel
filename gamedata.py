from ascii_art import childhood_art, adulthood_art, hope_art, tragic_art, bittersweet_art, rehab_art, happy_family_art, happy_alone_art, burnout_art, traveler_art, creative_art, lonely_addiction_art, balanced_art

scenes = {
    "start": {
        "art": childhood_art,
        "text": "You are a boy with a warm childhood, surrounded by kindness.",
        "choices": [
            ("Talk to your mother", "mother_scene", +5),
            ("Talk to your father", "father_scene", +5),
            ("Play outside", "child_play", +0)
        ]
    },
    "child_play": {
        "art": childhood_art,
        "text": "You spend time exploring and playing.",
        "choices": [
            ("Continue", "teacher_scene", 0)
        ]
    },
    "teacher_scene": {
        "art": childhood_art,
        "text": "Teacher praises your effort.",
        "choices": [
            ("Listen carefully", "school_friend", +7),
            ("Ignore", "school_friend", -3)
        ]
    },
    "mother_scene": {
        "art": childhood_art,
        "text": "Your mother smiles warmly.",
        "choices": [
            ("Hug her", "school_friend", +10),
            ("Ignore her", "school_friend", -5)
        ]
    },
    "father_scene": {
        "art": childhood_art,
        "text": "Your father gives advice.",
        "choices": [
            ("Thank him", "school_friend", +10),
            ("Stay silent", "school_friend", -5)
        ]
    },
    "school_friend": {
        "art": childhood_art,
        "text": "Your friend waves at you.",
        "choices": [
            ("Join them", "first_crush", +5),
            ("Walk away", "first_crush", -5)
        ]
    },
    "first_crush": {
        "art": childhood_art,
        "text": "You meet your crush.",
        "choices": [
            ("Say yes", "teen_hobby", +10),
            ("Say no", "teen_hobby", -5)
        ]
    },
    "teen_hobby": {
        "art": childhood_art,
        "text": "You enjoy hobbies.",
        "choices": [
            ("Keep practicing", "first_job", +8),
            ("Quit early", "peer_pressure", -5)
        ]
    },
    "first_job": {
        "art": adulthood_art,
        "text": "You start your first job.",
        "choices": [
            ("Work hard", "adult_depression_choice", -5),
            ("Slack off", "adult_depression_choice", -10),
            ("Collapse", "burnout", -20),
            ("Balance hobbies", "adult_depression_choice", +5)
        ]
    },
    "peer_pressure": {
        "art": adulthood_art,
        "text": "Friends offer cigarettes or alcohol.",
        "choices": [
            ("Try it", "adult_depression_choice", -7),
            ("Refuse", "adult_depression_choice", +3)
        ]
    },
    "adult_depression_choice": {
        "art": adulthood_art,
        "text": "Decide how to live your life:",
        "choices": [
            ("Find a partner", "happy_family", -5),
            ("Focus on career", "happy_alone", -5),
            ("Therapy", "hope", +10),
            ("Travel", "traveler", +8),
            ("Create", "creative", +10),
            ("Seek balance", "balanced", +5)
        ]
    },
    "tragic": {"art": tragic_art, "text": "Ending: Tragic.", "choices": []},
    "hope": {"art": hope_art, "text": "Ending: Hopeful.", "choices": []},
    "bittersweet": {"art": bittersweet_art, "text": "Ending: Bittersweet.", "choices": []},
    "rehab": {"art": rehab_art, "text": "Ending: Rehab.", "choices": []},
    "happy_family": {"art": happy_family_art, "text": "Ending: Happy Family.", "choices": []},
    "happy_alone": {"art": happy_alone_art, "text": "Ending: Happy Alone.", "choices": []},
    "burnout": {"art": burnout_art, "text": "Ending: Burnout.", "choices": []},
    "traveler": {"art": traveler_art, "text": "Ending: Traveler.", "choices": []},
    "creative": {"art": creative_art, "text": "Ending: Creative Soul.", "choices": []},
    "lonely_addiction": {"art": lonely_addiction_art, "text": "Ending: Lonely Addiction.", "choices": []},
    "balanced": {"art": balanced_art, "text": "Ending: Balanced Life.", "choices": []},
}
