#!/usr/bin/env python3
import re
import os

CHAPTERS_DIR = '/Users/csv610/Projects/MyBooks/SpaceDict/chapters'

# Terms that appear in multiple chapters - keep the one in parentheses
# Format: "Term": ("keep_chapter", "remove_chapters")
DUPLICATES = {
    # Regulatory - keep in Aerospace
    "FAA": ("chapter2_aerospace.tex", ["chapter4_drones.tex"]),
    "EASA": ("chapter2_aerospace.tex", ["chapter4_drones.tex"]),
    "ICAO": ("chapter2_aerospace.tex", ["chapter4_drones.tex"]),
    "UAS": ("chapter2_aerospace.tex", ["chapter4_drones.tex"]),
    "UAV": ("chapter2_aerospace.tex", ["chapter4_drones.tex"]),
    
    # Sustainable fuel - keep in Aerospace
    "Sustainable Aviation Fuel": ("chapter2_aerospace.tex", ["chapter1_aerodynamics.tex"]),
    
    # Engine types - keep in Aerospace
    "Turbofan": ("chapter2_aerospace.tex", ["chapter1_aerodynamics.tex"]),
    "Turbojet": ("chapter2_aerospace.tex", ["chapter1_aerodynamics.tex"]),
    
    # Heat Shield - keep in Aerospace (more detailed)
    "Heat Shield": ("chapter2_aerospace.tex", ["chapter1_aerodynamics.tex"]),
    
    # Insulation - keep in Rocket (more detailed)
    "Insulation": ("chapter3_rocket_missile.tex", ["chapter1_aerodynamics.tex"]),
    
    # Accelerometer - keep in Aerodynamics (more detailed)
    "Accelerometer": ("chapter1_aerodynamics.tex", ["chapter4_drones.tex"]),
    
    # Gyroscope - keep in Space Science (more detailed)
    "Gyroscope": ("chapter5_spacescience.tex", ["chapter4_drones.tex"]),
    
    # Magnetometer - keep in Space Science (more detailed)
    "Magnetometer": ("chapter5_spacescience.tex", ["chapter4_drones.tex"]),
    
    # Thrust Vector Control - keep in Rocket
    "Thrust Vector Control": ("chapter3_rocket_missile.tex", ["chapter1_aerodynamics.tex", "chapter2_aerospace.tex"]),
    
    # Solar Panel - keep in Space Science
    "Solar Panel": ("chapter5_spacescience.tex", ["chapter2_aerospace.tex"]),
    
    # Solar Wind - keep in Space Science
    "Solar Wind": ("chapter5_spacescience.tex", ["chapter2_aerospace.tex"]),
    
    # Satellite - keep in Space Science
    "Satellite": ("chapter5_spacescience.tex", ["chapter2_aerospace.tex", "chapter3_rocket_missile.tex"]),
    
    # Spacecraft - keep in Space Science
    "Spacecraft": ("chapter5_spacescience.tex", ["chapter2_aerospace.tex"]),
    
    # Launch Pad - keep in Rocket
    "Launch Pad": ("chapter3_rocket_missile.tex", ["chapter5_spacescience.tex"]),
    
    # Range Safety - keep in Rocket
    "Range Safety": ("chapter3_rocket_missile.tex", ["chapter2_aerospace.tex"]),
    
    # Upper Stage - keep in Rocket
    "Upper Stage": ("chapter3_rocket_missile.tex", ["chapter2_aerospace.tex"]),
    
    # Nozzle - keep in Rocket (most detailed)
    "Nozzle": ("chapter3_rocket_missile.tex", ["chapter1_aerodynamics.tex"]),
    
    # Thrust - keep in Rocket (more detailed)
    "Thrust": ("chapter3_rocket_missile.tex", ["chapter1_aerodynamics.tex", "chapter2_aerospace.tex"]),
    
    # Upper Stage - keep in Rocket
    "Upper Stage": ("chapter3_rocket_missile.tex", ["chapter2_aerospace.tex"]),
    
    # Heat Shield - keep in Aerospace
    "Heat Shield": ("chapter2_aerospace.tex", ["chapter1_aerodynamics.tex"]),
}

def remove_term_from_chapter(term, chapter_file):
    """Remove a dictentry for term from chapter_file"""
    filepath = os.path.join(CHAPTERS_DIR, chapter_file)
    with open(filepath, 'r') as f:
        content = f.read()
    
    # Pattern to match the dictentry for this term
    # Escape special regex chars in term
    escaped_term = re.escape(term)
    pattern = rf'\\dictentry\{{{escaped_term}\}}[^{{]*\{{cat[A-Z]{{2}}\}}'
    
    new_content = re.sub(pattern, '', content, count=1, flags=re.DOTALL)
    
    if new_content != content:
        with open(filepath, 'w') as f:
            f.write(new_content)
        print(f"  Removed '{term}' from {chapter_file}")
        return True
    else:
        print(f"  NOT FOUND: '{term}' in {chapter_file}")
        return False

def main():
    for term, (keep_chapter, remove_chapters) in DUPLICATES.items():
        print(f"\nProcessing: {term}")
        for rc in remove_chapters:
            remove_term_from_chapter(term, rc)
    
    print("\nDone!")

if __name__ == '__main__':
    main()