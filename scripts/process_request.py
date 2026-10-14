import json

with open("test/request.json", "r", encoding="utf-8") as file:
    request = json.load(file)

print("PMS Request")
print("-----------")
print(request)

title = request["title"]

if "access" in title.lower():
    category = "AccessRequest"
elif "laptop" in title.lower():
    category = "HardwareRequest"
else:
    category = "Unknown"

print()
print("Classification")
print("--------------")
print(category)

print()
print("Decision")
print("--------")

if category == "AccessRequest":
    print("Create access ticket")
elif category == "HardwareRequest":
    print("Send to IT hardware queue")
else:
    print("Manual review required")