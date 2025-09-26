import time
import random
from gamedata import scenes, objects, adult_objects

happiness = 50
dependencies = {"Cigarettes": 0, "Alcohol": 0}

def slow_print(text, delay=0.03):
    for c in text:
        print(c, end='', flush=True)
        time.sleep(delay)
    print()

def load_art(filename):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return f"[Missing art: {filename}]"

def get_happiness_stage():
    if happiness <= 20:
        return "Despair"
    elif happiness <= 40:
        return "Depressed"
    elif happiness <= 60:
        return "Neutral"
    elif happiness <= 80:
        return "Meh"
    else:
        return "Worth Living"

def random_object_encounter(adult=False):
    global dependencies
    pool = adult_objects if adult else objects
    chance = 0.5 if adult else 0.3

    if random.random() < chance and pool:
        obj = random.choice(pool)
        if obj.get("art") is None and "art_file" in obj:
            obj["art"] = load_art(obj["art_file"])
        print(obj["art"])
        slow_print(f"You encounter {obj['name']}.")

        choice = input("Do you interact with it? (y/n) ").strip().lower()
        while choice not in ['y', 'n']:
            slow_print("Invalid choice. Please type 'y' or 'n'.")
            choice = input().strip().lower()

        if choice == 'y':
            if adult and obj["name"] in ["Cigarettes", "Alcohol"]:
                success_chance = 0.4
            else:
                success_chance = 0.7

            if random.random() < success_chance:
                impact = obj["impact"]
                if adult and obj["name"] in ["Smartphone", "Laptop", "Medicine"] and random.random() < 0.2:
                    impact = -abs(obj["impact"]) // 2
                    if obj["name"] == "Smartphone":
                        slow_print("You got distracted by notifications! Minor setback.")
                    elif obj["name"] == "Laptop":
                        slow_print("Work overload! Minor stress caused.")
                    else:
                        slow_print("Side effects! Minor setback.")
                else:
                    slow_print("The interaction had a positive effect.")
            else:
                impact = -abs(obj["impact"])
                if adult and "dependency" in obj:
                    dependencies[obj["name"]] += obj["dependency"]
                    dependencies[obj["name"]] = min(dependencies[obj["name"]], 10)
                    impact -= int(dependencies[obj["name"]] * 1.5)
                    slow_print("Addiction worsens! Your happiness drops.")
                else:
                    slow_print("The interaction backfired.")

            print(f"(Current Happiness: {happiness + impact}, Dependencies: {dependencies})\n")
            return impact
        else:
            slow_print("You ignored it. Nothing happens.")
    return 0

def random_life_event(adult=False):
    if adult:
        events = [
            ("You got sick for a while.", -10),
            ("You made a new supportive friend.", +8),
            ("You lost your job unexpectedly.", -15),
            ("You had the chance to travel abroad.", +12),
            ("You felt creative and drew something amazing.", +7)
        ]
    else:
        events = [
            ("You got a compliment from a teacher.", +5),
            ("You made a new friend at school.", +7),
            ("You scraped your knee while playing.", -3),
            ("You found a small treasure outdoors.", +4),
            ("You argued with a sibling.", -5)
        ]

    if random.random() < 0.3:
        event, effect = random.choice(events)
        slow_print(f"Life Event: {event}")
        print(f"(Current Happiness: {happiness + effect})\n")
        return effect
    return 0

def check_dependencies_for_ending(key):
    global dependencies, happiness
    if key in ["happy_family", "happy_alone"]:
        if dependencies["Cigarettes"] > 3 or dependencies["Alcohol"] > 3:
            slow_print("Your addictions sabotaged your relationships...")
            return "lonely_addiction"
    if key == "hope":
        if dependencies["Cigarettes"] > 2 or dependencies["Alcohol"] > 2:
            return "rehab"
        elif happiness <= 40:
            return "bittersweet"
    return key


def play_scene(key, adult=False):
    global happiness
    key = check_dependencies_for_ending(key)
    scene = scenes[key]
    print(scene["art"])
    slow_print(scene["text"])

    happiness += random_object_encounter(adult)
    happiness += random_life_event(adult=adult)
    happiness = max(0, min(100, happiness))
    print(f"Mental State: {get_happiness_stage()} (Happiness: {happiness})")
    print(f"Cigarettes Dependency: {dependencies['Cigarettes']}, Alcohol Dependency: {dependencies['Alcohol']}")
    print("\n" + "-"*40 + "\n")

    if not scene["choices"]:
        print("\n-- THE END --\n")
        slow_print(f"Final Happiness: {happiness}")
        slow_print(f"Cigarettes Dependency: {dependencies['Cigarettes']}")
        slow_print(f"Alcohol Dependency: {dependencies['Alcohol']}")
        if happiness > 70 and dependencies["Cigarettes"] <= 2 and dependencies["Alcohol"] <= 2:
            slow_print("You lived a fulfilling and happy life!")
        elif happiness > 40:
            slow_print("Life was average, with its ups and downs.")
        else:
            slow_print("Life was challenging, and you struggled along the way.")
        print("\nThanks for playing!\n")
        return

    for desc, next_key, happiness_change in scene["choices"]:
        slow_print(f"{desc}? (y/n)")
        choice = input().strip().lower()
        while choice not in ['y', 'n']:
            slow_print("Invalid choice. Please type 'y' or 'n'.")
            choice = input().strip().lower()
        if choice == 'y':
            happiness += happiness_change
            happiness = max(0, min(100, happiness))
            next_adult = next_key in [
                "adult_depression_choice", "happy_family", "happy_alone",
                "hope", "tragic", "bittersweet", "burnout", "rehab",
                "traveler", "creative", "lonely_addiction", "balanced"
            ]
            play_scene(next_key, adult=next_adult)
            return
    next_key = scene["choices"][0][1]
    play_scene(next_key, adult=adult)