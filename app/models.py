from sqlalchemy import String
from sqlalchemy.orm import mapped_column, Mapped
from .db import Base

class User(Base):
    __tablename__ = "user"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30) nullable=True)
    email: Mapped[str | None] = mapped_column(String(225), unique=True, nullable=False) #type can be None bc can be empty

    