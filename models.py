import uuid 
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import UUID

db = SQLAlchemy()

def gen_uuid():
    return str(uuid.uuid4())

class Topic(db.Model):
    __tablename__ = 'topics'
    
    id = db.Column(UUID(as_uuid=False), primary_key=True, default=gen_uuid)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.Text, nullable=False)
    parent_topic_id = db.Column(UUID(as_uuid=False), db.ForeignKey("topics.id"), nullable=True)
    created_at = db.Column(db.DateTime(timezone=True), server_default=db.func.now())

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "parent_topic_id": self.parent_topic_id,
            "created_at": self.created_at
        }
    
class Skill(db.Model):
    __tablename__ = 'skills'
    
    id = db.Column(UUID(as_uuid=False), primary_key=True, default=gen_uuid)
    name = db.Column(db.String, nullable=False)
    topic_id = db.Column(UUID(as_uuid=False), db.ForeignKey("topics.id", ondelete="CASCADE"), nullable=False)
    difficulty = db.Column(db.String, nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), server_default=db.func.now())

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "topic_id": self.topic_id,
            "difficulty": self.difficulty,
            "created_at": self.created_at
        }
