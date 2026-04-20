from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from conf.config import settings

engine = create_engine(
    settings.DATABASE_URL,
    pool_size=10,        #连接池基础大小
    max_overflow=20,     #允许临时超出的连接数
    pool_pre_ping=True   #每次使用前检查连接是否有效（防止闪断）
)


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()