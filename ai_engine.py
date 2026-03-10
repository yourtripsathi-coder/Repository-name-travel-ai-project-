import pandas as pd

data = pd.read_csv("world_places.csv")

month = input("Enter travel month: ")
travel_type = input("Family, Couple or Both: ")

results = []

for index, row in data.iterrows():

    score = 0

    # month matching
    if month in row["best_months"]:
        score += 10

    # travel type match
    if travel_type == row["travel_for"] or row["travel_for"] == "Both":
        score += 8

    # weather score
    score += row["weather_score"]

    # crowd scoring
    if row["crowd"] == "Low":
        score += 6
    elif row["crowd"] == "Medium":
        score += 4
    else:
        score += 2

    results.append((row["place"], row["country"], score))

results.sort(key=lambda x: x[2], reverse=True)

print("\nTop travel recommendations:\n")

for r in results[:5]:
    print(r[0], "-", r[1], "Score:", r[2])