from datetime import datetime
from fastapi import  APIRouter, HTTPException, status , Response
from pydantic import BaseModel,Field,root_validator,validator
from typing import Optional, List
import hashlib
from db import bp_database
from auth import generate_token
clients_collection = bp_database["clients"]
print(bp_database,clients_collection)

router = APIRouter()


def generate_date():
   print(datetime.utcnow())
   return datetime.utcnow()

def generate_user_identity():
    print("hello world")
    

def hash_password(password):
    h = hashlib.new("SHA256")
    h.update((password).encode())
    return h.hexdigest()

class BloodPressure_record(BaseModel):
    date: datetime = Field(default_factory=datetime.utcnow)
    systolic:int
    diastolic:int
    pr:Optional[str]


class Monthly_records(BaseModel):
    name:str
    records:List[BloodPressure_record]





class NewUser(BaseModel):
    #firstname: str
    #lastname: str
    email: Optional[str]
    password: Optional[str]
    activated: bool = False
    created_at: datetime = Field(default_factory=generate_date)
    #user_identity: generate_user_identity()
    #records_2023:Monthly_records
     
    #user_identity: str = Field(default_factory=generate_date)

    # @classmethod
    # @root_validator(pre=True)
    # def set_created_at(cls, values):
    #     if "created_at" not in values:
    #         values["created_at"] = generate_date()
    #     return values
    # @classmethod
    # @root_validator(pre=True)
    # def set_user_identity(cls,values):
    #     if "user_identity" not in values:
    #         values["user_identity"] = str(values[""])
    #     return values

        

def check_existence(user: NewUser)-> bool:
    item = clients_collection.find_one({"email":user.email})
    return True if item else False 
    

class LoginUser(BaseModel):
    email: str
    password: str


class LoggedUser(BaseModel):
    email: str
    password: str
    activated: bool
    created_at: str





@router.get("/users")
async def read_users():
    return {"code": "code"}


@router.post("/users/signup", status_code=status.HTTP_201_CREATED)
async def create_user(user: NewUser): 
    has_account = check_existence(user)
    if has_account:
        raise HTTPException(409,{"code":"409","error": "User already exists",
                                    "message": "The user with the specified credentials already exists in the system."})
    else:
        hashed_password = hash_password(user.password)
        user.password = hashed_password
        x = clients_collection.insert_one(user.dict())
        print(x.inserted_id)
        return {"code": 201, "message":f"successfully created an account for {user.email} "}



@router.post("/users/login", status_code=status.HTTP_200_OK)
async def login(user: LoginUser,response:Response):
    match(user.email,user.password):
        case("",""):
            raise HTTPException(400,{"code":400,"error":"Bad Request","message":"Please provide both email and password for login."})
    retrieved = clients_collection.find_one({"email":user.email})
    claiming_hash = hash_password(user.password)
    match (retrieved):
        case (None):
            raise HTTPException(404,detail={"code":404, "error":"Unauthorized","message":f"Log in failed because there was no account associated with {user.email}"})
    match(retrieved["email"]==user.email,claiming_hash ==retrieved["password"]):
        case(True,False):
            raise HTTPException(401,{"code":401,"error":"Unauthorized","message":"Incorrect password. Please try again."})
        case (True,True):
            response.set_cookie(key="jwt", value = generate_token(user),httponly=True)
            return {"code":200,"message":"Successful Login"}



    
@router.get("/users/{user_identity}")
async def return_user_page(user_identity):
    return {"user_identity":user_identity}