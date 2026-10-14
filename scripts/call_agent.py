# Before running the sample:
#    pip install "azure-ai-projects>=2.1.0"

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

    print(f"Response output: {response.output_text}")