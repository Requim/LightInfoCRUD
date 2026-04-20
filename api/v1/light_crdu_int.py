from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.session import get_db
from db.data_struct import LightFixture
from schemas.light import LightCreate, LightResponse
from typing import List

router = APIRouter()

@router.post("/", response_model=LightResponse)
def create_light(light: LightCreate, db: Session = Depends(get_db)):
    db_light = LightFixture(**light.model_dump())
    db.add(db_light)
    db.commit()
    db.refresh(db_light)
    return db_light


@router.get("/", response_model=List[LightResponse])
def read_lights(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(LightFixture).offset(skip).limit(limit).all()


@router.delete("/{light_id}")
def delete_light(light_id: int, db: Session = Depends(get_db)):
    item = db.query(LightFixture).filter(LightFixture.id == light_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="灯具不存在")
    db.delete(item)
    db.commit()
    return {"message": "Success"}


@router.put("/{light_id}", response_model=LightResponse)
def update_light(
        light_id: int,
        light_update: LightCreate,
        db: Session = Depends(get_db)
):
    db_light = db.query(LightFixture).filter(LightFixture.id == light_id).first()
    if not db_light:
        raise HTTPException(status_code=404, detail="灯具不存在")

    #更新字段数据
    update_data = light_update.model_dump()
    for key, value in update_data.items():
        setattr(db_light, key, value)

    db.commit()
    db.refresh(db_light)
    return db_light