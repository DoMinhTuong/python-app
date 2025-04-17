import sqlite3

def remove_vietnamese_signs(text: str) -> str:
    # Replace Vietnamese characters with their non-accented equivalents
    replacements = {
        'àáạảãâầấậẩẫăằắặẳẵ': 'a',
        'ÀÁẠẢÃĂẰẮẶẲẴÂẦẤẬẨẪ': 'A', 
        'èéẹẻẽêềếệểễ': 'e',
        'ÈÉẸẺẼÊỀẾỆỂỄ': 'E',
        'òóọỏõôồốộổỗơờớợởỡ': 'o', 
        'ÒÓỌỎÕÔỒỐỘỔỖƠỜỚỢỞỠ': 'O',
        'ìíịỉĩ': 'i',
        'ÌÍỊỈĨ': 'I',
        'ùúụủũưừứựửữ': 'u',
        'ƯỪỨỰỬỮÙÚỤỦŨ': 'U',
        'ỳýỵỷỹ': 'y',
        'ỲÝỴỶỸ': 'Y',
        'đ': 'd',
        'Đ': 'D'
    }
    
    for vietnamese, latin in replacements.items():
        for char in vietnamese:
            text = text.replace(char, latin)
    return text

def build_alias(name: str) -> str:
    # Remove Vietnamese characters
    name = remove_vietnamese_signs(name)
    # Replace hyphens with spaces
    name = name.replace('-', ' ')
    # Convert to lowercase
    name = name.lower()
    # Trim spaces
    name = name.strip()
    # Replace spaces with hyphens
    name = name.replace(' ', '-')
    # Remove any characters that aren't a-z, 0-9, or hyphen
    name = ''.join(c for c in name if c.isalnum() or c == '-')
    # Replace multiple hyphens with single hyphen
    while '--' in name:
        name = name.replace('--', '-')
    return name

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

def create_user(email, name, password):
    conn = sqlite3.connect('./data/database.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO user (email, name, password) VALUES (?, ?, ?)', (email, name, password))
    conn.commit()
    conn.close()
    
def find_user_by_email(email):
    conn = sqlite3.connect('./data/database.db')
    cursor = conn .cursor()
    cursor.row_factory = dict_factory
    cursor.execute('SELECT id, email, name, password FROM user WHERE email = ?', (email,))
    user = cursor.fetchone()
    conn.commit()
    conn.close()
    return user

def find_user_by_email_and_password(email, password):
    conn = sqlite3.connect('./data/database.db')
    cursor = conn.cursor()
    cursor.row_factory = dict_factory
    cursor.execute('SELECT id, email, name, password FROM user WHERE email = ? AND password = ?', (email, password))
    user = cursor.fetchone()
    conn.commit()
    conn.close()
    return user

    
def get_songs_by_name(name):
    conn = sqlite3.connect('./data/database.db')
    conn.row_factory = dict_factory
    c = conn.cursor()
    alias = build_alias(name)
    query = f"SELECT id,name,album_name,artist_names,image_path,file_path FROM songs WHERE name LIKE '%{name}%' OR alias LIKE '%{alias}%'"
    c.execute(query)
    result = c.fetchall()
    conn.close()
    return result

def get_first_15_songs():
    conn = sqlite3.connect('./data/database.db')
    conn.row_factory = dict_factory
    c = conn.cursor()
    query = f"SELECT id,name,album_name,artist_names,image_path,file_path FROM songs LIMIT 15"
    c.execute(query)
    result = c.fetchall()
    conn.close()
    return result

def get_song_by_id(id):
    conn = sqlite3.connect('./data/database.db')
    conn.row_factory = dict_factory
    c = conn.cursor()
    query = f"SELECT id,name,album_name,artist_names,image_path,file_path FROM songs WHERE id = '{id}'"
    c.execute(query)
    result = c.fetchone()
    conn.close()
    return result

def create_playlists_table():
    conn = sqlite3.connect('./data/database.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS playlists (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            song_id INTEGER NOT NULL,
            user_id INTEGER NOT NULL,
            FOREIGN KEY (song_id) REFERENCES songs(id),
            FOREIGN KEY (user_id) REFERENCES users(id)
        )
    ''')
    conn.commit()
    conn.close()

def add_song_to_playlist(name, song_id, user_id):
    conn = sqlite3.connect('./data/database.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO playlists (name, song_id, user_id) VALUES (?, ?, ?)',
                  (name, song_id, user_id))
    conn.commit()
    conn.close()

def get_playlist_by_user_id(user_id):
    conn = sqlite3.connect('./data/database.db')
    cursor = conn.cursor()
    cursor.execute('''
        SELECT p.id, p.name, s.name as song_name, s.image_path, s.file_path
        FROM playlists p
        JOIN songs s ON p.song_id = s.id
        WHERE p.user_id = ?
    ''', (user_id,))
    playlists = cursor.fetchall()
    conn.close()
    return [{'id': p[0], 'name': p[1], 'song_name': p[2], 'image_path': p[3], 'file_path': p[4]} for p in playlists]

def delete_song_from_playlist(playlist_id):
    conn = sqlite3.connect('./data/database.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM playlists WHERE id = ?', (playlist_id,))
    conn.commit()
    conn.close()

def create_playlist(name, user_id):
    conn = sqlite3.connect('./data/database.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO playlists (name, user_id) VALUES (?, ?)',
                  (name, user_id))
    playlist_id = cursor.lastrowid
    conn.commit()
    conn.close()
    return playlist_id

def get_playlist_by_id(playlist_id):
    conn = sqlite3.connect('./data/database.db')
    conn.row_factory = dict_factory
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM playlists WHERE id = ?', (playlist_id,))
    playlist = cursor.fetchone()
    conn.close()
    return playlist

def update_playlist_name(playlist_id, new_name):
    conn = sqlite3.connect('./data/database.db')
    cursor = conn.cursor()
    cursor.execute('UPDATE playlists SET name = ? WHERE id = ?',
                  (new_name, playlist_id))
    conn.commit()
    conn.close()

def delete_playlist(playlist_id):
    conn = sqlite3.connect('./data/database.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM playlists WHERE id = ?', (playlist_id,))
    conn.commit()
    conn.close()

def get_playlist_songs(playlist_id):
    conn = sqlite3.connect('./data/database.db')
    conn.row_factory = dict_factory
    cursor = conn.cursor()
    cursor.execute('''
        SELECT s.id, s.name, s.artist_names, s.image_path, s.file_path
        FROM playlists p
        JOIN songs s ON p.song_id = s.id
        WHERE p.id = ?
    ''', (playlist_id,))
    songs = cursor.fetchall()
    conn.close()
    return songs

# Call this function when initializing the database
create_playlists_table()

#create_user('domintuong08@gmail.com', 'Do Minh Tuong', 567321)
# print(find_user_by_email('domintuong08@gmail.com'))
# print(find_user_by_email_and_password('domintuong08@gmail.com', '567321'))