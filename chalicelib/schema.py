from uuid import uuid4

SCHEMA = {
    "description": {"required": True, "type": "string"},
    "id": {"type": "string", "default_setter": lambda _: str(uuid4())},
    "state": {
        "type": "string",
        "allowed": ["uncompleted", "completed"],
        "default": "uncompleted",
    },
    "due_date": {"type": "datetime", "nullable": True, "default": None},
}
