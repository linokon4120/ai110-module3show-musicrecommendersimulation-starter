"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from .recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv") 
    print(f"Loaded songs: {len(songs)}")

    # Diverse profiles for stress testing
    profiles = [
        {"name": "High-Energy Pop (Balanced)", "genre": "pop", "mood": "intense", "energy": 0.9, "mode": "balanced"},
        {"name": "Chill Lofi (Genre-First)", "genre": "lofi", "mood": "chill", "energy": 0.4, "mode": "genre_first"},
        {"name": "Deep Intense Rock (Mood-First)", "genre": "rock", "mood": "intense", "energy": 0.9, "mode": "mood_first"},
        {"name": "Adversarial: Pop Chill High Energy (Energy-Focused)", "genre": "pop", "mood": "chill", "energy": 0.9, "mode": "energy_focused"},
        {"name": "Edge Case: Unknown Genre (Balanced)", "genre": "jazz", "mood": "relaxed", "energy": 0.5, "mode": "balanced"}
    ]

    for profile in profiles:
        print(f"\n--- Profile: {profile['name']} ---")
        user_prefs = {k: v for k, v in profile.items() if k not in ['name', 'mode']}
        mode = profile.get('mode', 'balanced')
        recommendations = recommend_songs(user_prefs, songs, k=5, mode=mode)

        print("Top recommendations:")
        for rec in recommendations:
            song, score, explanation = rec
            print(f"{song['title']} - Score: {score:.2f}")
            print(f"Because: {explanation}")
        print()


if __name__ == "__main__":
    main()
