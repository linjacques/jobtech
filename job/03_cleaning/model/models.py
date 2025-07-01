from sqlalchemy import Column, Integer, String, Text
from db.mysql_con import Base

class adzuna_job(Base):
    __tablename__ = "adzuna_job"

    id = Column(Integer, primary_key=True)
    job_title = Column(String(255))        
    company = Column(String(255))          
    location = Column(String(255))    
    industry = Column(String(255))         
    description = Column(Text)             
    skills = Column(Text)                  

class database(Base):
    __tablename__ = "database"

    id = Column(Integer, primary_key=True)
    database = Column(String(100))       
    usage_count = Column(Integer)         

class web_framework(Base):
    __tablename__ = "web_framework"

    id = Column(Integer, primary_key=True)
    web_framework = Column(String(100))   
    usage_count = Column(Integer)         

class platform(Base):
    __tablename__ = "platform"

    id = Column(Integer, primary_key=True)
    platform = Column(String(100))       
    usage_count = Column(String(100))     

class top_tech(Base):
    __tablename__ = "top_tech"

    id = Column(Integer, primary_key=True)
    technology = Column(String(100))      
    offer_count = Column(Integer)         
