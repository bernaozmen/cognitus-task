from sqlalchemy.orm import Session

from models import Record


def get_user(db: Session, user_id: int):
    return db.query(Record).filter(Record.id == user_id).first()


def get_user_text(db: Session, text: str):
    return db.query(Record).filter(Record.text == text).first()


def get_users(db: Session):
    return db.query(Record).all()

'''
def create_user(db: Session, user: schemas.UserCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = models.User(email=user.email, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Item).offset(skip).limit(limit).all()


def create_user_item(db: Session, item: schemas.ItemCreate, user_id: int):
    db_item = models.Item(**item.dict(), owner_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item
'''