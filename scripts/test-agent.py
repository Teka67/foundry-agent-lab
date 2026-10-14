import json

with open("test/request.json", "r", encoding="utf-8") as file:
    request = json.load(file)

print("PMS Request:")
print(request)

print("\nTitle:")
print(request["title"])
