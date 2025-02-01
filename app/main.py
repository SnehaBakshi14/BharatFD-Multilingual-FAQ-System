from fastapi import FastAPI, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List
import json

from . import models, schemas, translation
from .database import engine, get_db, redis_client

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Multilingual FAQ System")

@app.post("/faqs/", response_model=schemas.FAQ)
async def create_faq(faq: schemas.FAQCreate, db: Session = Depends(get_db)):
    db_faq = models.FAQ(
        question_en=faq.question_en,
        answer_en=faq.answer_en
    )
    db.add(db_faq)
    db.commit()
    db.refresh(db_faq)
    
    # Auto-translate to supported languages
    supported_langs = ['hi', 'bn']  # Add more as needed
    for lang in supported_langs:
        trans = models.FAQTranslation(
            faq_id=db_faq.id,
            language=lang,
            question=translation.translate_text(faq.question_en, lang),
            answer=translation.translate_text(faq.answer_en, lang)
        )
        db.add(trans)
    
    db.commit()
    db.refresh(db_faq)
    return db_faq

@app.get("/faqs/", response_model=List[schemas.FAQ])
async def get_faqs(
    skip: int = 0,
    limit: int = 10,
    lang: str = Query(None, max_length=2),
    db: Session = Depends(get_db)
):
    # Try to get from cache first
    cache_key = f"faqs:{lang}:{skip}:{limit}"
    cached_data = redis_client.get(cache_key)
    
    if cached_data:
        return json.loads(cached_data)
    
    faqs = db.query(models.FAQ).offset(skip).limit(limit).all()
    
    # If language is specified, ensure translations are loaded
    if lang and lang != 'en':
        for faq in faqs:
            if not any(t.language == lang for t in faq.translations):
                # Create missing translation
                trans = models.FAQTranslation(
                    faq_id=faq.id,
                    language=lang,
                    question=translation.translate_text(faq.question_en, lang),
                    answer=translation.translate_text(faq.answer_en, lang)
                )
                db.add(trans)
        db.commit()
    
    # Cache the results
    redis_client.setex(
        cache_key,
        300,  # Cache for 5 minutes
        json.dumps([{
            "id": faq.id,
            "question_en": faq.question_en,
            "answer_en": faq.answer_en,
            "created_at": faq.created_at.isoformat(),
            "updated_at": faq.updated_at.isoformat(),
            "translations": [{
                "id": t.id,
                "faq_id": t.faq_id,
                "language": t.language,
                "question": t.question,
                "answer": t.answer
            } for t in faq.translations]
        } for faq in faqs])
    )
    
    return faqs