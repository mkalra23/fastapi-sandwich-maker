from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import models, schemas, database

router = APIRouter(prefix="/sandwiches", tags=["Sandwiches"])

# Dependency to get DB session
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


# GET all sandwiches
@router.get("/", response_model=list[schemas.Sandwich])
def read_sandwiches(db: Session = Depends(get_db)):
    return db.query(models.Sandwich).all()


# GET sandwich by ID
@router.get("/{sandwich_id}", response_model=schemas.Sandwich)
def read_sandwich(sandwich_id: int, db: Session = Depends(get_db)):
    sandwich = db.query(models.Sandwich).filter(models.Sandwich.id == sandwich_id).first()
    if sandwich is None:
        raise HTTPException(status_code=404, detail="Sandwich not found")
    return sandwich


# POST create sandwich
@router.post("/", response_model=schemas.Sandwich)
def create_sandwich(sandwich: schemas.SandwichCreate, db: Session = Depends(get_db)):
    db_sandwich = models.Sandwich(**sandwich.dict())
    db.add(db_sandwich)
    db.commit()
    db.refresh(db_sandwich)
    return db_sandwich


# PUT update sandwich
@router.put("/{sandwich_id}", response_model=schemas.Sandwich)
def update_sandwich(sandwich_id: int, sandwich: schemas.SandwichCreate, db: Session = Depends(get_db)):
    db_sandwich = db.query(models.Sandwich).filter(models.Sandwich.id == sandwich_id).first()
    if db_sandwich is None:
        raise HTTPException(status_code=404, detail="Sandwich not found")
    for key, value in sandwich.dict().items():
        setattr(db_sandwich, key, value)
    db.commit()
    db.refresh(db_sandwich)
    return db_sandwich


# DELETE sandwich
@router.delete("/{sandwich_id}")
def delete_sandwich(sandwich_id: int, db: Session = Depends(get_db)):
    db_sandwich = db.query(models.Sandwich).filter(models.Sandwich.id == sandwich_id).first()
    if db_sandwich is None:
        raise HTTPException(status_code=404, detail="Sandwich not found")


