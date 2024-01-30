# Re-establishing the database with the existing tables and schema
# Note that this step is not required in a real application where the database is persistent
conn = sqlite3.connect(':memory:')
cursor = conn.cursor()

# Recreate the tables we defined earlier
cursor.executescript("""
    CREATE TABLE categories (
        id INTEGER PRIMARY KEY,
        name TEXT UNIQUE NOT NULL
    );

    CREATE TABLE mods (
        id INTEGER PRIMARY KEY,
        name TEXT UNIQUE NOT NULL,
        category_id INTEGER,
        FOREIGN KEY (category_id) REFERENCES categories(id)
    );

    CREATE TABLE modpacks (
        id INTEGER PRIMARY KEY,
        name TEXT UNIQUE NOT NULL
    );

    CREATE TABLE co_occurrences (
        mod_id1 INTEGER,
        mod_id2 INTEGER,
        count INTEGER,
        FOREIGN KEY (mod_id1) REFERENCES mods(id),
        FOREIGN KEY (mod_id2) REFERENCES mods(id)
    );
""")

# Insert mock data into the 'categories' table
categories_data = [
    (1, 'Adventure'),
    (2, 'Technology'),
    (3, 'Magic'),
    (4, 'Decoration'),
]

cursor.executemany("INSERT INTO categories (id, name) VALUES (?, ?)", categories_data)

# Insert mock data into the 'mods' table
# For simplicity, we'll add five mods with assigned categories
mods_data = [
    (1, 'ModA', 1),
    (2, 'ModB', 2),
    (3, 'ModC', 3),
    (4, 'ModD', 4),
    (5, 'ModE', 1),
]

cursor.executemany("INSERT INTO mods (id, name, category_id) VALUES (?, ?, ?)", mods_data)

# Insert mock data into the 'co_occurrences' table
co_occurrences_data = [
    (1, 2, 10), # ModA and ModB co-occur 10 times
    (1, 3, 5),  # ModA and ModC co-occur 5 times
    (1, 4, 2),  # ModA and ModD co-occur 2 times
    (2, 3, 8),  # ModB and ModC co-occur 8 times
    (2, 4, 3),  # ModB and ModD co-occur 3 times
    # ... blah blah blah
]

cursor.executemany("INSERT INTO co_occurrences (mod_id1, mod_id2, count) VALUES (?, ?, ?)", co_occurrences_data)

# Query the database to ensure the data was inserted properly
cursor.execute("SELECT * FROM categories")
print("Categories:")
print(cursor.fetchall())

cursor.execute("SELECT * FROM mods")
print("Mods:")
print(cursor.fetchall())

cursor.execute("SELECT * FROM co_occurrences")
print("co_occurrences:")
print(cursor.fetchall())

# Committing the transactions
conn.commit()

# Output the results to verify that the data was inserted correctly
"Mock data for categories, mods, and co_occurance was inserted successfully"
