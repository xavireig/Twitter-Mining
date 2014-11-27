import json
import csv
import sys

f = open(sys.argv[1])
data = json.load(f)
f.close()

for item in data:
    print item["user"]["id_str"]