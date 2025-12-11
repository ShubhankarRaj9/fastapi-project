from fastapi import APIRouter,Depends,status,Response,HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from .. import schemas, database, models, token
from sqlalchemy.orm import Session
# import jwt
from ..hashing import Hash


router = APIRouter(
    tags=['Authentication']
)

@router.post('/login')
def login(request:OAuth2PasswordRequestForm=Depends(), db:Session = Depends(database.get_db)):
    user= db.query(models.User).filter(models.User.email == request.username).first()
    if not user:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,
         detail=f'Invalid Credentials')    
    if not Hash.verify(user.password, request.password):
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,
         detail=f'Incorrect password')


    # need jwt-token not user
    # access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = token.create_access_token(
        data={"sub": user.email}
        #  expires_delta=access_token_expires
        )
    return {"access_token": access_token, "token_type": "bearer"}

    return user