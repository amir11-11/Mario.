import csv, sys
if len(sys.argv) != 3: sys.exit("Usage: python dna.py database.csv sequence.txt")
db = list(csv.DictReader(open(sys.argv[1])))
seq = open(sys.argv[2]).read()
STRs = db[0].keys() - {"name"}
counts = {str: max((seq[i:i+len(str)] == str) * (c+1) or c for i in range(len(seq)) for c in range(100)) for str in STRs}
for person in db:
    if all(person[str] == str(counts[str]) for str in STRs):
        print(person["name"])
        sys.exit(0)
print("No match")