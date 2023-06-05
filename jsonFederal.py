import json

# Federal Taxes 2022
federal2023 = {
    "bracket1" : [.10, 0, 11000],
    "bracket2" : [.12, 11001, 44725, 1100],
    "bracket3" : [.22, 44726, 95375, 5147],
    "bracket4" : [.24, 95376, 182100, 16290],
    "bracket5" : [.32, 182101, 231250, 37104],
    "bracket6" : [.35, 231251, 578125, 52832],
    "bracket7" : [.37, 578126, 174238.25]
}

federal = {"2023": federal2023}

# Serialize the Json Data
fed = json.dumps(federal, indent=4)

# Write to a file location
with open("federaltaxes.json", "w") as outfile:
    outfile.write(fed)