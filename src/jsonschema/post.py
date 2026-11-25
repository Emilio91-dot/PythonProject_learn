"""JSON Schema для проверки учебных объектов публикации."""

POST_SCHEMA = {
    "type": "object",
    "properties": {
        "id": {"type": "number"},
        "title": {"type": "string"},
    },
    "required": ["id"],
}
