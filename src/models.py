import enum
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean, ForeignKey, Enum, Table, Column
from sqlalchemy.orm import Mapped, mapped_column

db = SQLAlchemy()

class MediaType(enum.Enum):
    IMAGE = "image"
    VIDEO = "video"
    AUDIO = "audio"

class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(40), unique=True, nullable=False)
    firstname: Mapped[str] = mapped_column(String)
    lastname: Mapped[str] = mapped_column(String)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    comment = db.relationship('Comment')
    follower = db.relationship('Follower')


class Comment(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    comment_text: Mapped[str] = mapped_column(String)
    author_id: Mapped[int] = mapped_column(ForeignKey('user.id'), nullable=False)
    post_id: Mapped[int] = mapped_column(ForeignKey('post.id'), nullable=False) 

class Post(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('user.id'), nullable=False)  
    comment = db.relationship('Comment') 
    media = db.relationship('Media')

class Media(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    type: Mapped[MediaType] = mapped_column(Enum(MediaType))
    url: Mapped[str] = mapped_column(String)
    post_id: Mapped[int] = mapped_column(ForeignKey('post.id'), nullable=False)

follower = Table(
    "follower",
    db.metadata,
    Column("user_from_id", ForeignKey("user.id")),
    Column("user_to_id", ForeignKey("user.id"))
)


