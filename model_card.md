# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

<!-- Give your model a short, descriptive name.  
Example: **VibeFinder 1.0**   -->
***Taste Tuner***

---

## 2. Intended Use  

<!-- Describe what your recommender is designed to do and who it is for. 

Prompts:  

- What kind of recommendations does it generate  
- What assumptions does it make about the user  
- Is this for real users or classroom exploration   -->

This model is designed to reccomend songs based on a user's preferences.

It assumes the user provides a favorite genre, mood, and preferred energy level.

The model currently is for classroom exploration, not designed for real users.

---

## 3. How the Model Works  

<!-- Explain your scoring approach in simple language.  

Prompts:  

- What features of each song are used (genre, energy, mood, etc.)  
- What user preferences are considered  
- How does the model turn those into a score  
- What changes did you make from the starter logic  

Avoid code here. Pretend you are explaining the idea to a friend who does not program. -->

The scoring for individual songs is based on genre, mood, and energy. 

1. When comparing the user's preference with the song, the genre and mood are either a "match" or a "mismatch"
    * matches increase points, mismatches do not
2. The song's energy level is compared to the user's preferred energy level. The closer it is, the more points are awarded
3. The final score repesents how closely a song matches a user's taste profile

A list of all songs are then individually scored, then ranked based on their scores. Songs with the highest scores are recommended first, and following reccomendations are the next highest, in decreasing order

---

## 4. Data  

<!-- Describe the dataset the model uses.  

Prompts:  

- How many songs are in the catalog  
- What genres or moods are represented  
- Did you add or remove data  
- Are there parts of musical taste missing in the dataset   -->

This model uses a small catalog of 18 songs in data/songs.csv.

The dataset includes a mix of genres and moods (for example pop, lofi, rock, ambient, and moods like happy, chill, intense, and focused), along with numeric attributes like energy.

I did not remove songs during this phase, and used the provided catalog for experimentation.

There are still major gaps in musical taste coverage, including limited genre depth, limited mood variety, and no personalization history across multiple listening sessions.

---

## 5. Strengths  

<!-- Where does your system seem to work well  

Prompts:  

- User types for which it gives reasonable results  
- Any patterns you think your scoring captures correctly  
- Cases where the recommendations matched your intuition   -->

The system works well when users have clear preferences for mood and energy, and when their genre input is close to a known label.

The typo-tolerant matching improved robustness for minor formatting differences and misspellings, especially around labels like lofi/lo-fi.

The ranking behavior generally matches intuition when one song has both category alignment and close energy.

---

## 6. Limitations and Bias 

<!-- Where the system struggles or behaves unfairly. 

Prompts:  

- Features it does not consider  
- Genres or moods that are underrepresented  
- Cases where the system overfits to one preference  
- Ways the scoring might unintentionally favor some users   -->

Energy is overdominant in the system. This may recommend songs that are complete mismatches in genre or mood, but have similar energy. Additionally, users that may have multiple genre preferences are excluded, as the model favors songs that are close to one energy and supresses the rest.

---


## 7. Evaluation  

<!-- How you checked whether the recommender behaved as expected. 

Prompts:  

- Which user profiles you tested  
- What you looked for in the recommendations  
- What surprised you  
- Any simple tests or comparisons you ran  

No need for numeric metrics unless you created some. -->

I've tested user profiles that have typos in the genre, and also profiles that have out-of-range energies. The typos in the genres completely mismatched, as the genre matching is entirely binary- either a match or a mismatch. I ran the profiles after incrementally tweaking the model, normalizing energy values, and attempting to detect similarity in genres that could be typos

---

## 8. Future Work  

<!-- Ideas for how you would improve the model next.  

Prompts:  

- Additional features or preferences  
- Better ways to explain recommendations  
- Improving diversity among the top results  
- Handling more complex user tastes   -->

My next step would be adding multi-preference support, so users can provide more than one preferred genre or mood.

I would also improve recommendation diversity by limiting repeated patterns in the top results, instead of always returning songs with very similar energy levels.

Another improvement would be better explainability text that explicitly shows how each weighted component contributed to the final score.

Finally, I would expand the scoring to include more features from the dataset (such as tempo or danceability) and compare whether that improves recommendation quality.

---

## 9. Personal Reflection  

<!-- A few sentences about your experience.  

Prompts:  

- What you learned about recommender systems  
- Something unexpected or interesting you discovered  
- How this changed the way you think about music recommendation apps -->

This project helped me understand how small design choices in scoring logic can strongly shape recommendation outcomes.

One thing I found interesting was how quickly rankings changed when I adjusted feature weights, even though the underlying dataset stayed the same.

It changed how I think about music recommendation apps because now I pay more attention to how systems might over-focus on one signal (like energy) and unintentionally narrow what users see.
