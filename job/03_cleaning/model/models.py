from sqlalchemy import Column, Integer, String, Text, DateTime
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

class github_repo(Base):
    __tablename__ = "github_repo"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255))
    owner = Column(String(255))
    language = Column(String(100))
    stargazers_count = Column(Integer)
    forks_count = Column(Integer)
    html_url = Column(String(500))
    open_issues_count = Column(Integer)
    watchers_count = Column(Integer)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    license = Column(String(255))
    homepage = Column(String(500))    

class remoteok_job(Base):
    __tablename__ = "remoteok_job"

    id = Column(Integer, primary_key=True, autoincrement=True)

    source = Column(String(100))       
    country = Column(String(100))      
    job_title = Column(String(255))    
    company = Column(String(255))      
    job_link = Column(Text)         

class job_offer(Base):
    __tablename__ = "job_offer"

    id = Column(Integer, primary_key=True, autoincrement=True)

    job_title = Column(String(255))  
    company = Column(String(255))     
    salary = Column(String(100))        
    contract = Column(String(100))       
    remote = Column(String(50))          
    city = Column(String(100))          
