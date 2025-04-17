import sqlite3
import random

def create_playlists():
    conn = sqlite3.connect('./data/database.db')
    cursor = conn.cursor()
    
    # Get all song IDs
    cursor.execute("SELECT id FROM songs")
    all_song_ids = [row[0] for row in cursor.fetchall()]
    
    # Create 10 playlists
    playlist_names = [
        "My Favorites",
        "Workout Mix",
        "Chill Vibes",
        "Party Hits",
        "Road Trip",
        "Study Time",
        "Morning Coffee",
        "Evening Relaxation",
        "Dance Party",
        "Throwback Hits"
    ]
    
    user_id = 2  # Do Minh Tuong's user ID
    
    for playlist_name in playlist_names:
        # Add 5 random songs to each playlist
        random_song_ids = random.sample(all_song_ids, min(5, len(all_song_ids)))
        for song_id in random_song_ids:
            # Get song details
            cursor.execute('''
                SELECT name, image_path, file_path 
                FROM songs 
                WHERE id = ?
            ''', (song_id,))
            song = cursor.fetchone()
            
            if song:
                cursor.execute('''
                    INSERT INTO playlists (name, song_id, user_id, song_name, image_path, file_path)
                    VALUES (?, ?, ?, ?, ?, ?)
                ''', (playlist_name, song_id, user_id, song[0], song[1], song[2]))
    
    conn.commit()
    conn.close()
    print("Successfully created 10 playlists with songs!")

if __name__ == "__main__":
    create_playlists() 