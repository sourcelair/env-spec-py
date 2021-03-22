lines = [
    "DEBUG: [0,1]= 1",
    "ENVIRONMENT: [production,staging,development]= development",
]
enumerated = enumerate(lines)

for line in enumerated:
    print(line[0])
