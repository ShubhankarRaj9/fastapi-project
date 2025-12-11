from fastapi import APIRouter,Depends
from .. import schemas,models,database
from sqlalchemy.orm import Session
# from ..hashing import Hash
from ..repository import user

router = APIRouter(
    prefix='/user',
    tags=['User']
)

#create method
@router.post('/', response_model=schemas.ShowUser)
def create_user(request:schemas.User, db:Session = Depends(database.get_db)):
    return user.create_user(request,db)


# retrieve method
@router.get('/{id}', response_model=schemas.ShowUser)
def get_user(id:int, db:Session = Depends(database.get_db)):
    return user.get_user(id,db)

