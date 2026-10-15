import json

with open(
    "agents/RequestTriageAgent.json",
    "r",
    encoding="utf-8"
) as file:
    
    agent = json.load(file)

print(agent)