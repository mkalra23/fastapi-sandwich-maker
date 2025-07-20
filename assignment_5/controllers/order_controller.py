from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import models, schemas, database

router = APIRouter(prefix="/orders", tags=["Orders"])

# Dependency
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# GET all orders
@router.get("/", response_model=list[schemas.OrderDetail])
def read_orders(db: Session = Depends(get_db)):
    return db.query(models.OrderDetail).all()

# GET one order
@router.get("/{order_id}", response_model=schemas.OrderDetail)
def read_order(order_id: int, db: Session = Depends(get_db)):
    order = db.query(models.OrderDetail).filter(models.OrderDetail.id == order_id).first()
    if order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    return order

# CREATE order
@router.post("/", response_model=schemas.OrderDetail)
def create_order(order: schemas.OrderDetailCreate, db: Session = Depends(get_db)):
    db_order = models.OrderDetail(**order.dict())
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order

# UPDATE order
@router.put("/{order_id}", response_model=schemas.OrderDetail)
def update_order(order_id: int, order: schemas.OrderDetailCreate, db: Session = Depends(get_db)):
    db_order = db.query(models.OrderDetail).filter(models.OrderDetail.id == order_id).first()
    if db_order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    for key, value in order.dict().items():
        setattr(db_order, key, value)
    db.commit()
    db.refresh(db_order)
    return db_order

# DELETE order
@router.delete("/{order_id}")
def delete_order(order_id: int, db: Session = Depends(get_db)):
    db_order = db.query(models.OrderDetail).filter(models.OrderDetail.id == order_id).first()
    if db_order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    db.delete(db_order)
    db.commit()
    return {"message": "Order deleted successfully"}


