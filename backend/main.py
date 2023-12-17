from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.users import router as usersrouter
app = FastAPI()
app.include_router(usersrouter)


origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {"data": "1234"}