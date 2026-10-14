import json

# Lue PMS-pyyntö

with open('test/request.json', 'r',encoding="utf-8") as file:
    request = json.load(file)

title = request["title"]

print(f"Request: {title}")

# Simuloidaan agnetin vastaus

if "access" in title.lower():
    category = "AccessRequest"
elif "laptop" in title.lower():
    category = "HardwareRequest"
else:
    category = "Incident"

print (f"Category: {category}")

# Valitaan oikea jono

if category == "AccessRequest":
    queue_file = "queues/access_queue.json"
elif category == "HardwareRequest":
    queue_file = "queues/hardware_queue.json"
else:
    queue_file = "queues/incident_queue.json"

# Luetaan jono

with open(queue_file, 'r',encoding="utf-8") as file:
    queue = json.load(file)

# Lisää pyyntö

queue.append(request)

# Tallennetaan

with open(queue_file, 'w',encoding="utf-8") as file:
    json.dump(queue, file, indent=2)

print("")
print(f"Request added to {queue_file}")
