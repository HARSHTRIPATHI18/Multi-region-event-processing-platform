import json
import boto3

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("events")

def handler(event, context):
    detail = json.loads(event["detail"])

    table.put_item(
        Item={
            "event_id": detail["event_id"],
            "user_id": detail["user_id"],
            "event_type": detail["event_type"],
            "payload": detail["payload"],
            "created_at": detail["created_at"]
        }
    )
