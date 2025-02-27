from sqlalchemy import (Column, String, ForeignKey,
                        Integer, Boolean, DateTime)
from sqlalchemy.orm import relationship
from db import Base
from datetime import datetime


# Создаем модель User
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(52), nullable=False)
    phone_number = Column(String, nullable=False)
    level = Column(String, default="Select your level")
    reg_date = Column(DateTime, default=datetime.now())


# Создаем модель Question
class Question(Base):
    __tablename__ = "questions"

    id = Column(Integer, primary_key=True, autoincrement=True)
    question_text = Column(String, nullable=False)
    level = Column(String, default="easy")
    v1 = Column(String)
    v2 = Column(String)
    v3 = Column(String)
    v4 = Column(String)
    correct_answer = Column(String, nullable=False)


# Cоздаем модель UserAnswer
class UserAnswer(Base):
    __tablename__ = "user_answers"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    question_id = Column(Integer, ForeignKey("questions.id"))
    answer = Column(String)
    correctness = Column(Boolean, default=False)
    level = Column(String)

    user_fk = relationship(User, lazy="subquery", foreign_keys=[user_id])
    question_fk = relationship(Question, lazy="subquery", foreign_keys=[question_id])


# Создаем модель Result
class Result(Base):
    __tablename__ = "results"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    correct_answers = Column(Integer, default=0)
    level = Column(String)

    user_fk = relationship(User, lazy="subquery")
