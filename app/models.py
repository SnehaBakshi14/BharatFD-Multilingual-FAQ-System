from datetime import datetime
from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class FAQ(Base):
    __tablename__ = "faqs"
    
    id = Column(Integer, primary_key=True, index=True)
    question_en = Column(Text, nullable=False)
    answer_en = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    translations = relationship("FAQTranslation", back_populates="faq", cascade="all, delete-orphan")

class FAQTranslation(Base):
    __tablename__ = "faq_translations"
    
    id = Column(Integer, primary_key=True, index=True)
    faq_id = Column(Integer, ForeignKey("faqs.id", ondelete="CASCADE"))
    language = Column(String(2), nullable=False)  # e.g., 'hi', 'bn'
    question = Column(Text, nullable=False)
    answer = Column(Text, nullable=False)
    
    faq = relationship("FAQ", back_populates="translations")