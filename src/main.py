"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv")
    print(f"Loaded songs: {len(songs)}")

    edge_case_profiles = [
        ("Baseline match", {"genre": "pop", "mood": "happy", "energy": 0.8}),
        ("Typo/variant genre", {"genre": "lo-fi", "mood": "chill", "energy": 0.30}),
        ("Unknown genre + unknown mood", {"genre": "metalcore", "mood": "hyped", "energy": 0.8}),
        ("Out-of-range high energy", {"genre": "rock", "mood": "intense", "energy": 1.8}),
        ("Out-of-range low energy", {"genre": "ambient", "mood": "chill", "energy": -0.4}),
    ]

    for label, profile in edge_case_profiles:
        print("======================================")
        recommendations = recommend_songs(profile, songs, k=5)
        print(f"\nProfile: {label} -> {profile}")
        print("Top recommendations:\n")

        for song, score, explanation in recommendations:
            print(f"{song['title']} - Score: {score:.2f}")
            print(f"Because: {explanation}")
            print("Compare:")
            print(f"  genre  -> user: {profile['genre']} | song: {song.get('genre', '')}")
            print(f"  mood   -> user: {profile['mood']} | song: {song.get('mood', '')}")
            print(
                f"  energy -> user: {float(profile['energy']):.2f} | song: {float(song.get('energy', 0.0)):.2f}"
            )
            print()
        print("======================================")


if __name__ == "__main__":
    main()
