from sqlalchemy import Column, INTEGER, String, Boolean, TIMESTAMP, text, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class PostModel(Base):
    __tablename__ = "posts"

    id = Column(INTEGER, nullable=False, primary_key=True)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    published = Column(Boolean, nullable= False, server_default="True")
    created_at = Column(TIMESTAMP(timezone=True), nullable= False, server_default=text('NOW()'))
    owner_id = Column(INTEGER, ForeignKey("users.id", ondelete="CASCADE"), nullable = False, )

    owner = relationship("UserModel")

class UserModel(Base):
    __tablename__ = "users"

    id = Column(INTEGER, primary_key = True, nullable = False)
    username = Column(String, nullable = False, unique = True)
    email = Column(String, nullable = False, unique = True)
    password = Column(String, nullable = False)
    created_at = Column(TIMESTAMP(timezone=True), nullable = False, server_default = text('now()'))


class VoteModel(Base):
    __tablename__ = "votes"

    post_id = Column(INTEGER, ForeignKey("posts.id", ondelete="CASCADE"), primary_key = True, nullable = False)
    user_id = Column(INTEGER, ForeignKey("users.id", ondelete="CASCADE"), primary_key = True, nullable = False)