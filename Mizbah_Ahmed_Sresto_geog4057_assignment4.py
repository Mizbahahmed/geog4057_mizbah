# %%
# Q1 County name list
counties = ['East Baton Rouge', 'Jefferson', 'Orleans', 'St. Tammany', 'Lafayette']
print("Length of the list:", len(counties))
print("County names:")
for county in counties:
    print(county)

# %%
# Q2 County population dictionary
county_pop = {
    'East Baton Rouge': 456781,
    'Jefferson': 432552,
    'Orleans': 389617,
    'St. Tammany': 264570,
    'Lafayette': 245398
}
print("Largest population (East Baton Rouge):", county_pop['East Baton Rouge'])
print("Smallest population (Lafayette):", county_pop['Lafayette'])
total_pop = 0
for county in county_pop:
    total_pop += county_pop[county]
print("Total population from loop:", total_pop)

# %%
# Q3 String formatting
for county, pop in county_pop.items():
    print(f"{county} has a population of {pop}")

# %% [markdown]
# 

# %%
# Q4 Shape file names
shapefiles = [county + '.shp' for county in counties]
print("Shapefile names:", shapefiles)

# %%
# Q5 Full path names with os.path.join
import os
data_path = r"C:\Users\anany\Documents\data"  # Added 'r' for raw string
full_paths = []
for county in counties:
    full_path = os.path.join(data_path, f"{county}.shp")
    full_paths.append(full_path)
print("Full paths:", full_paths)

# %%
# Q6 Define countPopulation function
def countPopulation(pop_dict):
    """
    Compute the total populatoin of the counties in the dictionary
    GEOG 4057 GIS Programming
    """
    total = 0
    for county in pop_dict:
        total += pop_dict[county]
    return total

print("Function docstring:", countPopulation.__doc__)
print("Total population from function:", countPopulation(county_pop))


