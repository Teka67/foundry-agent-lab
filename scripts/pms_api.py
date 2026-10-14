import json

from flask import Flask
from flask import jsonify
from flask import request

from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient

app = Flask(__name__)

endpoint = "https://terolampinen-3170-resource.services.ai.azure.com/api/projects/terolampinen-3170"
agent_name = "RequestTriageAgent"


@app.route("/request", methods=["POST"])
def receive_request():

    data = request.json
    title = data["title"]

    with (
        DefaultAzureCredential() as credential,
        AIProjectClient(
            endpoint=endpoint,
            credential=credential,
            allow_preview=True,
        ) as project_client,
    ):

        openai_client = project_client.get_openai_client(
            agent_name=agent_name
        )

        conversation = openai_client.conversations.create()

        response = openai_client.responses.create(
            conversation=conversation.id,
            input=[
                {
                    "role": "user",
                    "content": title,
                }
            ],
        )

        print("Agent response:")
        print(response.output_text)

        result = json.loads(response.output_text)

        category = result["category"]

        if category == "AccessRequest":
            destination = "Access Queue"
        elif category == "HardwareRequest":
            destination = "Hardware Queue"
        elif category == "Incident":
            destination = "Incident Queue"
        else:
            destination = "Manual Review"

        request_id = data.get("request_id", "")
        requester = data.get("requestedBy", "")


        return jsonify(
            {
                "requestId": request_id,
                "requestedBy": requester,
                "category": result["category"],
                "priority": result["priority"],
                "destination": destination
            }
        )

if __name__ == "__main__":
    app.run(debug=True, port=5000)