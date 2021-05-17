from chalicelib.crud import CRUD

DB = None


def get_db():
    global DB
    if not DB:
        DB = LocalDB()
    return DB


class LocalDB(CRUD):
    def __init__(self):
        self.db = {}

    def add_item(self, **body):
        item_id = body["id"]
        self.db[item_id] = body
        return body

    def get_item(self, item_id):
        return self.db.get(item_id)

    def update_item(self, item_id, body):
        if self.db.get(item_id):
            self.db[item_id] = body
            return body

        return None

    def delete_item(self, item_id):
        if self.db.get(item_id):
            return self.db.pop(item_id)

        return None

    def get_all_items(self):
        return [value for _, value in self.db.items()]
