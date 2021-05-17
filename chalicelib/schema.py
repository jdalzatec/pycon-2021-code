SCHEMA = {
    "description": {"type": "string"},
    "id": {"type": "string"},
    "state": {"type": "string", "allowed": ["unstarted", "started", "completed"]},
    "due_date": {"type": "datetime", "nullable": True},
}
