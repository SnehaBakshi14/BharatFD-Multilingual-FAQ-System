from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class FAQTranslationBase(BaseModel):
    language: str
    question: str
    answer: str

class FAQTranslationCreate(FAQTranslationBase):
    pass

class FAQTranslation(FAQTranslationBase):
    id: int
    faq_id: int

    class Config:
        from_attributes = True

class FAQBase(BaseModel):
    question_en: str
    answer_en: str

class FAQCreate(FAQBase):
    translations: Optional[List[FAQTranslationCreate]] = None

class FAQ(FAQBase):
    id: int
    created_at: datetime
    updated_at: datetime
    translations: List[FAQTranslation] = []

    class Config:
        from_attributes = True