from chalicelib.crud import CRUD

DB = None


def get_db():
    global DB
    if not DB:
        DB = LocalDB()
    return DB


class LocalDB(CRUD):
    pass
