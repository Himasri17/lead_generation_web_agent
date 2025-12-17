from src.apollo_client import search_people

data = search_people(
    titles=["Director of Toxicology"],
    locations=["Boston"]
)

print(data)
