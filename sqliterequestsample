# Sample query function to find mods that co-occur with a user's current modpack using sqlite
def get_recommendations_for_modpack(modpack, cursor):
    # Placeholder for recommended mods with their co-occurrence counts
    recommendations = defaultdict(int)
    
    # Query for mods that co-occur with each mod in the user's modpack
    for mod in modpack:
        # Find the mod ID for the given mod name
        cursor.execute("SELECT id FROM mods WHERE name = ?", (mod,))
        mod_id_results = cursor.fetchone()
        if mod_id_results:
            mod_id = mod_id_results[0]

            # Find co-occurrences for this mod
            cursor.execute("""
                SELECT mod_id1, mod_id2, count
                FROM co_occurrences
                WHERE mod_id1 = ? OR mod_id2 = ?
            """, (mod_id, mod_id))

            # Tally co-occurrence counts for recommendations
            for mod_id1, mod_id2, count in cursor.fetchall():
                other_mod_id = mod_id2 if mod_id1 == mod_id else mod_id1
                recommendations[other_mod_id] += count
    
    # Filter out any mods that are already in the user's modpack
    modpack_mod_ids = {mod_id for mod, mod_id in modpack.items()}
    recommendations = {mod_id: count for mod_id, count in recommendations.items() if mod_id not in modpack_mod_ids}
    
    # Sort the recommendations by descending co-occurrence count
    sorted_recommendations = sorted(recommendations.items(), key=lambda item: item[1], reverse=True)
    
    # Convert mod IDs back to mod names
    recommended_mods = []
    for mod_id, _ in sorted_recommendations:
        cursor.execute("SELECT name FROM mods WHERE id = ?", (mod_id,))
        mod_name_results = cursor.fetchone()
        if mod_name_results:
            recommended_mods.append(mod_name_results[0])
    
    return recommended_mods

# Simulate recommendations for mockup modpack containing 'ModA' and 'ModC'
user_modpack = {'ModA': 1, 'ModC': 3}  # Using mock mod IDs based on previous insertions
recommendations = get_recommendations_for_modpack(user_modpack, cursor)

# Outputting the recommended mods
print(recommendations)
