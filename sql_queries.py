# DROP TABLES
drop = "DROP TABLE IF EXISTS "

songplay_table_drop = drop + "songplays"
user_table_drop = drop + "users"
song_table_drop = drop + "songs"
artist_table_drop = drop + "artists"
time_table_drop = drop + "times"

# CREATE TABLES
def create_table(table_name, table_attributes):
    """
    Creates table if not exists
    args:
        - table_name (str).
        - table_attributes (dict): {column_name: column_datatype}
    """
    columns_to_create = ""
    for column, dtype in table_attributes.items():
        columns_to_create += column + " " + dtype + ","

    return f"CREATE TABLE IF NOT EXISTS {table_name} ({columns_to_create[:-1]})"


songplay_table_create = create_table(
    "songplays",
    {
        "songplay_id": "SERIAL PRIMARY KEY NOT NULL",
        "start_time": "timestamp NOT NULL",
        "user_id": "int NOT NULL",
        "level": "varchar",
        "song_id": "varchar",
        "artist_id": "varchar",
        "session_id": "int",
        "location": "varchar",
        "user_agent": "varchar",
    },
)

user_table_create = create_table(
    "users",
    {
        "user_id": "int PRIMARY KEY NOT NULL",
        "first_name": "varchar",
        "last_name": "varchar",
        "gender": "varchar",
        "level": "varchar",
    },
)

song_table_create = create_table(
    "songs",
    {
        "song_id": "varchar PRIMARY KEY",
        "title": "varchar",
        "artist_id": "varchar NOT NULL",
        "year": "int",
        "duration": "numeric",
    },
)

artist_table_create = create_table(
    "artists",
    {
        "artist_id": "varchar PRIMARY KEY NOT NULL",
        "name": "varchar",
        "location": "varchar",
        "latitude": "numeric",
        "longitude": "numeric",
    },
)

time_table_create = create_table(
    "times",
    {
        "start_time": "timestamp PRIMARY KEY NOT NULL",
        "hour": "int",
        "day": "int",
        "week": "int",
        "month": "int",
        "year": "int",
        "weekday": "int",
    },
)
# INSERT RECORDS

songplay_table_insert = """INSERT INTO songplays (
  start_time, user_id, level, song_id, 
  artist_id, session_id, location, 
  user_agent
) 
VALUES 
  (%s, %s, %s, %s, %s, %s, %s, %s) ON CONFLICT DO NOTHING;

"""

user_table_insert = """INSERT INTO users (
  user_id, first_name, last_name, gender, 
  level
) 
VALUES 
  (%s,  %s, %s, %s, %s) ON CONFLICT(user_id) DO 
UPDATE 
SET 
  level = excluded.level;

"""

song_table_insert = """INSERT INTO songs (
  song_id, title, artist_id, year, duration
) 
VALUES 
  (%s, %s, %s, %s, %s) ON CONFLICT DO NOTHING;

"""

artist_table_insert = """INSERT INTO artists (
  artist_id, name, location, latitude, 
  longitude
) 
VALUES 
  ( %s, %s, %s, %s, %s) ON CONFLICT DO NOTHING;

"""


time_table_insert = """ INSERT INTO times (
  start_time, hour, day, week, month, 
  year, weekday
) 
VALUES 
  ( %s, %s, %s, %s, %s, %s, %s) ON CONFLICT DO NOTHING;

"""

# FIND SONGS

song_select = """
SELECT 
  songs.song_id, 
  artists.artist_id 
FROM 
  songs 
  JOIN artists ON songs.artist_id = artists.artist_id 
WHERE 
  songs.title = %s 
  AND artists.name = %s 
  AND songs.duration = %s
"""


# QUERY LISTS

create_table_queries = [
    songplay_table_create,
    user_table_create,
    song_table_create,
    artist_table_create,
    time_table_create,
]
drop_table_queries = [
    songplay_table_drop,
    user_table_drop,
    song_table_drop,
    artist_table_drop,
    time_table_drop,
]
