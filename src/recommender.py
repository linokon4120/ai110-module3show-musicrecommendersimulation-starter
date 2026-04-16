from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        # TODO: Implement recommendation logic
        return self.songs[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        # TODO: Implement explanation logic
        return "Explanation placeholder"

def load_songs(csv_path: str) -> List[Dict]:
    """Loads songs from a CSV file into a list of dictionaries."""
    import csv
    songs = []
    with open(csv_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            # Convert numerical fields to appropriate types
            row['id'] = int(row['id'])
            row['energy'] = float(row['energy'])
            row['tempo_bpm'] = float(row['tempo_bpm'])
            row['valence'] = float(row['valence'])
            row['danceability'] = float(row['danceability'])
            row['acousticness'] = float(row['acousticness'])
            row['popularity'] = int(row['popularity'])
            row['artist_popularity'] = int(row['artist_popularity'])
            row['instrumental'] = float(row['instrumental'])
            songs.append(row)
    return songs

def score_song(user_prefs: Dict, song: Dict, mode: str = 'balanced') -> Tuple[float, List[str]]:
    """Scores a song based on user preferences and returns score with reasons."""
    score = 0.0
    reasons = []
    
    # Set weights based on mode
    if mode == 'genre_first':
        genre_w, mood_w, energy_w = 3.0, 1.0, 1.0
    elif mode == 'mood_first':
        genre_w, mood_w, energy_w = 1.0, 3.0, 1.0
    elif mode == 'energy_focused':
        genre_w, mood_w, energy_w = 1.0, 1.0, 3.0
    else:  # balanced
        genre_w, mood_w, energy_w = 1.0, 1.0, 2.0
    
    # Genre match
    if song['genre'] == user_prefs['genre']:
        score += genre_w
        reasons.append(f"genre match (+{genre_w})")
    
    # Mood match
    if song['mood'] == user_prefs['mood']:
        score += mood_w
        reasons.append(f"mood match (+{mood_w})")
    
    # Energy similarity
    energy_diff = abs(song['energy'] - user_prefs['energy'])
    energy_score = energy_w * (1.0 - energy_diff)
    score += energy_score
    reasons.append(f"energy closeness ({energy_score:.2f})")
    
    # Popularity bonus
    pop_bonus = (song['popularity'] / 100) * 0.5
    score += pop_bonus
    reasons.append(f"song popularity ({pop_bonus:.2f})")
    
    # Release decade match
    if song.get('release_decade') == user_prefs.get('preferred_decade'):
        score += 1.0
        reasons.append("decade match (+1.0)")
    
    # Detailed moods match
    if 'detailed_moods' in song:
        moods = song['detailed_moods'].split(',')
        if user_prefs['mood'] in moods:
            score += 0.5
            reasons.append("detailed mood match (+0.5)")
    
    # Artist popularity bonus
    artist_bonus = (song['artist_popularity'] / 100) * 0.3
    score += artist_bonus
    reasons.append(f"artist popularity ({artist_bonus:.2f})")
    
    # Instrumental preference
    if user_prefs.get('prefers_instrumental', False) and song.get('instrumental', 0) > 0.5:
        score += 0.5
        reasons.append("instrumental match (+0.5)")
    
    return score, reasons

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5, mode: str = 'balanced') -> List[Tuple[Dict, float, str]]:
    """Recommends top k songs based on scoring and ranking."""
    scored_songs = []
    for song in songs:
        score, reasons = score_song(user_prefs, song, mode)
        explanation = ", ".join(reasons)
        scored_songs.append((song, score, explanation))
    
    # Sort by score descending
    scored_songs.sort(key=lambda x: x[1], reverse=True)
    
    # Return top k
    return scored_songs[:k]
