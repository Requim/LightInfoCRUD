from sqlalchemy import Column, Integer, String
from db.session import Base


class LightFixture(Base):
    __tablename__ = "lights"
    #增加索引方便查找
    id = Column(Integer, primary_key=True, index=True)
    brand = Column(String(50), nullable=False, index=True)
    model = Column(String(100), nullable=False, index=True)
    power = Column(Integer, nullable=False)
    color_temp = Column(Integer, nullable=False)