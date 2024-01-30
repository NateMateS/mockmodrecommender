# This is a simplified mockup recommendation system using the dense (dictionary-based) co-occurrence matrix
import time
import random
from collections import defaultdict

# Generate mock modpacks data
def generate_mock_modpacks(num_modpacks, num_unique_mods, max_mods_per_pack):
    unique_mods = [f"Mod{chr(65+i)}" for i in range(num_unique_mods)]
    modpacks = []
    for _ in range(num_modpacks):
        num_mods = random.randint(1, max_mods_per_pack)
        modpack = random.sample(unique_mods, num_mods)
        modpacks.append(modpack)
    return modpacks

# Function to create the co-occurrence matrix
def create_co_occurrence_matrix(modpacks):
    mod_co_occurrence = defaultdict(lambda: defaultdict(int))

    # Iterate through each modpack
    for pack in modpacks:
        # Iterate through each pair of mods in the modpack
        for i in range(len(pack)):
            for j in range(i, len(pack)):
                mod1, mod2 = pack[i], pack[j]
                mod_co_occurrence[mod1][mod2] += 1
                
                if mod1 != mod2:
                    mod_co_occurrence[mod2][mod1] += 1

    return mod_co_occurrence

# Generate a larger number of mock modpacks
num_modpacks = 100  # Total number of modpacks
num_unique_mods = 200  # Total number of unique mods
max_mods_per_pack = 50  # Maximum number of mods in a modpack

# Generate mock modpacks
start_time = time.time()
mock_modpacks = generate_mock_modpacks(num_modpacks, num_unique_mods, max_mods_per_pack)
end_time = time.time()
print(f"Mock modpacks generated in {end_time - start_time} seconds.")

# Timing the execution of creating the co-occurrence matrix
start_time = time.time()
co_occurrence_matrix = create_co_occurrence_matrix(mock_modpacks)
end_time = time.time()

# Report the performance
performance_time = end_time - start_time
print(f"Co-occurrence matrix created in {performance_time} seconds.")

# Assigning of mock categories to mock mods
def create_mock_categories(mod_co_occurrence):
    # Assign arbitrary categories to mods
    categories = ['Adventure', 'Technology', 'Magic', 'Decoration']
    mod_categories = {}
    
    for mod in mod_co_occurrence:
        # Assign random categories to mods for this example
        mod_categories[mod] = random.choice(categories)
    
    return mod_categories

# Implementation of diverse recommendations in the recommendations
def recommend_mods_with_culling(current_modpack, co_occurrence_matrix, mod_categories, num_recommendations=5):
    # Keep track of scores for each mod
    mod_scores = defaultdict(int)
    recommended_categories = set()

    # Iterate over all mods in the current modpack
    for mod in current_modpack:
        related_mods = co_occurrence_matrix.get(mod, {})
        # Increment the score of each mod by the number of times it co-occurs with the current mod
        for related_mod, co_occurrences in related_mods.items():
            # Ignore mods that are already in the current modpack or in the same category as a selected recommendation
            if related_mod not in current_modpack and mod_categories[related_mod] not in recommended_categories:
                mod_scores[related_mod] += co_occurrences

    # Sort the mods by their score in descending order
    sorted_mods = sorted(mod_scores.items(), key=lambda x: x[1], reverse=True)
    
    # Generate the list of recommendations ensuring category diversity
    recommendations = []
    for mod, score in sorted_mods:
        if len(recommendations) >= num_recommendations:
            # Stop when we have enough recommendations
            break
        if mod_categories[mod] not in recommended_categories:
            # Add the mod to the recommendations and take note of its category
            recommendations.append(mod)
            recommended_categories.add(mod_categories[mod])
    
    return recommendations

# Create mock categories for each mod
mock_categories = create_mock_categories(co_occurrence_matrix)

# Simulating recommendations based on the specified mockup client request modpack with its mockup modlist
user_modpack_with_culling = ['ModA', 'ModC']
recommendations_with_culling = recommend_mods_with_culling(user_modpack_with_culling, co_occurrence_matrix, mock_categories)
print(recommendations_with_culling)

# Get the user preferences here, a simple mockup currently
def get_user_preferences(user):
    # For the sake of our example, we're hardcoding user preferences
    # In a real system, this would likely come from the user profile or past behavior
    user_preferences = {
        'User1': 'Adventure',
        'User2': 'Technology',
        'User3': 'Magic',
        'User4': 'Decoration'
    }
    return user_preferences.get(user, 'Adventure')

# Implementation of personalization of the recommendations
def recommend_mods_with_personalization(current_modpack, co_occurrence_matrix, mod_categories, user_preferences, user, num_recommendations=5):
    # Keep track of scores for each mod
    mod_scores = defaultdict(int)
    recommended_categories = set()
    preference_boost = 1.2  # This is an arbitrary boost factor for mods in preferred categories

    # Get the preferred category for the user
    preferred_category = get_user_preferences(user)

    # Iterate over all mods in the current modpack
    for mod in current_modpack:
        related_mods = co_occurrence_matrix.get(mod, {})
        # Increment the score of each mod by the number of times it co-occurs with the current mod
        for related_mod, co_occurrences in related_mods.items():
            if related_mod not in current_modpack:
                mod_score = co_occurrences
                # If the mod is in the preferred category, apply a boost
                if mod_categories[related_mod] == preferred_category:
                    mod_score *= preference_boost
                mod_scores[related_mod] += mod_score

    # Sort the mods by their score in descending order
    sorted_mods = sorted(mod_scores.items(), key=lambda x: x[1], reverse=True)
    
    # Generate the list of recommendations ensuring category diversity and now also considering user preferences
    recommendations = []
    for mod, score in sorted_mods:
        if len(recommendations) >= num_recommendations:
            # Stop when we have enough recommendations
            break
        if mod_categories[mod] not in recommended_categories:
            # Add the mod to the recommendations and take note of its category
            recommendations.append(mod)
            recommended_categories.add(mod_categories[mod])
    
    return recommendations

# Simulating recommendations for the specified mockup sample user
sample_user = 'User1'
personalized_recommendations = recommend_mods_with_personalization(user_modpack_with_culling, co_occurrence_matrix, mock_categories, get_user_preferences, sample_user)
print(personalized_recommendations)
