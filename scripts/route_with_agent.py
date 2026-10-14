from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient

endpoint = "https://terolampinen-3170-resource.services.ai.azure.com/api/projects/terolampinen-3170"
agent_name = "RequestTriageAgent"

import json

with open("test/request.json", "r", encoding="utf-8") as file:
    request = json.load(file)

user_message = request["title"]

with (
    DefaultAzureCredential() as credential,
    AIProjectClient(
        endpoint=endpoint,
        credential=credential,
        allow_preview=True,
    ) as project_client,
):
    # Bind the OpenAI client to the existing agent endpoint.
    openai_client = project_client.get_openai_client(agent_name=agent_name)

    # GitHub Copilot preview agents require a conversation for every Responses turn.
    conversation = openai_client.conversations.create()
    response = openai_client.responses.create(
        conversation=conversation.id,
        input=[{"role": "user", "content": user_message}],
    )

result = json.loads(response.output_text)

category = result["category"]

print()
print("Agent Classification")
print("-------------------")
print(category)

if category == "AccessRequest":
    queue_file = "queues/access_queue.json"

elif category == "HardwareRequest":
    queue_file = "queues/hardware_queue.json"

else:
    queue_file = "queues/incident_queue.json"

with open(queue_file, "r", encoding="utf-8") as file:
    queue = json.load(file)

queue.append(request)

with open(queue_file, "w", encoding="utf-8") as file:
    json.dump(queue, file, indent=2)

print()
print(f"Request routed to {queue_file}")
