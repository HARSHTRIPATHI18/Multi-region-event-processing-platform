import json
import boto3
import uuid
from datetime import datetime

eventbridge = boto3.client("events")

def handler(event, context):
    body = json.loads(event["body"])

    event_detail = {
        "event_id": str(uuid.uuid4()),
        "user_id": body["user_id"],
        "event_type": body["event_type"],
        "payload": body.get("payload", {}),
        "created_at": datetime.utcnow().isoformat()
    }

    eventbridge.put_events(
        Entries=[{
            "Source": "app.events",
            "DetailType": body["event_type"],
            "Detail": json.dumps(event_detail),
            "EventBusName": "default"
        }]
    )

    return {
        "statusCode": 202,
        "body": json.dumps({"status": "accepted"})
    }
