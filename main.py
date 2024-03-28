from fastapi import FastAPI, Depends
import models
from database import engine
from api import auth, todos

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

app.include_router(auth.router, tags=["auth"])
app.include_router(todos.router, tags=["todos"])
# app.include_router(address.router, tags=["address"])
