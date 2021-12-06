from sqlalchemy import Table, Column, engine
from sqlalchemy.sql.sqltypes import Integer, String
from config.db import Base


class Forms(Base):
    __tablename__ = "forms"
    __table_args__ = {"autoload": True}

