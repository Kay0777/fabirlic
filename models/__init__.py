from datetime import datetime
from sqlalchemy import Unicode, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, composite, relationship

from sqlalchemy import Column, ForeignKey
from sqlalchemy import DateTime, Integer, String, Boolean
from phonenumbers.phonenumber import PhoneNumber

DATABASE_PATH = "sqllite:///../database.db"

engine = create_engine(DATABASE_PATH, connect_args={
                       "check_same_thread": False})
SessionLocal = sessionmaker(autocommit=True, autoflush=False, bind=engine)

Base = declarative_base()


class Distribution(Base):
    __tablename__ = "distributions"

    id = Column(Integer, autoincrement=True, primary_key=True, index=True)
    start_datetime = Column(DateTime, default=datetime.now, nullable=False)
    message = Column(String, nullable=False)
    code_mobile_operator = Column(String, nullable=False)
    end_datetime = Column(DateTime, onupdate=datetime.now)
    child = relationship(
        "Message", back_populates="distribution", uselist=False)


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, autoincrement=True, primary_key=True, index=True)
    phone_number = composite(PhoneNumber, Column(Unicode(11), 'FI'))
    code_mobile_operator = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.now)
    child = relationship("Message", back_populates="users", uselist=False)


class Message(Base):
    __tablename__ = "messages"

    id = Column(Integer, autoincrement=True, primary_key=True, index=True)
    sending_at = Column(DateTime, default=datetime.now, nullable=False)
    is_sended = Column(Boolean, default=False, onupdate=True)

    distribution_id = Column(Integer, ForeignKey('distribution.id'))
    distribution = relationship("Distribution", back_populates="child")

    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship("User", back_populates="children")
