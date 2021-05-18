import os
from functools import reduce

import boto3
from boto3.dynamodb.conditions import Attr

from chalicelib.crud import CRUD

DB = None
dynamodb_resource = boto3.resource("dynamodb")


def get_db():
    global DB
    if not DB:
        DB = DynamoDB()
    return DB


class DynamoDB(CRUD):
    def __init__(self):
        self.table = dynamodb_resource.Table(os.environ["APP_TABLE_NAME"])

    def add_item(self, **body):
        try:
            self.table.put_item(
                Item=body,
                Expected={"id": {"Exists": False}},
            )
            return body
        except dynamodb_resource.meta.client.exceptions.ConditionalCheckFailedException:
            return None

    def get_item(self, item_id):
        response = self.table.get_item(Key={"id": item_id})
        return response.get("Item")

    def update_item(self, item_id, **body):
        try:
            body.pop("id", None)
            return self.table.update_item(
                Key={"id": item_id},
                AttributeUpdates={key: {"Value": value} for key, value in body.items()},
                Expected={"id": {"Value": item_id, "Exists": True}},
            )
        except dynamodb_resource.meta.client.exceptions.ConditionalCheckFailedException:
            return None

    def delete_item(self, item_id):
        try:
            return self.table.delete_item(
                Key={"id": item_id},
                Expected={"id": {"Value": item_id, "Exists": True}},
            )
        except dynamodb_resource.meta.client.exceptions.ConditionalCheckFailedException:
            return None

    def get_all_items(self, query={}):
        if query:
            attributes = [Attr(key).eq(value) for key, value in query.items()]
            filter_expression = reduce(lambda x, y: x & y, attributes)
            return self.table.scan(FilterExpression=filter_expression).get("Items")

        return self.table.scan().get("Items")
