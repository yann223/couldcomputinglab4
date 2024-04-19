import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('user_score')




""" items = []
with open('data/items.json', 'r') as f:
    for row in f:
        items.append(json.loads(row))
# Batch writing item. Only one big query, cost less ans it's quicker
with table.batch_writer() as batch:
    for i in items:
        batch.put_item(i)
 """

"""
response = table.scan(
    Select='COUNT',
    ReturnConsumedCapacity='TOTAL',
)

print(response) """

""" username = "johnsonscott"
resp = table.query(
    Select='ALL_ATTRIBUTES',
    KeyConditionExpression="PK = :pk AND SK = :sk",
    ExpressionAttributeValues={
        ":pk": f"USER#{username}",
        ":sk": f"#METADATA#{username}",
    },
)
print(resp) """


""" id = "c9c3917e-30f3-4ba4-82c4-2e9a0e4d1cfd"
resp = table.query(
    Select='ALL_ATTRIBUTES',
    KeyConditionExpression="PK = :pk AND begins_with(SK, :sk)",
    ExpressionAttributeValues={
        ":pk": f"GAME#{id}",
        ":sk": "USER",
    },
)
print(resp) """


""" user = "kellercole"

resp = table.query(
    IndexName="InvertedIndex",
    KeyConditionExpression="SK = :sk AND begins_with(PK, :pk)",
    ExpressionAttributeValues={
        ":sk": f"USER#{user}",
        ":pk": "GAME#",
    },
)

print(resp) """

map = "Green Grasslands"

resp = table.query(
    IndexName="MapIndex",
    KeyConditionExpression="#map = :map",
    ExpressionAttributeValues={
        ":map": map,
    },
    ExpressionAttributeNames={ "#map": "map" },
)

print(resp)