import pandas as pd
from flask import Flask, render_template, request
from textblob import TextBlob
from config import CLIENT_ID, CLIENT_SECRET # Import credentials from config.py
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


# Load the musical sentiment dataset
df = pd.read_csv('Data/musical_sentiment.csv')

def normalize(value: float) -> float:
    """Normalize a value between -1 and 1 to 0 and 1."""
    return (value + 1) / 2

def select_songs_by_query(polarity: float, user_query: str) -> list:
    """
    Filters songs based on normalized polarity, genre, and emotional tags,
    and returns song metadata (track name, artist, Spotify link).
    """
    normalized_polarity = normalize(polarity)  # Normalize polarity to 0-1
    song_list = []

    # Debugging: Print polarity and user query
    print(f"User Query: {user_query} | Polarity: {polarity} | Normalized Polarity: {normalized_polarity}")

    # Filter by genre if the query matches a known genre
    genre_filtered = df[df['genre'].str.contains(user_query, case=False, na=False)]
    print(f"Songs matching genre '{user_query}': {len(genre_filtered)}")

    # Use the filtered dataset or fallback to the full dataset
    relevant_songs = genre_filtered if not genre_filtered.empty else df
    relevant_songs = relevant_songs.sample(frac=1).reset_index(drop=True)  # Shuffle

    # Debugging: Print total available songs
    print(f"Total songs available for selection: {len(relevant_songs)}")

    # Adjust proximity threshold for valence (increase threshold for more matches)
    for _, row in relevant_songs.iterrows():
        print(f"Checking song: {row['track']} | Valence: {row['valence_tags']} | Spotify ID: {row['spotify_id']}")
        
        # Adjust threshold to 0.4 for better matching
        if abs(row['valence_tags'] - normalized_polarity) <= 0.4:
            if pd.notnull(row['spotify_id']):  # Ensure valid Spotify ID
                song_data = {
                    'track': row['track'],
                    'artist': row['artist'],
                    'spotify_link': f"https://open.spotify.com/track/{row['spotify_id']}"
                }
                song_list.append(song_data)

            if len(song_list) >= 5:  # Stop after collecting 5 songs
                break

    # Fallback if less than 5 songs are found
    if len(song_list) < 5:
        print("⚠️ Not enough songs found! Expanding search...")
        remaining_songs = relevant_songs.sample(frac=1).reset_index(drop=True)
        for _, row in remaining_songs.iterrows():
            if pd.notnull(row['spotify_id']):  # Ensure valid Spotify ID
                song_data = {
                    'track': row['track'],
                    'artist': row['artist'],
                    'spotify_link': f"https://open.spotify.com/track/{row['spotify_id']}"
                }
                song_list.append(song_data)

            if len(song_list) >= 5:
                break

    # Debugging: Print final song list
    print(f"Final playlist (Total: {len(song_list)} songs): {[s['track'] for s in song_list]}")

    return song_list


@app.route("/")
def home():
    """Render the home page with the mood input form."""
    return render_template("index.html")


@app.route("/generate_playlist", methods=["POST"])
def generate_playlist():
    """Generate a playlist based on the user's mood input."""
    mood = request.form["mood"]
    try:
        analysis = TextBlob(mood)
        polarity = analysis.sentiment.polarity

        # Select songs based on polarity and user query
        playlist = select_songs_by_query(polarity, mood)

        # Pass the playlist with track and artist names to the template
        return render_template("playlist.html", mood=mood, playlist=playlist)
    
    except Exception as e:
        print(f"An error occurred: {e}")
        return render_template("playlist.html", mood=mood, playlist=[])


@app.route("/load_more_songs", methods=["POST"])
def load_more_songs():
    """Load 5 more songs based on the current mood."""
    mood = request.form["mood"]
    try:
        analysis = TextBlob(mood)
        polarity = analysis.sentiment.polarity

        # Select 5 more songs based on polarity and user query
        additional_songs = select_songs_by_query(polarity, mood)

        # Convert the additional songs to a JSON-friendly format
        additional_songs_json = [
            {
                "track": song["track"],
                "artist": song["artist"],
                "spotify_link": song["spotify_link"]
            }
            for song in additional_songs
        ]

        return jsonify(additional_songs_json)
    
    except Exception as e:
        print(f"An error occurred: {e}")
        return jsonify([])

if __name__ == "__main__":
    app.run(debug=True)


# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=5000)