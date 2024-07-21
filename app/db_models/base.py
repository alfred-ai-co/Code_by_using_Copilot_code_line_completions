from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
import datetime


Base = declarative_base()


class Project(Base):
    __tablename__ = "projects"
    
    
    tickets = relationship("Ticket", back_populates="project")

class Ticket(Base):
    __tablename__ = "tickets"
    
    
    project = relationship("Project", back_populates="tickets")
