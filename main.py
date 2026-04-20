from fastapi import FastAPI
from db.session import engine, Base
from api.v1.light_crdu_int import router as light_router

#自动创建表
Base.metadata.create_all(bind=engine)

app = FastAPI(title="灯具信息Api")

#挂载路由
app.include_router(light_router, prefix="/api/v1/lights", tags=["灯具信息"])


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)