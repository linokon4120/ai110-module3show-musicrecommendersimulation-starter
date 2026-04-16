# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

**VibeMatcher 1.0**  

---

## 2. Intended Use  

This recommender suggests 3-5 songs from a small catalog based on a user's preferred genre, mood, and energy level. It assumes users have clear vibe preferences and is designed for classroom exploration only, not for real users or production apps.  

---

## 3. How the Model Works  

The model scores songs by checking if the genre matches (+1 point), mood matches (+1 point), and how close the energy level is (doubled importance for closeness). It then ranks songs by total score to recommend the best matches.

---

## 4. Data  

The dataset has 18 songs with features like genre, mood, energy, valence, tempo, danceability, and acousticness. It's limited to a small catalog, mostly pop and lofi genres, which may not represent all musical tastes.  

---

## 5. Strengths  

The system works well for users with specific vibe preferences, correctly prioritizing exact matches and close energy levels. It provides clear explanations for why songs are recommended.  

---

## 6. Limitations and Bias 

The system struggles with small datasets, limiting variety and potentially overfitting to common genres like pop and lofi. After experimenting with weights, doubling energy importance made recommendations more accurate for energy-focused users but could unfairly prioritize high-energy songs, ignoring great low-energy matches. The scoring logic assumes categorical matches (genre/mood) are equally important for all users, which might not reflect diverse musical tastes. Biases exist toward songs with extreme energy values at the dataset edges, and the lack of diversity mechanisms can create filter bubbles where similar songs dominate recommendations.  

---

## 7. Evaluation  

I tested five user profiles: High-Energy Pop, Chill Lofi, Deep Intense Rock, an adversarial Pop/Chill/High-Energy mix, and an edge case with unknown genre (jazz). The results generally matched intuition—Chill Lofi favored low-energy lofi tracks, while High-Energy Pop prioritized intense pop songs. A surprise was how the adversarial profile still ranked pop songs first despite conflicting mood/energy, showing genre dominance. After doubling energy weight and halving genre, rankings shifted toward energy closeness, making results more accurate for energy-focused profiles but potentially less diverse.

Comparing profiles: High-Energy Pop vs. Chill Lofi shows energy as the key differentiator—high energy favors intense/motivational tracks, low energy shifts to relaxed/ambient ones. The adversarial profile demonstrates that genre wins over mood when they conflict, which makes sense for style-first preferences but could frustrate mood-focused users. Unknown genre profiles fall back to energy matches, proving the system handles missing data gracefully but relies heavily on numeric features.

---

## 8. Future Work  

- Add more songs and genres to the dataset for better variety  
- Include user feedback or interaction data for collaborative filtering  
- Implement diversity checks to avoid recommending too many similar songs  
- Add more features like lyrics or artist popularity  

---

## 9. Personal Reflection  

My biggest learning moment was realizing how simple scoring rules can create effective recommendations, but also how biases creep in from weight choices and small data. AI tools helped speed up coding and idea generation, but I double-checked math and logic manually to ensure accuracy. I was surprised that even basic algorithms "feel" like real recommendations when they match user vibes closely. Next, I'd add user interaction data and test with real people to see if the system holds up beyond simulations.  
