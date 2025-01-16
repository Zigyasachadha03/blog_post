from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Boolean, TIMESTAMP, text 
from app import Base

class PostModel(Base):
    __tablename__ = "posts"

    id = Column(Integer, nullable=False, primary_key=True)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    published = Column(Boolean, nullable= False, server_default="True")
    created_at = Column(TIMESTAMP(timezone=True), nullable= False, server_default=text('NOW()'))

