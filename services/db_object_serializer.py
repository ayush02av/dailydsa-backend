def serialize(db_object) -> dict:
    return {c.name: getattr(db_object, c.name) for c in db_object.__table__.columns}