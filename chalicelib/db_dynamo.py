from logging import exception
import os

import boto3

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
        pass

    def update_item(self, item_id, **body):
        pass

    def delete_item(self, item_id):
        pass

    def get_all_items(self):
        pass
